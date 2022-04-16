import json


def handler(event, context):
    print("Event:", event)
    print("Context:", event)

    return {"event": str(event), "context": str(context), "hello": "world"}
