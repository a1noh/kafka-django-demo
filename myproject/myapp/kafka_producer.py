from confluent_kafka import Producer
from django.conf import settings

def kafka_producer(message):
    p = Producer(settings.KAFKA_SETTINGS)
    try:
        p.produce(settings.KAFKA_TOPIC, message.encode('utf-8'))
        p.flush()
    except Exception as e:
        print('Producer error: {}'.format(str(e)))
