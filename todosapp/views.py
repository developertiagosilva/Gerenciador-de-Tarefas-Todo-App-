from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy 
from .models import todo

from datetime import date

from django.shortcuts import get_object_or_404, redirect

# from django.views.generic import DeleteView


class TodoListView(ListView):
    model = todo

class TodoCreateView(CreateView):
    model = todo
    fields = ["titulo", "data_entrega"]
    success_url =reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = todo
    fields = ["titulo", "data_entrega"]
    success_url =reverse_lazy("todo_list")

class TodoDeleteView(DeleteView):
    model = todo
    success_url = reverse_lazy('todo_list')

class TodoCompleteView(View):
    def get(self, request, pk):
        todo_null = get_object_or_404(todo, pk=pk)
        todo_null.datafinal = date.today()
        todo_null.finalizado = True
        todo_null.save()
        return redirect("todo_list")


class TodoCompleteView(View):
    def get(self, request, pk):
        todo_null = get_object_or_404(todo, pk=pk)
        todo_null.mark_has_complete()
        return redirect("todo_list")
