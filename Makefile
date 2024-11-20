requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes --with dev

install:
	pip install -r requirements.txt

test:
	pytest -v
