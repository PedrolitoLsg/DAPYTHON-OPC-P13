FROM python:3.9.13
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:$PORT