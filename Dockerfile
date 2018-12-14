FROM python:3.7.1-alpine3.8
MAINTAINER metabol 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
