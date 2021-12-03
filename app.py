import json


def lambda_handler(event, context):
    """ AWS Lambda Entry Point. Function takes in an event containing a body parameter with a numeric value
    and returns that numeric value's square.
    :param event: Required for Lambda, contains the trigger that cause the invocation: body parameter
    :param context: Required for Lambda, contains invocation/execution environment information
    :return: dict containing response code, and body (squared number)
    """

    value = event['body']
    squared_value = value ** 2
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "squared_value": squared_value,
            }
        ),
    }
