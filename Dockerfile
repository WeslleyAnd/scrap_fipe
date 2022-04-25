FROM python:3
RUN pip install selenium
RUN pip install webdriver-manager
WORKDIR /app
COPY . .
ENTRYPOINT [ "python3" ]