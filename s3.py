import boto3

aws_access_key_id = 'Access key Id'
aws_secret_access_key = 'Secrest acces key'
region_name = 'us-east-1' 

s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)


bucket_name = 'nikhilmeenabuvket'

try:
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' created successfully.")
except Exception as e:
    print(f"Error creating bucket: {e}")
