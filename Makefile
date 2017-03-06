VENVBIN=./venv/bin
NODEBIN=./node_modules/.bin
PYTHON=$(VENVBIN)/python
PIP=$(VENVBIN)/pip
PYTEST=$(VENVBIN)/py.test
PYLINT=$(VENVBIN)/pylint
SERVERLESS=$(NODEBIN)/serverless

.PHONY : clean

all: clean env thrift

env:
	virtualenv -p python2 venv
	npm install
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install -t vendored/ -r requirements.txt

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm -rf venv
	rm -rfv gen-py
	rm -rfv vendored

deploy:
	$(SERVERLESS) deploy

thrift: FORCE
	thrift -r --gen py service.thrift

test:
	$(PYTHON) test.py

FORCE:
