from google.cloud import storage


def gcs_upload(backet_name, filename, data, content_type):
    path_to_private_key = './credentials/iam-key.json'
    client = storage.Client.from_service_account_json(
        json_credentials_path=path_to_private_key)
    bucket = storage.Bucket(client, backet_name)
    blob = bucket.blob(filename)
    blob.upload_from_string(data, content_type=content_type)
    print(blob.public_url)
    # p = os.path.join(app.root_path, 'credentials/iam-key.json')
    # client = storage.Client.from_service_account_json(p)
    # bucket = client.create_bucket(backet_name)
    # return f'Bucket with name [{bucket.name}] created on GCS!'
