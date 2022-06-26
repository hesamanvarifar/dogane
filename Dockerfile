From python:3.9

ENV PYTHONUNBUFFERED=1


COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000