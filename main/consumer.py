import pika
# helps in sending events
import json
from main import create_app, APP
from models import Product, db


connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="main")


def callback(channel, method, properties, body):
    print("Recieved in main")
    data = json.loads(body)
    # print(data)

    if properties.content_type == "product_created":
        # print("{} 000 {} 000 {}", data["id"], data["title"], data["image"])
        product = Product(data["id"], data["title"], data["image"])
        app = create_app()
        with app.app_context():
            db.session.add(product)
            db.session.commit()

    elif properties.content_type == "product_updated":
        app = create_app()
        with app.app_context():
            product = Product.query.get(data["id"])
            product.title = data["title"]
            product.image = data["image"]
            db.session.commit()
            db.session.close()
            print("Product Updated")

    elif properties.content_type == "product_deleted":
        app = create_app()
        with app.app_context():
            product = Product.query.get(data["id"])
            db.session.delete(product)
            db.session.commit()
            db.session.close()
            print("Product Deleted")
    print("done")


channel.basic_consume(
    queue="main", on_message_callback=callback, auto_ack=True)

print("Started Consumening")

channel.start_consuming()

channel.close()
