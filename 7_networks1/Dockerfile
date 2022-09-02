FROM python:alpine3.10

WORKDIR /app

COPY . /app

RUN python -m pip install --upgrade pip \
    && pip install requests 

CMD [ "python", "main.py" ]