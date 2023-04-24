from sqs_utils.sqs_client import sqs

# Create an SQS queue
def create_queue(queue_name):
    try:
        response = sqs.create_queue(QueueName=queue_name)
    except sqs.exceptions.QueueNameExists:
        print(f"Queue {queue_name} already exists.")
        response = sqs.get_queue_url(QueueName=queue_name)
    queue_url = response['QueueUrl']
    print(f"Created queue {queue_name} with URL: {queue_url}")
    return queue_url
