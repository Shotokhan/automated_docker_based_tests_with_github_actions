FROM python:3.9

WORKDIR /usr/src/app

RUN apt-get update -y

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE=true

COPY src src
WORKDIR /usr/src/app/src
RUN chmod +x ./start_test.sh

# CMD ["pytest", "test.py"]
CMD [ "./start_test.sh" ]

