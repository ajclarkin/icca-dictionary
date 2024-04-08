FROM python:3.12-alpine

RUN pip3 install flask

RUN pip3 install flask_cors

RUN pip3 install gunicorn

WORKDIR /flask

ENTRYPOINT ["./gunicorn.sh"]
