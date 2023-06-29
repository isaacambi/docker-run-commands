se image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the source code into the container
COPY app.py /app

# Install dependencies
RUN pip install flask mysql-connector-python

# Expose the port on which the application will run
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]

