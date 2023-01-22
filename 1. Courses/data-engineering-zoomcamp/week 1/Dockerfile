FROM python:3.9.1

RUN pip install pandas sqlalchemy psycopg2 wget

WORKDIR /app
COPY postgres.py postgres.py 

ENTRYPOINT [ "python", "postgres.py" ]