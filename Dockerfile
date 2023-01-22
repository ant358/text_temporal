FROM python:3.9-slim-bullseye
# Set the environment variables
ENV APP_HOME=/app
# Set the working directory
WORKDIR $APP_HOME
# Copy the requirements file
COPY requirements-docker.txt .
# Install the Python requirements
RUN pip install -r requirements-docker.txt
# Copy the source code - see dockerignore
COPY . /app
# expose the port
EXPOSE 8080
# Entrypoint
ENTRYPOINT ["python"]
# Run bash
CMD ["main.py"]