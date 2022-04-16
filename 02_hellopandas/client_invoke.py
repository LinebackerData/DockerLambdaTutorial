import boto3
import json
import os
from multiprocessing.dummy import Pool


def invoke(s3_url, file_number=None):
    client = boto3.client("lambda")
    event = {"url": s3_url, "file_number": file_number}

    return client.invoke(
        FunctionName="hello-pandas",
        InvocationType="RequestResponse",
        Payload=json.dumps(event),
    )


if __name__ == "__main__":
    bucket_name = os.environ["BUCKET_NAME"]
    s3_url = f"s3://{bucket_name}/test.csv"
    result = invoke(s3_url, file_number=1)
    payload = result["Payload"].read()
    print(json.dumps(json.loads(payload), indent=2))

    # demo with multiprocessing pool
    jobs = [(s3_url, file_number) for file_number in range(1, 10)]
    with Pool(5) as p:
        results = p.starmap(invoke, jobs)
    print(results)
