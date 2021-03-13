FROM python:3.9

RUN pip install --upgrade pip

COPY ./requirements.txt .
COPY ./entrypoint.sh /
RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app
