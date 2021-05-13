## A simple makefile to manage this service.

name=GeoIP
maintainer="Stefan Moller"
description="GeoIP logger"

run: 
	python main.py -run

debug:
	python main.py -run --debug

lint:
	pylint main.py app/app.py app/models.py scripts/db.py

db: 
	python scripts/db.py new

	
profile:
	python -m cProfile main.py > profile

tests:
	python test/test.py
