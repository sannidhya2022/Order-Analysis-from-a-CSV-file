FROM python:3.8-slim

# Setting the working directory
WORKDIR /app

# Copying the current directory contents into the container at /app
COPY . /app

# Installing any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Runing task.py when the container launches
CMD ["python", "task.py"]
