FROM python:3.9-slim

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app
COPY data /app/data
COPY .streamlit /app/.streamlit

CMD ["streamlit", "run", "main.py"]
