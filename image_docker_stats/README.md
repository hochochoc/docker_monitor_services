# Introduction

monitor_service agent use Docker api to collect stats of service on the same host, and through api monitor_service server provides, it post stats on server every TIME_POST seconds

## Usage

- You can build docker image from source or use provided image 'hocx3/docker_stats:latest'. 
- You must provide environment variables for service 'agent' which is used to connect api server provides, and set time interval to post stats on server:
    environment:
        - PORT=4000
        - HOST_ID=192.168.99.100#ip address of host which server runs on
        - TIME_POST=30
- After all, you can deploy this service to your swarm. On manager node, run:
    docker stack deploy -c docker-stack.yml <stack-name>
The service will run on each host in the swarm you deploy this agent service
