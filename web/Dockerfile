FROM python:latest  

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt  

COPY . ./web

EXPOSE 8000

ENV FLASK_SERVER_PORT=8000

CMD ["python", "web/app.py"]