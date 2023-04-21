from sqs_utils.sqs_client import sqs
from sqs_utils.create_queue import create_queue
from sqs_utils.delete_queue import delete_queue
from sqs_utils.produce_messages import produce_messages
from sqs_utils.consume_messages import consume_messages

messages = [
    {
        'brand': 'Toyota',
        'model': 'Corolla',
        'doors': 4,
        'sports_car': False
    },
    {
        'brand': 'Ford',
        'model': 'Mustang',
        'doors': 2,
        'sports_car': True
    },
    {
        'brand': 'Tesla',
        'model': 'Model S',
        'doors': 4,
        'sports_car': True
    }
]

queue_name = 'cars'

queue_url = create_queue(queue_name)

produce_messages(queue_url, messages)

consume_messages(queue_url, messages)

delete_queue(queue_url, queue_name)
