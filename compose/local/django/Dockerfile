FROM python:3.9-alpine3.18
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app
RUN pip install --upgrade pip
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
