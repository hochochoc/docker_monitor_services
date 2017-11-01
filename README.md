# Introduction

This script will provide api for:<br />
- Agents on each host to post stats of services to server which is saved in mongoDB database
- Developers who want to check the health of their services deployed in stack to get stats of services either by their names or by their id
<br />
The stats of services is saved in mongoDB database, and regularly update new stats after 30 seconds, if not updated after 5 minutes, the stats of that service will be deleted from database


## Usage

    git clone https://github.com/hochochoc/docker_stats.git your_workspace
    cd your_workspace
    
You must deploy image_monitor_service first (server), then deploy image_docker_stats
