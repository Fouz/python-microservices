import pika
# helps in sending events


connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="main")


def callback(channel, method, properties, body):
    print("Recieved in main")
    print(body)


channel.basic_consume(queue="main", on_message_callback=callback)

print("Started Consumening")

channel.start_consuming()

channel.close()
