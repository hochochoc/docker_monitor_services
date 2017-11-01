from mongoengine import *
import datetime
import os

mongodb_ip = os.getenv("MONGODB_ENV_MONGODB_IP", "127.0.0.1")
mongodb_port = int(os.getenv("MONGODB_ENV_MONGODB_PORT", 27017))
mongodb_name = os.getenv("MONGODB_ENV_DBNAME", "monitor_")
update_interval = int(os.getenv("UPDATE_INTERVAL", 300))
connect(mongodb_name, host='mongodb://'+mongodb_ip+':'+str(mongodb_port)+'/'+mongodb_name)
class Service(Document):
    service_id = StringField(required=True)
    service_name = StringField(required=True)
    container_id = StringField(required=True)
    instance_stats = DictField()
    created = DateTimeField(required=True, default=datetime.datetime.now)
    meta = {
        'indexes': [
            {
                'fields': ['created'],
                'expireAfterSeconds': update_interval
                #automatically delete document from db after 5 min
            }
        ]
    }