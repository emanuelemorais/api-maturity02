FROM python:latest

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/database

RUN python migration.py

WORKDIR /app

EXPOSE 8000

CMD ["python", "main.py"]