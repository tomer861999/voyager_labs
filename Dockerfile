FROM python:3.8-slim-buster
WORKDIR .
RUN mkdir /app
COPY . /app
RUN pip3 install -r /app/requirements.txt
CMD ["python3","/app/web_up_check.py"]