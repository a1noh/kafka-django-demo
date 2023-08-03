from confluent_kafka import Consumer
from django.conf import settings

def kafka_consumer():
    c = Consumer(settings.KAFKA_SETTINGS)
    c.subscribe([settings.KAFKA_TOPIC])
    try:
        while True:
            msg = c.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print("Consumer error: {}".format(msg.error()))
                continue
            print('Received message: {}'.format(msg.value().decode('utf-8')))
    except KeyboardInterrupt:
        c.close()
