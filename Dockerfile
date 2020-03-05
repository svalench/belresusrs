FROM python:3.7.4
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requiremens.txt /code/
RUN pip install --upgrade -r requiremens.txt
COPY . .