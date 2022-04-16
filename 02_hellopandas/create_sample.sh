#!/bin/bash
if [ -z $BUCKET_NAME ]
then
    echo "Please define bucketname: export BUCKET_NAME=<your-bucket-goes-here>"
    exit 1
fi
s3_url="s3://${BUCKET_NAME}/test.csv"
printf "a,b,c\n1,2,3\n4,5,6\n7,8,9" | aws s3 cp - ${s3_url}
echo "Wrote sample data to ${s3_url}"
aws s3 cp ${s3_url} -
echo ""