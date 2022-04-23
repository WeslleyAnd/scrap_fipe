FROM python:3
RUN pip install beautifulsoup4 
RUN pip install requests
WORKDIR /usr/src/app
COPY . .
CMD ["pip install beautifulsoup4", "consulta.py"]
ENTRYPOINT [ "python3" ]