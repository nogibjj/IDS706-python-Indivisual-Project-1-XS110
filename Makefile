install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black scripts/*.py

lint:
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py
	ruff check scripts/*.py

test:
	python -m pytest -vv --cov=scripts scripts/test_*.py
	pytest --nbval individual_project.ipynb

deploy:
	#deploy goes here
		
all: install lint deploy format test 