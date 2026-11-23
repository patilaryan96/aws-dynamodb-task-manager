# AWS DynamoDB Task Manager

A two-tier task management application built using Python Flask and Amazon DynamoDB.

The application allows users to create, view, update, and delete tasks through a web interface, with task data stored persistently in DynamoDB.

## Architecture

- **Application Layer:** Python, Flask, HTML, CSS
- **Database Layer:** Amazon DynamoDB
- **AWS SDK:** Boto3
- **Development Environment:** Windows, VS Code

## Features

- Create tasks with title, description, and priority
- View tasks stored in DynamoDB
- Update task status between Pending and Completed
- Delete tasks
- Persistent cloud database storage
- UUID-based task identifiers
- Flask health check endpoint

## Technologies Used

- Python
- Flask
- Boto3
- Amazon DynamoDB
- AWS IAM
- HTML
- CSS
- Git
- GitHub

## Project Structure

```text
aws-dynamodb-task-manager/
├── app.py
├── dynamodb.py
├── main.py
├── create_task.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/patilaryan96/aws-dynamodb-task-manager.git
cd aws-dynamodb-task-manager
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure AWS credentials

Configure AWS CLI with credentials for an IAM identity that has appropriate DynamoDB permissions.

```bash
aws configure
```

Set the region to:

```text
ap-south-1
```

### 5. Create the DynamoDB table

Create a DynamoDB table named:

```text
CloudTaskManager
```

Partition key:

```text
task_id (String)
```

### 6. Run the application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## DynamoDB Operations

| Operation | Boto3 Method |
|---|---|
| Create task | `put_item()` |
| Read tasks | `scan()` |
| Update task | `update_item()` |
| Delete task | `delete_item()` |

## Security

AWS credentials are not stored in the source code. The application uses AWS credential configuration and IAM permissions to communicate with DynamoDB.

## Future Enhancements

- Deploy application on Amazon EC2
- Configure IAM roles for EC2
- Automate infrastructure using Terraform
- Add task filtering and search
- Implement CI/CD using GitHub Actions
- Improve application security and production configuration