#rabbitmq part
import pika

'''
class PikaClient:

    def __init__(self, process_callable):
        self.publish_queue_name = env('PUBLISH_QUEUE', 'foo_publish_queue')
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=env('RABBIT_HOST', '127.0.0.1'))
        )
        self.channel = self.connection.channel()
        self.publish_queue = self.channel.queue_declare(queue=self.publish_queue_name)
        self.callback_queue = self.publish_queue.method.queue
        self.response = None
        self.process_callable = process_callable
        logger.info('Pika connection initialized')

    async def consume(self, loop):
        """Setup message listener with the current running loop"""
        connection = await connect_robust(host=env('RABBIT_HOST', '127.0.0.1'),
                                      port=5672,
                                      loop=loop)
        channel = await connection.channel()
        queue = await channel.declare_queue(env('CONSUME_QUEUE', 'foo_consume_queue'))
        await queue.consume(self.process_incoming_message, no_ack=False)
        logger.info('Established pika async listener')
        return connection

    async def recieve(self):
        """Processing incoming message from RabbitMQ"""
        message.ack()
        body = message.body
        logger.info('Received message')
        if body:
            self.process_callable(json.loads(body))

    def send(self, message):
        """Method to publish message to RabbitMQ"""
        self.channel.basic_publish(
            exchange='',
            routing_key=self.publish_queue_name,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=str(uuid.uuid4())
            ),
            body=json.dumps(message)
        )

'''







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

