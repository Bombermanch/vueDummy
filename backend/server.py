import bottle
from truckpad.bottle.cors import CorsPlugin, enable_cors

app = bottle.Bottle()

class TodoItem:
    def __init__(self, description, unique_id):
        self.description = description
        self.is_completed = False
        self.uid = unique_id

    def __str__(self):
        return self.description.lower()

    def to_dict(self):
        return {
            "description": self.description,
            "is_completed": self.is_completed,
            "uid": self.uid
        }


tasks_db = {
    uid: TodoItem(desc, uid)
    for uid, desc in enumerate(
        start=1,
        iterable=[
            "прочитать книгу",
            "учиться жонглировать 30 минут",
            "помыть посуду",
            "поесть",
        ],
    )
}


@enable_cors
@app.route("/api/tasks/")
def index():
    tasks = [task.to_dict() for task in tasks_db.values()]
    return {"tasks": tasks}



app.install(CorsPlugin(origins=['http://localhost:8080']))

if __name__ == "__main__":
    bottle.run(app, host="localhost", port=5000)