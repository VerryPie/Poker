import pika
import logging
import functools

logging.basicConfig(level=logging.INFO)

def on_message(chan, method_frame, header_frame, body, userdata=None):
    print(userdata)
    print(body)
    chan.basic_ack(delivery_tag=method_frame.delivery_tag)

if __name__ == '__main__':
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(
        exchange="test_exchange",
        exchange_type = "direct",
        passive=False,
        durable=True,
        auto_delete=False)

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange='logs', queue=queue_name)


    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(" [x] %r" % body)

    on_message_callback = functools.partial(
        on_message, userdata='on_message_userdata')
    channel.basic_consume('standard', on_message_callback)
    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

