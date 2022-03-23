CREATE OR REPLACE FUNCTION add_refline() RETURNS TRIGGER AS $add_fk_to_line$
DECLARE
	new_record wprod_bl_ligne%ROWTYPE;
	bl_record wprod_bl_entete%ROWTYPE;
BEGIN
	IF (TG_OP = 'INSERT') THEN
		SELECT * INTO bl_record FROM wprod_bl_entete WHERE wprod_bl_entete."bl_num"=NEW."bli_bl_num";
		
		IF NOT FOUND THEN
			RETURN NULL;
		END IF;
		NEW."bl_entete_id":=bl_record.id;
		NEW."bli_select":=False;

		RETURN NEW;
	END IF;
	RETURN NULL;
END
$add_fk_to_line$ LANGUAGE plpgsql;

CREATE TRIGGER add_fk_to_line
BEFORE INSERT ON public.wprod_bl_ligne
	FOR EACH ROW EXECUTE FUNCTION add_refline();

