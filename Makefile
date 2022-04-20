lint:
	python3 -m flake8

test:
	python3 -m unittest discover -p '*test*.py' -v

lint-fix:
	black