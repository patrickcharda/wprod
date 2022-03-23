"""import psycopg2
# Connect to an existing database
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % ("localhost", "drones", "postgres", "Sop7x6clabonne!"))
print(conn)"""

"""
a=[1]
print(id(a))
a+=[2]
print(a)
print(id(a))
new_a =[]
for e in a:
    new_a.append(e)
print(new_a)
print(id(new_a))
print(dir(a))
"""
def f():
    print(list(dir(f)))
f()
# print(f.__module__)
print(f.__defaults__) # valeur des params obligatoires par défaut, représentés par des variables
print(f.__kwdefaults__)
print(f.__annotations__)
def g(a=0, b=0, c=0, *args, d=7):
    print(locals())
print(g.__defaults__) # (0, 0, 0)
print(g.__kwdefaults__) # None
g() # {'a': 0, 'b': 0, 'c': 0}
g(b=6) # {'a': 0, 'b': 6, 'c': 0}

def h(*args):
    return locals()
h(5,9,8,7,4)

def h(*args, **kwargs) :
	return locals()
h(8,6,5,4,a=2,b=0,c=8,d='test') # {'args': (8, 6, 5, 4), 'kwargs': {'a': 2, 'b': 0, 'c': 8, 'd': 'test'}} 
# args (n-uplet) et kwargs (dictionnaire) sont des variables locales à la fonction

def h(**kwargs) :
	locals().update(**kwargs) # => passe les paramètres nommés en variables de la fonction
	del kwargs
	return locals()
h(a=9, b=11, c= 'toi') # {'a': 9, 'b': 11, 'c': 'toi'}

def f(a, b=0, *args, **kwargs):
    return a + b + sum(args) + sum(kwargs.values())

f(1, 2, 3, 4, y=5, z=6) # 21
# Ordre : arguments obligatoires en premier, arguments optionnels ensuite, paramètres extensibles enfin
# avec arguments non nommés d'abord (ici 3 et 4), puis arguments nommés (y et z)
# La fonction f(…) n’a qu’un seul paramètre obligatoire qui est a (b ayant une valeur par défaut)

#paramètres étoilés : 1* pour les paramètres non nommés, 2** pour les paramètres nommés
f(*[1, 2, 3, 4], **{'y': 5, 'z': 6}) # ou f(*(1, 2, 3, 4), **{'y': 5, 'z': 6}) parenthèses ou crochets, c'est au choix 


def f2(b, c, *args, **kwargs):
    return locals()

datas = {
    'a':1,
    'b':2,
    'c':2,
    'name':'bob',
}
f1(**datas) # {'a': 1, 'b': 2, 'args': (), 'kwargs': {'c': 2}}
f2(**datas) # {'b': 2, 'c': 2, 'args': (), 'kwargs': {'a': 1}}
f2(**{'a':9,'b':8,'c':7}) # {'b': 8, 'c': 7, 'args': (), 'kwargs': {'a': 9}}

# Annotations pr contrôle du type des params passés à une fonction
def wrapper(f):
    def wrapped(*args, **kw):
        for n, t in f.__annotations__.items():
            if n == 'return':
                continue
            a = type(kw.get(n, f.__kwdefaults__ != None and f.__kwdefaults__.get(n) or None))
            if a != t:
                raise TypeError("L'argument %s devrait ê de type %s mais il est de type %s" % (n,t, type(a)))
            r=f(**kw)
            if 'return' in f.__annotations__:
                if type(r) != f.__annotations__['return']:
                    raise TypeError("le type du résultat devrait ê %s et il est %s" % (f.__annotations__['return'], type(r)))
            return r
        return wrapped
@wrapper
def f(*args,a:str, b:int=42)->int:
    print('f', locals())
    return 1

f(a='', b=1)

# OBJET

class C :
	def methode_instance(self, *args, **kwargs) :
		return 'ceci est une méthode d’instance appliquée sur %s' %self

	@classmethod
	def methode_classe(cls, *args, **kwargs) :
		return 'ceci est une methode de classe appliquée sur %s' %cls

	@staticmethod
	def methode_statique(*args, **kwargs):
		return 'ceci est une méthode statique'

c=C()
print(c.methode_instance())
print(C.methode_instance(c))
print(C.methode_classe())
print(c.methode_classe())
print(C.methode_statique())
print(c.methode_statique())

f=c.methode_instance
f()
f=C.methode_instance # appel statique d'une méthode d'instance
f(c)

# l'appel statique est utilisé pour l'appel d'une méthode d'un père :
class Z:
    def methode_instance(self):
        result= Y.methode_instance(self)
        result += X.methode_instance(self)
        return result

