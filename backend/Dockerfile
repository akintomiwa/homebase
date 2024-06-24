# backend/Dockerfile

FROM python:3.11.2

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip3 install --no-cache-dir -r requirements.txt

# COPY . /app/

ENV PYTHONPATH "${PYTHONPATH}:/app"

# Expose the Django server port
EXPOSE 80

# CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]