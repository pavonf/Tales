import pika
import APIFunctions2
import json
import datetime

credentials = pika.PlainCredentials('gabe','gabe')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.160',5672,'/',credentials))

channel = connection.channel()

channel.queue_declare(queue='quiz',passive=False,durable=True)

def callback(ch, method, properties, body):
	args = body.split(":") 
	var = APIFunctions2.ingrediants(args[0],args[1],args[2])
	emptyStr = ''
	for word in var:
		emptyStr = emptyStr + ',' + word

	channel.basic_publish(exchange='',
        			 routing_key='alcoholicReply',
        			 body=json.dumps(emptyStr)) 
	print("Message Sent:")



channel.basic_consume(
	queue='quiz',  
    on_message_callback=callback,
    auto_ack=True)

print ( '[*] Waiting for messages. To exit press CTRL+C')



channel.start_consuming()
connection.close() 
