# Вытаскиваем базовый образ
FROM python:3.8-slim

# Устанавливаем переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Настраиваем рабочий каталог
WORKDIR /kino

# Устанавливаем зависимости

RUN pip3 install pipenv
COPY Pipfile Pipfile.lock 
RUN  pipenv install 
RUN pip3 install django

COPY . ./
