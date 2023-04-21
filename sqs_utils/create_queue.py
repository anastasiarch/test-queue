from sqs_utils.sqs_client import sqs

# Create an SQS queue
def create_queue(queue_name):
    response = sqs.create_queue(QueueName=queue_name)
    queue_url = response['QueueUrl']
    print(f"Created queue {queue_name} with URL: {queue_url}")
    return queue_url
