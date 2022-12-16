from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import TodoList, TodoItem

# Create your views here.

class ListListView(ListView):
    model = TodoList
    template_name = "todo_app/index.html"

class ItemListView(ListView):
    model = TodoItem
    template_name = "todo_app/todo_list.html"

    def get_queryset(self):
        return TodoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = TodoList.objects.get(id=self.kwargs["list_id"])
        return context

class ListCreate(CreateView):
    model = TodoList
    fields = ["title"]

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context
    
class ItemCreate(CreateView):
    model = TodoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date"
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = TodoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = TodoList.objects.get(id=self.kwargs['list_id'])
        context["todo_list"] = todo_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

class ItemUpdate(UpdateView):
    model = TodoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date"
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

class ListDelete(DeleteView):
    model = TodoList
    # You have to use reverse_lazy() instead of reverse(),
    # as the urls are not loaded when the file is imported.
    success_url = reverse_lazy("index")

class ItemDelete(DeleteView):
    model = TodoItem

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context