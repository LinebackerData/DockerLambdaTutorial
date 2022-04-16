def handler(event, context):
    print("Event:", event)
    print("Context:", context)

    return {"event": str(event), "context": str(context), "hello": "world"}