class Ma_classe:
    def __init__(self, variable) -> None:
        self.attribute = variable
        self.other = []
    def methode(self):
        return self.attribute


ex = Ma_classe('toto')
print(ex.methode())
chaine = 'du blabla'
ex = Ma_classe(chaine)
print(ex.methode())

class La_class:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            # self.__dict__[k] = v # ou moins élégant : setattr(self, k, v)
            # ou le plus élégant :
            self.__dict__.update(kwargs)

alpha = {'a':'arbre','b':'bouleau', 'c':'châtaignier'}

lex = La_class(**alpha)
print(lex.__dict__) # {'a':'arbre','b':'bouleau', 'c':'châtaignier'}

class Point:
    def __init__(self, x, y) -> None:
        self.x, self.y = x, y
    def module(self, other=None):
        if other is None:
            other= Point(0,0)
        return ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5

p1= Point(2, -3)
p1.module()
p2= Point(2, 4)
p2.module()

class Rectangle:
    def __init__(self, largeur, longueur) -> None:
        self.largeur, self.longueur = largeur, longueur
    def aire(self, other=None):
        if other is None:
            other = Rectangle(0,0)
        return(((self.largeur)*(self.longueur))+((other.largeur)*(other.longueur)))

r1=Rectangle(2,4)
r1.aire()
r2=Rectangle(7,9)
r2.aire()
r1.aire(r2)

class Point3D:
    def __init__(self, x, y, z) -> None:
        self.x, self.y, self.z = x, y, z
    def module(self):
        return (self.x**2+self.y**2+self.z**2)**0.5

class Point2D(Point3D):
    def __init__(self, x, y) -> None:
        Point3D.__init__(self, x, y, 0) # appel statique
        
class Point1D(Point2D):
    def __init__(self, x) -> None:
        Point2D.__init(self, x, 0)

# polymorphisme paramétrique

from curses.ascii import EM
from functools import singledispatch
@singledispatch
def func(arg) :
	print('comportement par défaut')

@func.register(int)
@func.register(float)
def _(arg) :
	print('comportement pour un nombre')

func('test') # comportement par défaut
func(4) # comportement pour un nombre

class Custom:
	pass

@func.register(Custom)
def _(arg) :
	print('comportement pour une classe custom')

>>> func.registry.keys() # registre asssociant fonctions (ou méthodes) et type
dict_keys([<class 'object'>, <class 'float'>, <class 'int'>, <class '__main__.Custom'>])
        
        
>>> func.registry.values()
dict_values([<function func at 0x0000029F12EF01F0>, <function _ at 0x0000029F12EF05E0>, <function _ at 0x0000029F12EF05E0>, <function _ at 0x0000029F12EF0550>])  

# HERITAGE MULTIPLE

class Point:
    def __init__(self, x, y) -> None:
        self.x, self.y = x, y
    def module(self, other=None):
        if other is None:
            other= Point(0,0)
        return ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5  

class Batiment:
    def __init__(self, nom, ressources) -> None:
        self.nom = nom
        self.ressources = ressources
    def produire(self):
        return '%s produit %s' % (self.nom, self.ressources)
    
class BatimentUnique(Batiment, Point):
    def __init__(self, nom, ressources, x, y) -> None:
        Batiment.__init__(self, nom, ressources)
        Point.__init__(self, x,y)

mine = BatimentUnique('mine', ['Or', 'Platine'], 0, 42)
mine.produire()
mine.module()

# Interfaces

import csv

class File:
    def __iter__(self):
        return self
    def __next__(self):
        raise StopIteration
    
file = File()
csv.reader(file)

try:
    iter = file.__iter__()
    while True:
        res= iter.__next__()
        print(res)
except StopIteration:
    print('Terminé')
except:
    raise TypeError('Doit ê un itérateur')

# Informal Interfaces

class InformalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text."""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Extract text from the currently loaded file."""
        pass

class PdfParser(InformalParserInterface): # concrete implementation
    """Extract text from a PDF"""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides InformalParserInterface.extract_text()"""
        pass

class EmlParser(InformalParserInterface): # concrete implementation
    """Extract text from an email"""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override InformalParserInterface.extract_text()
        """
        pass

issubclass(PdfParser, InformalParserInterface) # True
issubclass(EmlParser, InformalParserInterface) # True ! -> it violates the definition of an interface !
PdfParser.__mro__
EmlParser.__mro__

# Informal interface using metaclasses

    # on veut que issubclass(EmlParser, InformalParserInterface) retourne False
    
class ParserMeta(type):
    """A Parser metaclass that will be used for parser class creation.
    """
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text))
        
