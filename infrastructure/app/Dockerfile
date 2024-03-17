FROM python:3-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt

# add the following
WORKDIR /app/project
EXPOSE 8000
CMD python3 ./manage.py runserver 0.0.0.0:8000