run:
	pipenv run flask run

.test:


test: .test
	pipenv run python -m unittest
