

all: install format test run


install:
	poetry install

format:
	poetry run black src/

test:
	poetry run pytest --doctest-modules -vvvv

run:
	cd src/aoc2020; poetry run python 1.py
	cd src/aoc2020; poetry run python 2.py
	cd src/aoc2020; poetry run python 3.py
