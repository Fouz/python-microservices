FROM python:3.9

RUN pip install --upgrade pip

COPY ./requirements.txt .
COPY ./entrypoint.sh /
RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

# ENV PYTHONUNBUFFERED 1
# WORKDIR /app
# COPY requirements.txt /app/requirements.txt
# RUN pip install -r requirements.txt
# COPY . /app

# FROM python:3.9
# ENV PYTHONUNBUFFERED 1

# WORKDIR  /app

# COPY requirements.txt .

# RUN pip install --upgrade pip

# RUN pip install -r requirements.txt

# COPY . /app

# COPY  entrypoint.sh .
# WORKDIR /app

# WORKDIR /app
# ENTRYPOINT ["sh", "entrypoint.sh"]
