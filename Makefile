MODULE := magic
BLUE=\033[0;34m
NC=\033[0m

venv:
	. ./venv/bin/activate

install:
	python3 -m venv venv
	. ./venv/bin/activate
	python3 -m pip install -r requirements.txt

test:
	@pytest

lint:
	@echo "${BLUE}Running isort against source and test files...${NC}"
	@-isort .
	@echo "\n${BLUE}Running Black against source and test files...${NC}"
	@-black .
	@echo "\n${BLUE}Running Flake8 against source and test files...${NC}"
	@-flake8 .

clean:
	rm -rf .pytest_cache .coverage .pytest_cache coverage.xml

delete_venv:
	rm -rf venv

.PHONY: clean test