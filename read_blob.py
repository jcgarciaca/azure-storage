import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    # Quick start code goes here
    connect_str = "SharedAccessSignature=sv=2020-02-10&ss=bf&srt=sco&sp=rwdlacx&se=2022-03-01T22:08:42Z&st=2021-02-17T14:08:42Z&spr=https&sig=GOb0Izl8ihrSSN%2F8GpJ0USclvmLNqnbAdFAXfcpsYZk%3D;BlobEndpoint=https://datalakegs.blob.core.windows.net/;FileEndpoint=https://datalakegs.file.core.windows.net/;"
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Create the container
    container_name = 'verdadunica'
    container_client = ContainerClient.from_connection_string(connect_str, container_name=container_name)
        
    # List the blobs in the container
    blob_list = container_client.list_blobs()
    
    print("\nListing blobs...")
    for blob in blob_list:
        print(blob.name)


except Exception as ex:
    print('Exception:')
    print(ex)