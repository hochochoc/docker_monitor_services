import docker
import time 
import requests
import json
import os

host = os.getenv('HOST_ID', '127.0.0.1')
port = int(os.getenv('PORT', 4000))
time_post = int(os.getenv('TIME_POST', 30))
url = 'http://'+host+':'+str(port)+'/monitor/api/v1.0/stats/service'
def get_stats():
    while True:
        try:
            client = docker.DockerClient(base_url= 'unix:///var/run/docker.sock')
            for container in client.containers.list():
                labels = container.labels
                container_id = container.short_id
                stat_service = {}
                if len(labels) and 'com.docker.swarm.service.name' in labels.keys():
                    stat_gen = container.stats()
                    stat = stat_gen.next()
                    print type(stat)
                    stat = json.loads(stat)
                    stat_service['container_id'] = container_id
                    stat_service['service_name'] = labels['com.docker.swarm.service.name']
                    stat_service['service_id'] = labels['com.docker.swarm.service.id']
                    stat_service['instance_stats'] = stat
                    post = requests.post(url, json=stat_service)
                    print post.text
            time.sleep(time_post)
        except Exception as e:
            print str(e)
            pass
if __name__=='__main__':
    get_stats()