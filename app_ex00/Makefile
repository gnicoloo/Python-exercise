.PHONY: all install run clean

PYTHON = python3
VENV = venv
APP = main.py
VENV_PYTHON = $(VENV)/bin/python

all: install run

$(VENV)/bin/activate:
	$(PYTHON) -m venv $(VENV)

install: $(VENV)/bin/activate
	$(VENV_PYTHON) -m pip install --upgrade pip
	$(VENV_PYTHON) -m pip install -r requirements.txt

run:
	$(VENV_PYTHON) $(APP)

clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -r {} +
