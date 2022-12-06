#rabbitmq part
import pika

def send(obj):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='requests')

    channel.basic_publish(exchange='',
                      routing_key='requests',
                      body=obj)
    print ("Request sent")
    connection.close()

def receive():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='requests')

    def callback(ch, method, properties, body):
        print ("Request received")

        channel.basic_consume(callback,
                              queue='requests',
                              no_ack=True)

        channel.start_consuming()


def consume(loop):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='localhost'))
    channel = connection.channel()
    channel.declare_queue(queue='requests')
    queue.consume(self.process_incoming_message, no_ack=False)
    print('Established pika async listener')
    return connection

