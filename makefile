VENV = venv

setup:
	python3 -m venv $(VENV)
	source .venv/bin/activate
	pip3 install -r requirements.txt

activate:
	source .venv/bin/activate
	
deactivate:
	deactivate

test:
	python3 -m unittest discover -s './internal'