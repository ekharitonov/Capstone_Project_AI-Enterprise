FROM python:3.8.5
RUN apt-get update && apt-get install -y
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD [ "python", "./run_app.py" ]
