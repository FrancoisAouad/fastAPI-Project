FROM python:alpine
RUN pip install fastapi
RUN pip install "uvicorn[standard]"
WORKDIR /usr/app/src
COPY . .
EXPOSE 8000
CMD [ "uvicorn","server:app", "--reload" ]