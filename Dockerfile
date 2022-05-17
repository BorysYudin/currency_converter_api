FROM python:3.7-alpine

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "src:create_app()"]
