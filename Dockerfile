#
FROM python:3.10

#
WORKDIR /code

ENV DJANGO_SETTINGS_MODULE=seed.settings
#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY . /code/

RUN python manage.py migrate

EXPOSE 8000

CMD ["uvicorn", "seed.asgi:application"]
