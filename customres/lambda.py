####
# Get the parameter from the CFN template and checks if it exists in the Parameter store.
# If so, it returns the parameter value to the CFN template,
# otherwise an errore message is returned.
####
import json
import uuid
import requests
import boto3

def get_cfn_secret(event, context):
    """
    Lambda main function
    """
    res_props = event['ResourceProperties']
    if not 'Name' in res_props or not 'Region' in res_props:
        __send_response(
            "FAILED",
            "Name or Region property missing",
            event
            )
        return
    if not res_props['Name'] or not res_props['Region']:
        __send_response(
            "FAILED",
            "Name or Region property empty",
            event
            )

    req_param = res_props['Name']
    region = res_props['Region']

    ssm = boto3.client('ssm', region_name=region)
    # get parameter from Stored parameter
    response = ssm.get_parameters(
        Names=[
            req_param
        ],
        WithDecryption=True
    )

    if response['InvalidParameters']:
        __send_response(
            "FAILED",
            "Parameter doesn't exist",
            event
            )
    else:
        __send_response(
            "SUCCESS",
            "Parameter retrieves successfully",
            event,
            response['Parameters'][0]['Value']
            )


def __send_response(status, reason, event, secret=None):
    """
    Create response and send to the pre-signed url provided by
    CloudFormation
    """
    body_resp = {
        "Status":status,
        "Reason":reason,
        "StackId":event['StackId'],
        "RequestId":event['RequestId'],
        "PhysicalResourceId":str(uuid.uuid4()),
        "LogicalResourceId":event['LogicalResourceId'],
        "Data":{}
    }
    if status == 'SUCCESS':
        body_resp['Data']['Secret'] = secret

    requests.put(event['ResponseURL'], data=json.dumps(body_resp), headers={'content-type':""})
