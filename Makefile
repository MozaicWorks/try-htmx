run:
	python -m flask run

.test:


test: .test
	pipenv run python test/tests.py
