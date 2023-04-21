import json
from sqs_utils.sqs_client import sqs

def consume_messages(queue_url, messages):
    consumed_messages = []

    while True:
        response = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=5
        )

        if 'Messages' in response:
            for message in response['Messages']:
                consumed_messages.append(json.loads(message['Body']))
                sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=message['ReceiptHandle']
                )
                print(f"Consumed message: {json.loads(message['Body'])}")
        else:
            break

# Verify that all messages were delivered correctly
    assert len(messages) == len(consumed_messages)

    for produced, consumed in zip(messages, consumed_messages):
        assert produced == consumed

    print("All messages delivered correctly.")
