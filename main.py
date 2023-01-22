# note does not run in jupyter notebook, run in the terminal
from fastapi import FastAPI
import uvicorn
import logging
import os
import pathlib
from datetime import datetime
from src.input_data import get_wiki_page, get_random_wiki_page
from src.control import Job_list

# setup logging
# get todays date
datestamp = datetime.now().strftime('%Y%m%d')
container_name = os.getenv('CONTAINER_NAME')
# append date to logfile name
log_name = f'log-{container_name}-{datestamp}.txt'
path = os.path.abspath('./logs/')
# add path to log_name to create a pathlib object
# required for loggin on windows and linux
log_filename = pathlib.Path(path, log_name)

# create log file if it does not exist
if os.path.exists(log_filename) is not True:
    # create the logs folder if it does not exist
    if os.path.exists(path) is not True:
        os.mkdir(path)
    # create the log file
    open(log_filename, 'w').close()

# create logger
logger = logging.getLogger()
# set minimum output level
logger.setLevel(logging.DEBUG)
# Set up the file handler
file_logger = logging.FileHandler(log_filename)

# create console handler and set level to debug
ch = logging.StreamHandler()
# set minimum output level
ch.setLevel(logging.INFO)
# create formatter
formatter = logging.Formatter('[%(levelname)s] -'
                              ' %(asctime)s - '
                              '%(name)s : %(message)s')
# add formatter
file_logger.setFormatter(formatter)
ch.setFormatter(formatter)
# add a handler to logger
logger.addHandler(file_logger)
logger.addHandler(ch)
# mark the run
logger.info(f'Lets get started! - logginng in "{log_filename}" today')

# create the FastAPI app
app = FastAPI()

# create the job list
jobs = Job_list()


# OUTPUT- routes
@app.get("/")
async def root():
    logging.info("Root requested")
    return {"message": "Template ML API to work with text data"}


@app.get("/wiki_page/{page_name}")
async def wiki_page(page_name: str):
    """Get the text content of a Wikipedia page"""
    logging.info(f"Page {page_name} requested")
    result = get_wiki_page(page_name)
    return {"title": page_name, "content": result}


@app.get("/random_wiki_page")
async def random_wiki_page():
    """Get a random Wikipedia page summary"""
    page_title = get_random_wiki_page()[0]
    result = get_wiki_page(page_title)
    logging.info(f"Random page {page_title} requested")
    return {"title": page_title, "content": result}


@app.get("/get_current_jobs")
async def get_current_jobs():
    """Get the current jobs"""
    logging.info("Current jobs list requested")
    return {"Current jobs": jobs.jobs}


# INPUT routes
@app.post("/add_job/{job}")
async def add_job(job: str):
    """Add a job to the list of jobs"""
    jobs.add(job)
    logging.info(f"Job {job} added")
    return {"message": f"Job {job} added"}


@app.post("/remove_job/{job}")
async def remove_job(job: str):
    """Remove a job from the list of jobs"""
    jobs.remove(job)
    logging.info(f"Job {job} removed")
    return {"message": f"Job {job} removed"}


if __name__ == "__main__":
    # goto localhost:8080/
    # or localhost:8080/docs for the interactive docs
    uvicorn.run(app, port=8080, host="0.0.0.0")
