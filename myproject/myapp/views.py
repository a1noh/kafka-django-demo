from django.http import HttpResponse

from . import kafka_consumer
from . import kafka_producer

def home_view(request):
    # View for the homepage
    return HttpResponse("Welcome to the Home Page!")


def send_message(request):
    message = "Hello, Kafka!"
    kafka_producer.kafka_producer(message)
    return HttpResponse("Message sent to Kafka topic.")

def receive_message(request):
    kafka_consumer.kafka_consumer()
    return HttpResponse("Consuming messages from Kafka topic.") # it will not reach here because this is a loop