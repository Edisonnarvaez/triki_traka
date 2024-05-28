FROM python:3.11.9-alpine

WORKDIR /usr/src/triki_traka_backend

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONNUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/triki_traka_backend

COPY . .

ENTRYPOINT [ "./entrypoint.sh" ]