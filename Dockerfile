FROM python:3.7.4-alpine

MAINTAINER Vishy Ganesh

#Install runtime packages
RUN apk add libxml2 libxml2-dev libxslt-dev
#install build packages
RUN apk add --no-cache --virtual .build-deps gcc musl-dev
RUN mkdir /usr/src/app

COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY servicehealth /servicehealth/
COPY servicehealth.py /
#RUN ls cd /
# clean up
RUN apk del --purge \
    .build-deps && \
 rm -rf \
    /root/.cache \
    /tmp/*
WORKDIR /

ENTRYPOINT ["python3", "./servicehealth.py"]