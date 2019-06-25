FROM python:3 
COPY . /app
WORKDIR /app 
RUN pip install -r requirements.txt
EXPOSE 80
ENV NAME World
CMD ["python", "server.py"]

