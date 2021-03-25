import boto3
ddb = boto3.client("dynamodb")

def handler(request):
    try:
        data = ddb.put_item(
            TableName="KChineseAnimal",
            Item={
                'BirthYear': {
                    'N': "1995"
                }
            }
        )
    except BaseException as e:
        print(e)
        raise(e)
    
    return "Successfully executed"
