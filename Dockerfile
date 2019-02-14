FROM python:3.6-slim-stretch

RUN apt update
RUN apt install -y python3-dev gcc

ADD requirements/production.txt production.txt

RUN pip install -r production.txt

ADD main.py main.py
ADD templates templates
ADD export.pkl export.pkl

# Run it once to trigger resnet download
RUN python main.py

# Start the server
CMD ["python", "main.py", "production"]
