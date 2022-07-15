FROM python:3.8-slim-bullseye

WORKDIR /app
COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./config.py .
COPY ./main.py .

ENTRYPOINT ["python", "main.py"]
