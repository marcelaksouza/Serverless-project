FROM python:3.9

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /server

COPY requirements.txt /server/requirements.txt

RUN pip install -r /server/requirements.txt

COPY . /server

EXPOSE ${SERVER_PORT}

CMD ["uvicorn", "server.main:server", "--host", "0.0.0.0", "--port", "5000" , "--reload"]

#Bug found: Error: Invalid value for '--port': '${APP_PORT}' is not a valid integer.