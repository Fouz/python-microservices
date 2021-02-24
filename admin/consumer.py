import pika
# helps in sending events


connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="admin")


def callback(channel, method, properties, body):
    print("Recieved in admin")
    print(body)


channel.basic_consume(queue="admin", on_message_callback=callback)

print("Started Consumening")

channel.start_consuming()

channel.close()
