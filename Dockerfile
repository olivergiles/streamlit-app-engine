FROM python:3.8.13-slim-bullseye

WORKDIR /app

COPY ./ ./

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
