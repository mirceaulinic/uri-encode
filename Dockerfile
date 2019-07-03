FROM python:3.6-alpine

COPY encode.py /var/run/encode

ENTRYPOINT ["/var/run/encode"]

CMD []
