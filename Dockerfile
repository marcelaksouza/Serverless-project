# Base image
FROM python:3.9

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

EXPOSE ${APP_PORT}

CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "5000" , "--reload"]

#Bug found: Error: Invalid value for '--port': '${APP_PORT}' is not a valid integer.