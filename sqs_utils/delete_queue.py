from sqs_utils.sqs_client import sqs

# Delete the queue
def delete_queue(queue_url, queue_name):
    try:
        sqs.delete_queue(QueueUrl=queue_url)
        print(f"Deleted queue {queue_name} with URL: {queue_url}")
    except sqs.exceptions.QueueDoesNotExist:
        print(f"Queue {queue_name} with URL {queue_url} not found.")
