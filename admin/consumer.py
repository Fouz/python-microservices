import pika
# helps in sending events


params = pika.URLParameters(
    "amqps://hkazzjar:o0AOL8dqsCtbCfgDQLhdy78Jrrz_8nOL@hummingbird.rmq.cloudamqp.com/hkazzjar")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="admin")


def callback(channel, method, properties, body):
    print("Recieved in admin")
    print(body)


channel.basic_consume(
    queue="admin", on_message_callback=callback, auto_ack=True)

print("Started Consumening")

channel.start_consuming()

channel.close()