class UpdatedInformalParserInterface(metaclass=ParserMeta):
    """This interface is used for concrete classes to inherit from.
    There is no need to define the ParserMeta methods as any class
    as they are implicitly made available via .__subclasscheck__().
    """
    pass

class PdfParserNew:
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides UpdatedInformalParserInterface.extract_text()"""
        pass

class EmlParserNew:
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides UpdatedInformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override UpdatedInformalParserInterface.extract_text()
        """
        pass

issubclass(PdfParserNew, UpdatedInformalParserInterface) # True
issubclass(EmlParserNew, UpdatedInformalParserInterface) # False

PdfParserNew.__mro__ # (<class '__main__.PdfParserNew'>, <class 'object'>) 
# -> UpdatedInformalParserInterface n'apparaît pas dans la résolution bien qu'il s'agisse d'une superclasse de PdfParserNew.
# cela vient du fait que UpdatedInformalParserInterface est une classe virtuelle de PdfParserNew

Autre exemple d interface utilisant une métaclasse

class PersonMeta(type):
    """A person metaclass"""
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'name') and 
                callable(subclass.name) and 
                hasattr(subclass, 'age') and 
                callable(subclass.age))

class PersonSuper:
    """A person superclass"""
    def name(self) -> str:
        pass

    def age(self) -> int:
        pass

class Person(metaclass=PersonMeta):
    """Person interface built from PersonMeta metaclass."""
    pass

Here, you have the setup for creating your virtual base classes:

The metaclass PersonMeta
The base class PersonSuper
The Python interface Person

# Inheriting subclasses
class Employee(PersonSuper):
    """Inherits from PersonSuper
    PersonSuper will appear in Employee.__mro__
    """
    pass

class Friend:
    """Built implicitly from Person
    Friend is a virtual subclass of Person since
    both required methods exist.
    Person not in Friend.__mro__
    """
    def name(self):
        pass

    def age(self):
        pass
    
issubclass(Friend, Person) # False mais Person est une classe virtuelle de Friend car Friend implémente son interface
isinstance(Friend, Person) # False
issubclass(Employee, Person) # False
isinstance(Employee, Person) # False
issubclass(Employee, PersonSuper) # True
isinstance(Employee, PersonSuper) # False

# Formal interfaces using abc.ABMeta

import abc

class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text))

class PdfParserNew:
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass

class EmlParserNew:
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass

issubclass(PdfParserNew, FormalParserInterface) # True
issubclass(EmlParserNew, FormalParserInterface) # False

# using abstract metho declaration

class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text) or 
                NotImplemented)

    @abc.abstractmethod
    def load_data_source(self, path: str, file_name: str):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def extract_text(self, full_file_path: str):
        """Extract text from the data set"""
        raise NotImplementedError

class PdfParserNew(FormalParserInterface):
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass

class EmlParserNew(FormalParserInterface):
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass
    
pdf_parser = PdfParserNew()
issubclass(PdfParserNew, FormalParserInterface) # True
eml_parser = EmlParserNew() # lève une erreur car la méthode abstraite extract_text n'est pas implémentée
# c est le comportement attendu qd on met en place une interface formelle

https://realpython.com/python-interface/#using-metaclasses

# ATTRIBUTS ET VISIBILITE

# L’accessibilité passe par les 3 méthodes : __getattr__ __setattr__ __delattr__

class A:
    read_only = ['x', 'y']
    x, y, z = 'X', 'Y', 'Z'
    def __setattr__(self, name, value):
        if name in self.read_only:
            raise Exception('read-only attribute')
        else:
            return object.__setattr__(self, name, value)
    def __delattr__(self, name):
        if name in self.read_only:
            raise Exception('read_only attribute')
        else:
            return object.__delattr__(self, name)

a=A()
a.x
a.x='eegfr'
del a.x

# nb : il est toujours possible de modifier read_only ou les fonctions __setattr__ et __delattr__
# si on le voulait il faudrait transformer read_only en n-uplet et lui ajouter son propre nom en élément,
# ainsi que celui des fonctions __setaatr__ et __delattr__

# Pour rendre un attribut privé, par convention on le préfixe d'un underscore; il reste mofifiable,
# mais sa visibilité est limitée au module courant (il n'est pas exportable, la primitive import
# ne tenant pas compte des attributs, fonctions ou classes préfixés d'un underscore)
# les attributs préfixés par 2 underscores ont invisibles et privés

class A:
    def __m(self):
        return 1
A.__m() # AttributeError: type object 'A' has no attribute '__m'
a=A()
dir(a)
# => on s'aperçoit qu'en réalité une méthode _A__m existe, ainsi appelable :
a._A__m()
A._A__m(a)

# PROPRIETES

