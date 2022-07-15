FROM python3.8-slim

WORKDIR /app
COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./config.py .
COPY ./main.py .

ENTRYPOINT ["python", "main.py"]
