# Introduction

monitor_service server collect stats of services that are running on hosts that monitor_service agents are running on to collect stats and post stats to monitor_service server by means of api server provides

## Usage

- You can build docker image from source or use provided image 'hocx3/monitor_services:latest'. 
- You must provide environment variables for service 'web' which is used to connect mongodb, and set time interval to update data in database which is out of date for docker-stack.yml or use default config like this:
    - MONGODB_ENV_MONGODB_IP=mongodb
    - MONGODB_ENV_MONGODB_PORT=27017
    - MONGODB_DBNAME=_monitor
    - UPDATE_INTERVAL=300
- After all, you can deploy this stack to your swarm. On manager node, run:
    docker stack deploy -c docker-stack.yml <stack-name>
- Note: Mongodb mounts volume to ./data. Therefore, you have to make a directory 'mkdir ./data' at the directory you are working on. If you don't want to mount on that directory, you can replace your directory on docker-stack.yml like that '<your-dir>:/data/db
    volumes:
      - ./data:/data/db

### Example
    Use api GET by "curl" or through web browser 
    "http://$IP:$PORT/monitor/api/v1.0/stats/get_service_by_name/<service_name>"
    "http://$IP:$PORT/monitor/api/v1.0/stats/get_service_by_id/<service_id>"
    Use api POST:
    "http://$IP:$PORT/monitor/api/v1.0/stats/service"
