PORT=5000


run:
	python main.py ${PORT}

test:
	curl --data "raw data" -X POST localhost:5000

clean:
	rm -f *.pyc *.pyo
