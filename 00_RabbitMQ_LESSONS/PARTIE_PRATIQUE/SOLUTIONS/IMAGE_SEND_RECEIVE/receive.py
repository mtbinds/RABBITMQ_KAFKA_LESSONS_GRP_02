import pika
import base64
from PIL import Image
from io import BytesIO


def callback(ch, method, properties, body) :

    # Décoder l'image base64
    image_data = base64.b64decode(body)

    # Ouvrir l'image avec Pillow
    image = Image.open(BytesIO(image_data))

    # Afficher l'image
    image.show()


# Se connecter au serveur RabbitMQ 
connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel=connection.channel()

# Déclarer la file d'attente
channel.queue_declare(queue='image_queue')

# Définir la fonction du rappel
channel.basic_consume(queue='image_queue', on_message_callback=callback, auto_ack=True)

print('Attente de messages est en cours...')

# Commencer la consommation de messages
channel.start_consuming()








