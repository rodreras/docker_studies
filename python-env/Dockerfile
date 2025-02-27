FROM python:3.10

WORKDIR /app

COPY requirements.txt .

# We run pip install outside CMD to avoid the installation every time the container starts.
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]