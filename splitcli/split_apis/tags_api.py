from splitcli.split_apis import http_client

def tags_base_url(workspace_id):
    return f"tags/ws/{workspace_id}"

def tags_create_url(workspace_id, object_name, object_type):
    base_url = tags_base_url(workspace_id)
    return f"{base_url}/object/{object_name}/objecttype/{object_type}"

def add_tags(workspace_id, object_name, tags, object_type="Split"):
    path = tags_create_url(workspace_id,object_name,object_type)
    content = tags
    result = http_client.post(path, content)
    print(path)
    return result