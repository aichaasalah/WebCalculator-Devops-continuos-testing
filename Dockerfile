FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pytest --maxfail=5 --disable-warnings --capture=no

EXPOSE 5000

CMD ["python", "app/main.py"]
