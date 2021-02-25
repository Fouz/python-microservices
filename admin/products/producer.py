import pika
import json
# helps in sending events


params = pika.URLParameters(
    "amqps://hkazzjar:o0AOL8dqsCtbCfgDQLhdy78Jrrz_8nOL@hummingbird.rmq.cloudamqp.com/hkazzjar")
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange="", routing_key="main",
                          body=json.dumps(body), properties=properties)
