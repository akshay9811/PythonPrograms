FROM python:3.7 AS builder
WORKDIR /app
COPY . .
RUN pip install flask
#---------------------------------------
# Stage 2
FROM python:3.7-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.7/site-packages/ /usr/local/lib/python3.7/site-packages/
COPY . .
CMD ["python3","app.py"]
