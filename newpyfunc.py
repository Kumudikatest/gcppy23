import boto3
ddb = boto3.client("dynamodb")

def handler(request):
    try:
        data = ddb.put_item(
            TableName="KChineseAnimal",
            Item={
                'BirthYear': {
                    'S': "1994"
                }
            }
        )
    except BaseException as e:
        print(e)
        raise(e)
    
    return "Successfully executed"
