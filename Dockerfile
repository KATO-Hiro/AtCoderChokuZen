# See:
# https://hub.docker.com/_/python
FROM python:3.8-alpine

WORKDIR /usr/src/app

# See:
# https://qiita.com/ryuichi1208/items/6020cfabc92bd8153654
RUN apk update && apk add fish git

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
