FROM python:3
WORKDIR /usr/src/app
COPY . .
CMD ["consulta.py"]
ENTRYPOINT [ "python3" ]