import os
from datetime import timedelta
from decouple import config, Csv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG',cast=bool)

ALLOWED_HOSTS = ['localhost','127.0.0.1','192.168.1.16','*']
#ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS='*'


# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django_extensions',
	'corsheaders',
	# Django REST framework
	'rest_framework',
	# Toys application
	#'toys.apps.ToysConfig',
	# Drones application
	#'drones.apps.DronesConfig',
	# Wprod aplication,
	'wprod.apps.WprodConfig',
	# Django Filters
	'django_filters',
	# Token authentification
	#'rest_framework.authtoken',
	'djmoney',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'restful01.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'restful01.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': config('DBENGINE'),
		#'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		'NAME': config('DBNAME'),
		'USER': config('DBUSER'),
		'PASSWORD': config('DBPWD'),
		'HOST': config('DBHOST'),
		'PORT': config('DBPORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# Cors Origins

""" CORS_ALLOWED_ORIGINS = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://localhost",
] """

CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', cast=Csv())
CORS_ALLOW_CREDENTIALS = config('CSRF_ALLOW_CREDENTIALS', cast=bool)

""" CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
] """

# Pagination options

REST_FRAMEWORK = {
	#'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.LimitOffsetPagination',
	'DEFAULT_PAGINATION_CLASS': 'wprod.custompagination.LimitOffsetPaginationWithUpperBound',
	'PAGE_SIZE':1000,
	'DEFAULT_FILTER_BACKENDS': (
		'django_filters.rest_framework.DjangoFilterBackend',
		'rest_framework.filters.OrderingFilter',
		'rest_framework.filters.SearchFilter',
		),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        #'rest_framework.authentication.BasicAuthentication',
        #'rest_framework.authentication.SessionAuthentication',
        # JWT
		'rest_framework_simplejwt.authentication.JWTAuthentication',
		'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        ),
    'DEFAULT_THROTTLE_CLASSES': (
		'rest_framework.throttling.AnonRateThrottle',
		'rest_framework.throttling.UserRateThrottle',
		'rest_framework.throttling.ScopedRateThrottle',
	),
    'DEFAULT_THROTTLE_RATES': {
		'anon': '100/hour',
		'user': '5000/hour',
		'bl_entete-list': '300/hour',
		'api-root': '20/hour',
	}
}

SIMPLE_JWT = {
'ACCESS_TOKEN_LIFETIME': timedelta(days=10),
'REFRESH_TOKEN_LIFETIME': timedelta(days=20),
'ROTATE_REFRESH_TOKENS': False,
'BLACKLIST_AFTER_ROTATION': True,

'AUTH_HEADER_TYPES': ('Bearer',),
'USER_ID_FIELD': 'id',
'USER_ID_CLAIM': 'user_id',

'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
'TOKEN_TYPE_CLAIM': 'token_type',

'JTI_CLAIM': 'jti',
'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
'SLIDING_TOKEN_LIFETIME': timedelta(days=10),
'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=20),
}

