from todoapp import ma
from todoapp.models import Task
from marshmallow import fields


class TaskSchema(ma.SQLAlchemySchema):
    id = fields.Integer(dump_only=True)
    timestamp = fields.DateTime(format='iso', dump_only=True)

    class Meta:
        model = Task
        fields = ("id", "title", "description", "timestamp")


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
