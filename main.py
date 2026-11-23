from dynamodb import table

response = table.scan()

tasks = response["Items"]

for task in tasks:
    print(f"Task ID: {task['task_id']}")
    print(f"Title: {task['title']}")
    print(f"Priority: {task['priority']}")
    print(f"Status: {task['status']}")
    print(f"Created At: {task['created_at']}")
    print(f"Description: {task['description']}")
    print("-" * 40)