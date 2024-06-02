install:
	pip install poetry && \
	poetry install
        poetry shell
        poetry add requests

start:
	poetry run python example_bot/dop.py 
