import logging

import azure.functions as func

from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient


def main(req: func.HttpRequest) -> func.HttpResponse:

    # display secret Kkey from Azure vault

    logging.info('Python HTTP trigger function processed a request.')
    secretname = req.params.get('secretname')
    if not secretname:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            secretname = req_body.get('secretname')

    if secretname:

        if secretname == "secret1":
            secret1, name1, date1 = getsecretkey1()
            return func.HttpResponse(f"Name1: {name1} secret1: {secret1} creation date: {date1}")
        elif secretname == "secret2":
            secret2, name2, date2 = getsecretkey2()
            return func.HttpResponse(f"Name2: {name2} secret2: {secret2} creation date: {date2}")
        elif secretname == "secret3":
            secret3, name3, date3 = getsecretkey3()
            return func.HttpResponse(f"Name3: {name3} secret3: {secret3} creation date: {date3}")
        else:
            return func.HttpResponse(f"No secret for you!", status_code=400)

    else:
        # return all secrets data

        secret1, name1, date1 = getsecretkey1()
        secret2, name2, date2 = getsecretkey2()
        secret3, name3, date3 = getsecretkey3()

        return func.HttpResponse(

            body=f" Name1: {name1} secret1: {secret1} creation date: {date1} \n Name2: {name2} secret2: {secret2} creation date: {date2} \n Name3: {name3} secret3: {secret3} creation date: {date3}",


            status_code=400
        )

#################


TENANT_ID = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
CLIENT_ID = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
CLIENT_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


########################################

def getsecretkey1():

    keyVault1_name = 'VaronisAssignmentKv1'
    KeyVault_URI = f"https://{keyVault1_name}.vault.azure.net/"

    SECRET_NAME = 'VaronisAssignmentSecret'

    _credential = ClientSecretCredential(
        tenant_id=TENANT_ID,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )

    _sc = SecretClient(vault_url=KeyVault_URI, credential=_credential)
    KVA_SECRET = _sc.get_secret(SECRET_NAME).value

    # print(dir(_sc.get_secret(SECRET_NAME).properties.created_on))
    KVA_DATE = _sc.get_secret(SECRET_NAME).properties.created_on

    return KVA_SECRET, SECRET_NAME, KVA_DATE


#################################################


def getsecretkey2():

    keyVault2_name = 'VaronisAssignmentKv2'
    KeyVault_URI = f"https://{keyVault2_name}.vault.azure.net/"

    SECRET_NAME = 'VaronisAssignmentSecret'

    _credential = ClientSecretCredential(
        tenant_id=TENANT_ID,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )

    _sc = SecretClient(vault_url=KeyVault_URI, credential=_credential)
    KVA_SECRET = _sc.get_secret(SECRET_NAME).value
    KVA_DATE = _sc.get_secret(SECRET_NAME).properties.created_on

    return KVA_SECRET, SECRET_NAME, KVA_DATE


##############################

def getsecretkey3():

    keyVault3_name = 'VaronisAssignmentKv3'
    KeyVault_URI = f"https://{keyVault3_name}.vault.azure.net/"

    SECRET_NAME = 'VaronisAssignmentSecret'

    _credential = ClientSecretCredential(
        tenant_id=TENANT_ID,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )

    _sc = SecretClient(vault_url=KeyVault_URI, credential=_credential)
    KVA_SECRET = _sc.get_secret(SECRET_NAME).value
    KVA_DATE = _sc.get_secret(SECRET_NAME).properties.created_on

    return KVA_SECRET, SECRET_NAME, KVA_DATE
