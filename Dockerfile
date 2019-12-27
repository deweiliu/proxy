# reference https://github.com/darkmavis1980/flask-python-3-docker
FROM python:3.7

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN pytest
CMD [ "python", "./run.py" ]