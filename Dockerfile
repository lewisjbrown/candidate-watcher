FROM python:alpine3.8
WORKDIR /app/
RUN apk update
COPY ./requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY . /app/
ENTRYPOINT ["python", "candidate_watcher/main.py"]
