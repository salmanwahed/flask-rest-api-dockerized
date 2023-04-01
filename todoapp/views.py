from flask import request
from flask_restful import Resource, abort
from todoapp import db, api, app
from todoapp.models import Task
from todoapp.schemas import task_schema, tasks_schema


@app.route('/')
def home():
    return 'Running API...'


class TaskResource(Resource):
    def get(self):
        try:
            tasks = Task.query.all()
            return tasks_schema.dump(tasks)
        except Exception as ex:
            abort(http_status_code=500, error=ex.args[0])

    def post(self):
        try:
            new_task = Task(title=request.json['title'], description=request.json['description'])
            db.session.add(new_task)
            db.session.commit()
            return task_schema.dump(new_task)
        except Exception as ex:
            abort(http_status_code=500, error=ex.args[0])


api.add_resource(TaskResource, '/api/todo')
