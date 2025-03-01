#!/bin/bash

# Makes sure there are 3 arguments
if [ "$#" -ne 3]; then
    echo "Usage: $0 <local-file> <bucket-name> <expiration-seconds>"
    exit 1
fi

# Assign input arguments to variables
LOCAL_FILE=$1
BUCKET_NAME=$2
EXPIRATION=$3

# Upload the file to the S3 bucket
aws s3 cp "$LOCAL_FILE" s3://"$BUCKET_NAME"/

# Generate a presigned URL
SIGNED_URL=$(aws s3 presign --expires-in "$EXPIRATION" s3://"$BUCKET_NAME"/"$LOCAL_FILE")

echo "Presigned URL (expires in $EXPIRATION seconds):"
echo "$SIGNED_URL"

