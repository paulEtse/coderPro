lint:
	flake8

test:
	python -m unittest discover -p '*test*.py' -v

lint-fix:
	black