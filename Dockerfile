FROM python:3.9
WORKDIR /usr/src/hello-world
COPY . . 
CMD ["python", "hello.py"]