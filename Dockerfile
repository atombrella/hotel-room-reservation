FROM python:3.6

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

WORKDIR /usr/src/app/hotelrooms

EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "runserver"]
