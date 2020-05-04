FROM python:3

WORKDIR /usr/src/pms

RUN pip install --no-cache-dir Flask
RUN pip install --no-cache-dir PyMySQL

COPY . .

CMD ["python", "server.py"]
