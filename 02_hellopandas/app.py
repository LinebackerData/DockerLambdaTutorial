import json
import boto3
import pandas as pd
import os


def handler(event, context):
    print("Event:", event)
    print("Context:", event)

    s3_client = boto3.client("s3")
    s3_url = event['url']
    s3_url_split = s3_url.replace("s3://", "").split("/", maxsplit=1)
    print(f"{s3_url=}")
    bucket_name, key = s3_url_split
    print(f"{bucket_name=}")

    # note that we can just read directly
    df = pd.read_csv(s3_url)
    print(df.to_markdown())

    df2 = df.sum()
    print(df2.to_markdown())

    s3_url_output = s3_url.replace("/test.csv", "/test_output.csv")

    df2.to_csv(s3_url_output, index=False)



    data = s3_client.get_object(Bucket=bucket_name, Key=key)["Body"].read().decode()

    return {
        "event": str(event),
        "context": str(context),
        "hello": "world",
        "s3_url": s3_url,
        "data": data,
    }


if __name__ == "__main__":
    bucket_name = os.environ["BUCKET_NAME"]
    event = {"url": f"s3://{bucket_name}/test.csv"}
    result = handler(event, None)
    print(json.dumps(result, indent=2))
