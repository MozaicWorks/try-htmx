run:
	pipenv run python -m flask run

.test:


test: .test
	pipenv run python -m unittest
