setup:
	pip install -r requirements.txt

PY = $(shell find code -type f -name "*.py")

lint:
	isort --check -rc code
	black --check code
	flake8 code
	mypy $(PY)

fmt format:
	isort -rc code
	black code
