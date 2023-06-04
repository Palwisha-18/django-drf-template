FROM python:3.8
RUN apt-get update -qq && apt-get install -y -qq \
    gdal-bin binutils libproj-dev libgdal-dev cmake &&\
    apt-get clean all &&\
    rm -rf /var/apt/lists/* &&\
    rm -rf /var/cache/apt/*
ENV PYTHONUNBUFFERED 1
WORKDIR /django_project
COPY . /django_project
RUN pip install -r requirements.txt
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh