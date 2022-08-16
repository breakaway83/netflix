PROJ=netflix
VENV_PATH=$$HOME/.virtualenvs/${PROJ}
PYTHON=python3

all: help

help:
	@echo "setup ------------ - Set up exploit_automation project from scratch"


.PHONY: setup
setup: clean-venv requirements exploit-automation
	echo "source \"$(VENV_PATH)/bin/activate\""


.PHONY: clean-venv
clean-venv:
	rm -rf $(VENV_PATH)
	$(PYTHON) -m venv $(VENV_PATH) --clear

.PHONY: requirements
requirements:
	source "$(VENV_PATH)/bin/activate" && \
	pip install -U pip wheel && \
	pip install -r requirements.txt

.PHONY: exploit-automation
exploit-automation:
	source "$(VENV_PATH)/bin/activate" && \
	pip install --editable .