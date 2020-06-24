# See:
# https://hub.docker.com/_/python
FROM python:3.8-alpine

WORKDIR /usr/src/app

# See:
# https://qiita.com/ryuichi1208/items/6020cfabc92bd8153654
# https://github.com/alpine-docker/git/issues/1
RUN apk update && apk add gcc libc-dev openssh fish git

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "bot/main.py" ]
