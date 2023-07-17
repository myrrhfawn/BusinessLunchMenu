FROM python:3.9.2


SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

RUN useradd -rms /bin/bash dm && chmod 777 /opt /run

WORKDIR /dm

RUN mkdir /dm/static && mkdir /dm/media && chown -R dm:dm /dm && chmod 755 /dm

COPY --chown=dm:dm . .

RUN pip install -r requirements.txt

USER dm

CMD gunicorn dailyMenu.wsgi:application -b 0.0.0.0:8000