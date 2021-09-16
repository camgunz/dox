.PHONY: test install help

help:
	@echo "Commands: install"

venv:
ifeq ($(VIRTUAL_ENV), )
	$(error "Not running in a virtualenv")
endif

install: venv
	@python setup.py install
