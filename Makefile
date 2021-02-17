PYTHON=python3
ENV=env

GETTEXT_POT=gettext-pot
GETTEXT_PO=gettext-catalogs
LANGS=es cn

.PHONY: all

env:
	rm -rf $(ENV)
	$(PYTHON) -m venv $(ENV)
	$(ENV)/bin/python -m pip install -r requirements.txt

# Generate POT file from source files
pot:
	-mkdir $(GETTEXT_POT)
	$(ENV)/bin/pybabel extract -o $(GETTEXT_POT)/template.pot src
	$(foreach lang,$(LANGS),cp $(GETTEXT_POT)/template.pot $(GETTEXT_POT)/$(lang).po;)

# Compile translated message catalog to MO
mo:
	$(foreach lang,$(LANGS),mkdir -p src/i18n/$(lang)/LC_MESSAGES;)
	$(ENV)/bin/pybabel compile --domain=AppName --locale=es --directory=src/i18n --input-file $(GETTEXT_PO)/es.po
	$(ENV)/bin/pybabel compile --domain=AppName --locale=cn --directory=src/i18n --input-file $(GETTEXT_PO)/cn.po
	find src -name "*.mo"



