# pull official base image
FROM python:3.10.2-alpine

# set work directory
WORKDIR /usr/src/app

# set docker port
EXPOSE 8000

# set environment variables
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# run migrations
RUN python manage.py migrate

# start server
CMD ["uvicorn", "seed.asgi:application", "0.0.0.0:8000"]
