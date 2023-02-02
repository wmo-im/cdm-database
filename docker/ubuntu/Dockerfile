FROM python:3.9.13-slim

ENV TZ="Etc/UTC" \
    DEBIAN_FRONTEND="noninteractive" \
    DEBIAN_PACKAGES="cron bash vim git libffi-dev python3-cryptography libssl-dev libudunits2-0 python3-paho-mqtt python3-dateparser python3-tz python3-setuptools"

ADD ./docker/ubuntu/requirements.txt requirements.txt

RUN echo "Acquire::Check-Valid-Until \"false\";\nAcquire::Check-Date \"false\";" | cat > /etc/apt/apt.conf.d/10no--check-valid-until \
    && apt-get update -y \
    && apt-get install -y ${DEBIAN_PACKAGES} \
    && apt-get install -y python3 python3-pip libpq-dev \
    && pip3 install -r requirements.txt \
    && pip3 install --no-cache-dir https://github.com/opencdms/pyopencdms/archive/dib_testing.zip




