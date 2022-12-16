from django.contrib import admin
from todo_app.models import TodoItem, TodoList

# Register your models here.

admin.site.register(TodoItem)
admin.site.register(TodoList)