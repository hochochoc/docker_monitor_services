#coding: utf-8
from flask import Flask, request, jsonify, Blueprint, abort
from models import *
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" 
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

@app.route('/monitor/api/v1.0/stats/get_service_by_id/<service_id>', methods=['GET'])
def get_service_by_id(service_id):
    try:
        service_stats = Service.objects(service_id = service_id)
        print service_stats
        service_ = {}
        service_['service_id']= service_stats[0]['service_id']
        service_['service_name']= service_stats[0]['service_name']
        instances_stats = []
        for instance in service_stats:
            instance_stats   = {}
            instance_stats['created'] = instance['created']
            instance_stats['container_id'] = instance['container_id']
            instance_stats['instance_stat'] = instance['instance_stats']
            instances_stats.append(instance_stats)
        service_['instances_stats'] = instances_stats
        return jsonify({'service_stats': service_})
    except Exception as e:
        return jsonify({'results': str(e)})
    
@app.route('/monitor/api/v1.0/stats/get_service_by_name/<service_name>')
def get_service_by_name(service_name):
    try:
        service_stats = Service.objects(service_name = service_name)
        print service_stats
        service_ = {}
        service_['service_id']= service_stats[0]['service_id']
        service_['service_name']= service_stats[0]['service_name']
        instances_stats = []
        for instance in service_stats:
            instance_stats   = {}
            instance_stats['created'] = instance['created']
            instance_stats['container_id'] = instance['container_id']
            instance_stats['instance_stat'] = instance['instance_stats']
            instances_stats.append(instance_stats)
        service_['instances_stats'] = instances_stats
        return jsonify({'service_stats': service_})
    except Exception as e:
        return jsonify({'results': str(e)})

@app.route('/monitor/api/v1.0/stats/service', methods=['POST'])
def post_service_stats():
    if not request.json or not 'service_id' in request.json:
        abort(400)
    service_id = request.json['service_id']
    service_name = request.json['service_name']
    container_id = request.json['container_id']
    stats = request.json['instance_stats']
    try:
        service_stats = Service.objects(service_id=service_id, service_name=service_name, container_id=container_id).update_one(
            set__created=datetime.datetime.now,
            set__instance_stats=stats,
            upsert=True
        )
    
        print service_stats
        print type(service_stats)
        service = Service.objects(container_id=container_id)
        print service
        service = service.to_json()
        return jsonify({'service_instance_stats': service}), 201
    except Exception as e:
        return jsonify({'results': str(e)})
    # try:
        
    # except:
    #     abort(500)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
