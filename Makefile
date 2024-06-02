install:
	pip install poetry && \
	poetry install

start:
	poetry run python example_bot/dop.py 
