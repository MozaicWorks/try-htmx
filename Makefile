run:
	pipenv run flask run

.test:


test: .test
	pipenv run python -m unittest -v

unittest: .test
	pipenv run python -m unittest test/test_unit.py -v
