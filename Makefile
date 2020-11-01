.PHONY: install build-requirements flake8

.PHONY: build
build:
	docker build -t app .

# Launch this to ...install ?
.PHONY: install
install:
	pip install -Ur requirements.txt

# Use flake8 image instead of building the app to do a lint
.PHONY: lint
lint:
	docker run -ti --rm -v $$(pwd):/apps alpine/flake8:3.5.0 -v *.py

# Launch this to launch unit test
.PHONY: unit-test
unit-test: build
	docker run -t --rm app python3.9 -m unittest tests/unit-test.py

# Launch this command to show result for test
.PHONY: launch_for_test
launch_for_test: build
	docker run -t --rm app python3.9 launch_for_test.py

.PHONY: launch web interface
launch-web:
	 docker-compose build web && docker-compose up web
