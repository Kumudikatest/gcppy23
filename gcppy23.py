import boto3
import json
cognito_idp = boto3.client("cognito-idp")

def handler(request):
    json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    print(json.dumps("\"foo\bar"))
    try:
        data = cognito_idp.list_users(
            UserPoolId="us-east-1_HdYJb7Znp",
            Limit=10
        )
        print (data)
    except BaseException as e:
        print(e)
        raise(e)
    
    return "Successfully executed"
