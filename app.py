from flask import Flask, render_template, request, redirect, url_for
from dynamodb import table
from datetime import datetime
import uuid

app = Flask(__name__)


def get_tasks():
    response = table.scan()
    tasks = response.get("Items", [])

    while "LastEvaluatedKey" in response:
        response = table.scan(
            ExclusiveStartKey=response["LastEvaluatedKey"]
        )
        tasks.extend(response.get("Items", []))

    tasks.sort(key=lambda task: task.get("created_at", ""), reverse=True)

    return tasks


@app.route("/")
def index():
    tasks = get_tasks()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    priority = request.form.get("priority", "Medium")

    if not title:
        return redirect(url_for("index"))

    task = {
        "task_id": str(uuid.uuid4()),
        "title": title,
        "description": description,
        "priority": priority,
        "status": "Pending",
        "created_at": datetime.now().isoformat()
    }

    table.put_item(Item=task)

    return redirect(url_for("index"))


@app.route("/complete/<task_id>", methods=["POST"])
def complete_task(task_id):
    response = table.get_item(
        Key={"task_id": task_id}
    )

    task = response.get("Item")

    if task:
        new_status = (
            "Completed"
            if task["status"] != "Completed"
            else "Pending"
        )

        table.update_item(
            Key={"task_id": task_id},
            UpdateExpression="SET #status = :status",
            ExpressionAttributeNames={
                "#status": "status"
            },
            ExpressionAttributeValues={
                ":status": new_status
            }
        )

    return redirect(url_for("index"))


@app.route("/delete/<task_id>", methods=["POST"])
def delete_task(task_id):
    table.delete_item(
        Key={"task_id": task_id}
    )

    return redirect(url_for("index"))


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(debug=True)