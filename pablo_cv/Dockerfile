FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


ADD manage.py .

WORKDIR /app

COPY requirements.txt /app/
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apk del .build-deps
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --no-input

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pablo_cv.wsgi:application"]
