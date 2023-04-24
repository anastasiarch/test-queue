
# Stream processing test

This project demonstrates how to use AWS Simple Queue Service (SQS) to produce and consume messages, using the Boto3 Python library and can be tested against a local SQS endpoint using Localstack.


These functions can be imported and used in other Python projects that require SQS functionality, making it easier to build scalable and distributed systems.


## Prerequisite

Here are the prerequisites to run this project:

```bash
    # Python 3 
    # An AWS account with access to create and delete SQS queues and send and receive messages.
    # Docker
    # Localstack
```
    
## Installation

The required packages to run this project can be easily installed

```bash
  pip install -r requirements.txt
```


## Files and Functions

- **main.py** This is the main script that runs the example scenario. It imports the necessary functions from the other modules and executes them in the correct order.
- **sqs_utils/sqs_client.py** This module contains the **get_sqs_client()** function, which creates an SQS client using the boto3 library. This function takes an optional endpoint_url parameter, which is used to specify the URL of the local SQS endpoint when running the application with Localstack.
- **sqs_utils/create_queue.py** This module contains the **create_queue(queue_name)** function, which creates a new SQS queue with the specified name and returns the queue URL.
- **sqs_utils/delete_queue.py** This module contains the **delete_queue(queue_url, queue_name)** function, which deletes an existing SQS queue with the specified URL and name.
- **sqs_utils/produce_messages.py** This module contains the produce_messages(queue_url, messages) function, which sends a list of messages to an SQS queue with the specified URL.
- **sqs_utils/consume_messages.py** This module contains the consume_messages(queue_url, expected_messages) function, which retrieves messages from an SQS queue with the specified URL and compares them to the expected messages passed as an argument. If all messages are successfully retrieved and match the expected messages, the function returns **True**.
- **test_data/cars.json** contains a collection of JSON files. These files can be used to verify that the functions correctly produce and consume messages from an SQS queue.


## Running Tests

To run test, run the following command

```bash
  python main.py
```



## Demo Scenario

1. Scenario: Messages are consumed successfully
* Produce a few messages on queue with cars details. Message should contain details on a car as follows:
```bash
       - Brand name
       - Model
       - Number of Doors
       - Indicating whether it is a Sports car or not
```

* Consume previously produced messages from queue with cars details.
* Compare the produced and consumed messages to verify that all messages were delivered correctly.

## Output log

The output log displays the following information:

- The created queue name and URL
- The produced messages
- The consumed messages
- A message indicating whether all messages were delivered correctly or not
- The deleted queue name and URL

```javascript
Created queue cars with URL: http://localhost:4566/000000000000/cars
Produced message: {'brand': 'Toyota', 'model': 'Corolla', 'doors': 4, 'sports_car': False}
Produced message: {'brand': 'Ford', 'model': 'Mustang', 'doors': 2, 'sports_car': True}
Produced message: {'brand': 'Tesla', 'model': 'Model S', 'doors': 4, 'sports_car': True}
Consumed message: {'brand': 'Toyota', 'model': 'Corolla', 'doors': 4, 'sports_car': False}
Consumed message: {'brand': 'Ford', 'model': 'Mustang', 'doors': 2, 'sports_car': True}
Consumed message: {'brand': 'Tesla', 'model': 'Model S', 'doors': 4, 'sports_car': True}
All messages delivered correctly.
Deleted queue cars with URL: http://localhost:4566/000000000000/cars
```


## Author

- [@anastasiarch](https://github.com/anastasiarch/)



