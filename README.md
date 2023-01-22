[![Makefile CI process for Github](https://github.com/ant358/ml-ops-template/actions/workflows/devops-github.yml/badge.svg)](https://github.com/ant358/ml-ops-template/actions/workflows/devops-github.yml)

# ml-ops-template

This is a template for a machine learning project.  It is designed to be used with a CI process to automate the testing and deployment of the project. It will be a base for NLP based projects deployed to a container microservice.

The template was built using the following steps:
## First build out the project 
Create the files and folders you need for your project.  This includes the following:
Makefile
Dockerfile
requirements.txt
main.py
src/
    __init__.py
    train.py
    predict.py
    test.py
data/
notebooks/
models/
tests/
docs/
README.md

## Create a virtual environment
python3 -m venv venv
activate the virtual environment
source venv/bin/activate or on windows venv\Scripts\activate

## Install the requirements
The first time you run the requirements it is worth removing the pinned version numbers so the best version for the python version is installed.  Once you have the project running you can pin the versions, with pip freeze > requirements.txt
pip install -r requirements.txt
or make install

## Start the CI process  
Push the changes so far to github or gitlab
Then check that the requirements are installed correctly in the first stage of the CI process.
Check the first step of the CI process is successful, (add the badge to the readme file.)
Then add the formating and linting steps to the CI process.
Test that they are working and detecting errors.

## Add some tests and test coverage stats
Add some tests to the tests folder and run the tests with pytest
Fail some tests to check the CI process fails
add a pytest.ini file to the root of the project
add a __init__.py file to the tests folder

## Build the docker image
write the dockerfile and 
add a docker build step to the CI process

## run the docker image
add a docker run step to the CI process

## Run the docker image locally
Check that you can connect to the API at http://localhost:8000/docs or the endpoints directly from a terminal using curl http://localhost:8000/get_random_wiki_page 

## setup the environment variables
add any the environment variables to the .env file
if passwords are added to the .env file make sure to 
add the .env file to the .gitignore file as it contains sensitive information
that should not be pushed to github or gitlab. However at the moment it is used
to transfer the container name from docker run to the python logger.
create a container name to use when running the docker image as part of a network
so that it can be identified in the logs  

## As the template is converted to each project  
Write more tests

