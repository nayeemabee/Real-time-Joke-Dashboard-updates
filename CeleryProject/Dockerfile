# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8090

# Define environment variable
ENV NAME World

# Run app.py when the container launches
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "CeleryProject.wsgi:application"]
