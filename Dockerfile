FROM python:slim

WORKDIR /app/
ADD requirements.txt /app/

RUN pip install -r requirements.txt

ADD . /app/

CMD ["python","pick.py"]
