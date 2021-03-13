import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product
# helps in sending events

url=str(os.environ.get('RABBIT_URL'))
params = pika.URLParameters(url)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="admin")


def callback(channel, method, properties, body):
    print("Recieved in admin")
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print("Products likes increased")


channel.basic_consume(
    queue="admin", on_message_callback=callback, auto_ack=True)

print("Started Consumening")

channel.start_consuming()

channel.close()

