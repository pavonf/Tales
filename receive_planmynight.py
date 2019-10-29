import pika
import APIFunctions2
import json
import datetime

credentials = pika.PlainCredentials('gabe','gabe')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.160',5672,'/',credentials))

channel = connection.channel()

channel.queue_declare(queue='alcoholic',passive=False,durable=True)

def callback(ch, method, properties, body): 
    var = APIFunctions2.planmynight(body)
    channel.basic_publish(exchange='',
        			 routing_key='alcoholicReply',
        			 body=json.dumps(var))
    print("Message Sent")




channel.basic_consume(
	queue='alcoholic',  
    on_message_callback=callback,
    auto_ack=True)

print ( '[*] Waiting for messages. To exit press CTRL+C')



channel.start_consuming()
connection.close() 
