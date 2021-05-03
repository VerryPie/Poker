import pika
import sys
import secrets

if __name__ == '__main__':
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='lobby', exchange_type='fanout')
    token = secrets.token_hex()
    message = ' '.join(secrets.token_hex())
    channel.basic_publish(exchange='logs', routing_key='', body=message)