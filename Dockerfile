# Base image
FROM python:3.9

# Label docker image
LABEL type "fastAPI-container"

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

EXPOSE ${APP_PORT}

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]

#bug found: Error: Invalid value for '--port': '${APP_PORT}' is not a valid integer.