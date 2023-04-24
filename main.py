#!/usr/bin/env python

import json
from sqs_utils.sqs_client import sqs
from sqs_utils.create_queue import create_queue
from sqs_utils.delete_queue import delete_queue
from sqs_utils.produce_messages import produce_messages
from sqs_utils.consume_messages import consume_messages

try:
    with open('test_data/cars.json') as f:
        car_messages = json.load(f)

    queue_name = 'cars'
    queue_url = create_queue(queue_name)

    produce_messages(queue_url, car_messages)
    consume_messages(queue_url, car_messages)
    delete_queue(queue_url, queue_name)
    
except Exception as e:
    print(f"An error occurred: {e}")
