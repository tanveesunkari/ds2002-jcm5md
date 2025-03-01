import boto3

# Create an S3 client
s3 = boto3.client('s3', region_name='us-east-1')

# Your S3 bucket name
bucket = 'ds2002-jcm5md'

# Path to the local file you want to upload
local_file = 'sun.jpg'

# Open the file and upload it to S3
with open(local_file, 'rb') as data:
    resp = s3.put_object(
        Body=data,
        Bucket=bucket,
        Key='sun.jpg',  # This is the name it will have in S3
        ACL='public-read'  # Make the file public
    )

# Print the response for debugging
print(resp)

# Check the contents of the bucket (Optional)
response = s3.list_objects_v2(Bucket=bucket)

for obj in response.get('Contents', []):
    print(obj['Key'])

# Optionally print the URL for the uploaded file
file_url = f"https://{bucket}.s3.amazonaws.com/sun.jpg"
print(f"File URL: {file_url}")
