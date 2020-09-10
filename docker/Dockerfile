FROM python 3.6
RUN mkdir /src
RUN mkdir /static

WORKDIR /src
RUN apt-get update && apt-get install -y gettext libgettextpo-dev zliblg libjpeg-dev
RUN pip install --upgrate pip

COPY ./requirements.txt/scripts/
RUN pip install --no-cache-dir -r /scripts/requirements.txt

CMD ["sh","-c","python manage.py collectstatic --no-input; python manage.py migrate; python manage.py runserver 0.0.0.0:8000"]