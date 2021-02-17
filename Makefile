PYTHON=python3
ENV=env

.PHONY: env

env:
	rm -rf $(ENV)
	$(PYTHON) -m venv $(ENV)
	$(ENV)/bin/python -m pip install -r requirements.txt


