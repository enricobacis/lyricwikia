.PHONY  : all clean install test

VENV = venv

install: $(VENV)
	$(VENV)/bin/python setup.py install

all: | install test

test: install
	$(VENV)/bin/python setup.py test

clean:
	rm -rf $(VENV)

$(VENV):
	virtualenv $(VENV)
