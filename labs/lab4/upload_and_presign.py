import boto3
import urllib.request

# Initialize the S3 client
s3 = boto3.client('s3', region_name='us-east-1')

# Define the S3 bucket and file details
bucket_name = 'ds2002-jcm5md'
file_url = 'https://no-cdn.shortpixel.ai/client/to_avif,q_lossy,ret_wait/https://shortpixel.com/blog/wp-content/uploads/2023/12/nyan-cat.gif'
local_file = 'sample.gif'

# Fetch the file from the internet and save it locally
urllib.request.urlretrieve(file_url, local_file)

# Upload the file to S3
with open(local_file, 'rb') as data:
    s3.put_object(
        Body=data,
        Bucket=bucket_name,
        Key=local_file
    )

# Generate a presigned URL for the file
expires_in = 3600  # Expiration time in seconds (1 hour)
presigned_url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': local_file},
    ExpiresIn=expires_in
)

# Output only the presigned URL
print(presigned_url)

