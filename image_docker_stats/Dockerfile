FROM python:2.7-slim

WORKDIR /monitor_services
ADD . /monitor_services
RUN pip install -r requirements.txt
CMD ["python", "docker_stats.py"]