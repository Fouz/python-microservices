import pika
import json
# helps in sending events
import os


url=str(os.environ.get('RABBIT_URL'))
params = pika.URLParameters(url)

connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange="", routing_key="admin",
                          body=json.dumps(body), properties=properties)
