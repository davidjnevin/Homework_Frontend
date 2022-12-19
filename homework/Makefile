# target: test - Test the code
.PHONY: test
test:
	@PYTHONPATH=. pytest

# target: lint - Lint the code
.PHONY: lint
lint:
	flake8 .  && 	black . && isort .

