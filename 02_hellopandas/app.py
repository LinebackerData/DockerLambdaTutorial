import json
import boto3
import pandas as pd
import os
from summify import sum_my_df


def handler(event, context):
    print("Event:", event)
    print("Context:", context)

    # print the file using boto and s3
    s3_url = event["url"]
    file_number = event.get("file_number", "")
    s3_url_split = s3_url.replace("s3://", "").split("/", maxsplit=1)
    print(f"{s3_url=}")
    bucket_name, key = s3_url_split
    print(f"{bucket_name=}")

    # note that we can just read directly
    df = pd.read_csv(s3_url)
    print(df.to_csv())

    # do something non-trival...in this case just sum()
    # and use another module while we are at it
    df2 = sum_my_df(df)
    print(df2.to_csv())

    # let's create some output
    output_replace = f"/test_output{file_number}.csv.gz"

    s3_url_output = s3_url.replace("/test.csv", output_replace)

    df2.to_csv(s3_url_output, index=False)

    return {
        "s3_url": s3_url,
        "s3_url_output": s3_url_output,
    }


if __name__ == "__main__":
    bucket_name = os.environ["BUCKET_NAME"]
    event = {"url": f"s3://{bucket_name}/test.csv"}
    result = handler(event, None)
    print(json.dumps(result, indent=2))
