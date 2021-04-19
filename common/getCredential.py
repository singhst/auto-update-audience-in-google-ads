from oauth2client.service_account import ServiceAccountCredentials
from google.cloud import storage
import json

def get_credential_local(keyFileLocation, scopes = ['https://www.googleapis.com/auth/analytics.readonly']):
    """Initializes an Analytics Reporting API V4 service object.

    Returns:
        An authorized Analytics Reporting API V4 service object.
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        keyFileLocation, scopes)

    return credentials


def get_credential_cloudstorage(bucketName:str, jsonKeyName:str, scopes = ['https://www.googleapis.com/auth/analytics.readonly']):
    
    def download_gcs_file(obj, to, bucket):
        """If `to` file path is passed, save file to /tmp only as cloud functions only supports that to write to
        """
        client = storage.Client()
        bucket = client.get_bucket(bucket)
        blob = bucket.blob(obj)

        if to is None:
            # Download the contents of the blob as a string and then parse it using json.loads() method
            data = json.loads(blob.download_as_string(client=None))
            return data
        else:   # save file to /tmp only as cloud functions only supports that to write to
            blob.download_to_filename(to)
            print('downloaded file {} to {}'.format(obj, to))
    
    jsonKey = download_gcs_file(jsonKeyName, None, bucketName)
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(jsonKey, scopes)

    return credentials


def set_env_variable(KEY_FILE_LOCATION):
    """Set credential json key as GOOGLE_APPLICATION_CREDENTIALS in environment variable.
    To let local environment get credential and enough permission to get authentication to GCS.
    """
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = KEY_FILE_LOCATION


if __name__ == '__main__':    
    # === Get credential key from local environment ====================
    KEY_FILE_LOCATION = "././json_key_from_gcp.json"

    credentials_local = get_credential_local(KEY_FILE_LOCATION)
    print("> credentials_local:\t\t", credentials_local)


    # === Get credential key from GCP Google Cloud Storage ====================
    # KEY_FILE_LOCATION = 'perceptive-ivy-293901-acf003f3426d.json'
    GCS_BUCKET_NAME = 'cloud_func_auth_json'
    SERVICE_ACCOUNT_KEY_JSON = 'perceptive-ivy-293901-acf003f3426d.json'

    # Set env variable to let local environment get credential and enough permission to get authentication to GCS
    KEY_FILE_LOCATION = "././perceptive-ivy-293901-acf003f3426d.json"
    set_env_variable(KEY_FILE_LOCATION)
    print("> env parameters set")

    # Download the credential key from Cloud Storage
    credentials_cloudstorage = get_credential_cloudstorage(GCS_BUCKET_NAME, SERVICE_ACCOUNT_KEY_JSON)
    print("> credentials_cloudstorage:\t", credentials_cloudstorage)