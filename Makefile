install:
	# install the dependencies
	pip install --upgrade pip &&\
	pip install -r requirements.txt
format:
	# format the code
	yapf *.py src/*.py tests/*.py
lint:
	# see flake8.ini for linting configuration
	flake8 -v *.py src/*.py tests/*.py
test:
	# see pytest.ini for test configuration
	python -m pytest tests/*.py
build:
	# build the container
	docker build -t text_temporal .
run:
	# deploy the code
	docker run \
		--rm -d -p 8010:8010 \
		--name text_temporal \
		-e CONTAINER_NAME \
		--env CONTAINER_NAME="text_temporal" \
		--env-file .env \
		# use docker volumes to persit data from multiple containers
		-v text_data_vol:/app/data \
		-v text_data_logs:/app/logs \
		image-name
deploy:
	# customise to the cloud provider
	# docker login
	# docker tag image-name svgcant2022/text_ms:text_temporal

all: install format lint test build run deploy
