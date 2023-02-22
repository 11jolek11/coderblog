FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python", "diyblog/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
