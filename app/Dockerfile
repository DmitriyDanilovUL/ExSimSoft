FROM python:3.8

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN useradd -rms /bin/bash worker && chmod 777 /opt 

WORKDIR /app

RUN mkdir /app/base && mkdir /app/media && chown -R worker:worker /app && chmod 755 /app

COPY --chown=worker:worker . /app

RUN pip --no-cache-dir install --upgrade pip==23.1.2 | pip install --no-cache-dir -r requirements.txt

USER worker

#CMD ["gunicorn","-b","0.0.0.0:8000","main.wsgi:application"]
