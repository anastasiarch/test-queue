import json
import time
from sqs_utils.sqs_client import sqs

def produce_messages(queue_url, messages):
    for message in messages:
        try:
            sqs.send_message(
                QueueUrl=queue_url,
                MessageBody=json.dumps(message)
            )
            print(f"Produced message: {message}")
        except sqs.exceptions.QueueFull:
            print(f"Error: Could not send message: {message}")
    time.sleep(1)
