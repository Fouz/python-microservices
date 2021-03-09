FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

COPY  entrypoint.sh /app

ENTRYPOINT ["sh", "entrypoint.sh"]

# FROM python:3.9-alpine
# ENV PYTHONUNBUFFERED 1

# COPY requirements.txt /app/requirements.txt
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# COPY . /app

# WORKDIR /app
# COPY  ./entrypoint.sh /

# ENTRYPOINT ["sh", "/entrypoing.sh"]