# Mécanisme visant à rendre accessible une méthode comme s'il s'agissait d'un attribut

class Bulletin:
    def __init__(self, *notes) -> None:
        self.notes = list(notes)
    @property
    def moyenne(self):
        if len(self.notes):
            return sum(self.notes)/len(self.notes)
        return None
    @property
    def derniere_note(self):
        if len(self.notes):
            return self.notes[-1]
        return None
    # ce mécanisme fonctionne aussi avec le setter et le deleter
    @derniere_note.setter
    def derniere_note(self, note):
        self.notes.append(note)
    @derniere_note.deleter
    def derniere_note(self):
        self.notes.pop()
    
bulletin = Bulletin(12, 13, 16, 19)
bulletin.moyenne, bulletin.derniere_note # (15.0, 19)
bulletin.derniere_note = 10
bulletin.moyenne, bulletin.derniere_note # (14.0, 10)
        
class A:
    __attr = 0
    @property
    def attribut(self):
        return self.__attr
    @attribut.setter
    def attribut(self, value):
        self.__attr = value
    @attribut.deleter
    def attribut(self):
        del self.__attr

# si on ne fournit ni setter ni deleter, l'attribut attribut sera protégé (mais on pourra tjrs accéder à __attr via _A__attr )

a = A()
a.attribut = 42
a.attribut, a._A__attr # (42, 42)
del a.attribut
a.attribut # 0
a.attribut = 99
a.attribut # 99
a.attribut = 77
a.attribut # 77
a._A__attr # 77
del a._A__attr
a.attribut # 0
a.attribut = 66
a.attribut # 66
a._A__attr # 66


class Calcul:
    num1 = 10 #attribut de classe

    def __init__(self, num2):
        self.num2 = num2 #attribut d'instance

    def mtd_instance(self, num3):
        print("Une méthode normale.")
        return self.num1 + self.num2 + num3

    @classmethod 
    def mtd_class(cls, num3):
        print("Une methode de classe.") 
        return cls.num1 + num3 

    @staticmethod 
    def mtd_statique(num3):
        print("Une methode statique.") 
        return num3
    
    @staticmethod
    def mtd_static(num4):
        print("une méthode statique")
        return num4 + Calcul.num1
    
obj1 = Calcul(20)
# print(obj1.num1) # 10
## obj1.num1 = 100
print(obj1.mtd_instance(30)) # 60 ## 150
print(obj1.mtd_class(30)) # 40 ## 40
print(Calcul.mtd_class(30)) # 40 ## 40
print(obj1.mtd_statique(30)) # 30 ## 30
print(Calcul.mtd_statique(30)) # 30 ## 30
print(Calcul.mtd_static(4)) ## 14 

class A:
    __slots__ = ['a','b']
    
a=A()
a.a= 4
a.b= 'x'
a.c= 4 # 'A' object has no attribute c
def b():
    print('I am the b function of A')
a.b = b
a.b() # I am the b function of A
a.__slots__
dir(a)

# METACLASSES

# https://zestedesavoir.com/tutoriels/954/notions-de-python-avancees/4-classes/1-types/
# https://realpython.com/python-metaclasses/


class Point2D(tuple):
    def __new__(cls, x, y):
        return super().__new__(cls, (x, y))

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]
    
Foo= type('Foo', (), {}) # équivalent à class Foo: pass
x= Foo()
x # <__main__.Foo object at 0x0000029F12F16DD0>

Bar = type('Bar', (Foo,), dict(attr=100)) # équivalent à à class Bar(Foo): attr=100
x= Bar()
x.attr # 100
x.__class__ # <class '__main__.Bar'>
x.__class__.__bases__ # (<class '__main__.Foo'>,)

# autre exemple
def f(obj):
    print('attr = ', obj.attr)

Foo = type(
    'Foo',
    (),
    {
        'attr': 100,
        #'attr_val': lambda x : x.attr
        'attr_val': f
    }
)
x = Foo()
x.attr # 100
x.attr_val() # attr = 100

# ce qui précède équivaut à

def f(obj):
    print('attr = ', obj.attr)
    
class Foo:
    attr=100
    """def attr_val(self):
        return self.attr = 100"""
    attr_val = f
x = Foo()
x.attr # 100
x.attr_val() # attr = 100

# autre exemple :

class Foo:
    pass

def new(cls):
    x= object.__new__(cls)
    x.attr = 100
    return x

Foo.__new__ = new

f= Foo()
f.attr # 100

# Une autre façon de faire des métaclasses personnalisées, plus conventionnelle :

class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x

class Foo(metaclass=Meta):
    pass

Foo.attr # 100
y = Foo()
y.attr # 100

        


