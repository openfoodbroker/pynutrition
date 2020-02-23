FROM python:latest
COPY . /app/

WORKDIR /app


RUN pip3 install -r requirements.txt
RUN python3 -m pytest -s tests/test_week_generator.py
