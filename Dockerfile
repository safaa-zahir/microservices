FROM python:3.9-slim
WORKDIR /microservice
COPY . /microservice
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python3","product-service.py"]
