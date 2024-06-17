import pika
import base64

# Se connecter au serveur RabbitMQ

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Déclarer la file d'attente

channel.queue_declare(queue='image_queue')

# Lecture de l'image

with open('image.jpeg', 'rb') as f :

     image = f.read()

image_base64 = base64.b64encode(image).decode('utf-8')

# Envoyer l'image encodee

channel.basic_publish(exchange='', routing_key='image_queue', body=image_base64)

print('Image envoyée')

# Fermer la connection

connection.close()








