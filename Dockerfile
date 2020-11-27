FROM python:3.8

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY scripts/ .

COPY data/ .

COPY assets/ .

CMD ["python", "-m", "scripts"]

