from sqs_utils.sqs_client import sqs

# Delete the queue
def delete_queue(queue_url, queue_name):
    sqs.delete_queue(QueueUrl=queue_url)
    print(f"Deleted queue {queue_name} with URL: {queue_url}")
