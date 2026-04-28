import requests

# Simulating task creation in ClickUp via API
url = "https://api.clickup.com/api/v2/list/123456/task"

headers = {
    "Authorization": "YOUR_API_TOKEN",
    "Content-Type": "application/json"
}

data = {
    "name": "Nova tarefa automatizada",
    "description": "Tarefa criada automaticamente via integração",
    "status": "to do",
    "priority": 3
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200 or response.status_code == 201:
    print("Task created successfully!")
else:
    print("Error creating task:", response.text)
