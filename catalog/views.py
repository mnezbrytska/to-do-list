from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from catalog.forms import TaskForm, TagForm
from catalog.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "catalog/index.html"
    context_object_name = "tasks"
    ordering = ["is_done", "-created_at"]

    def get_queryset(self):
        return Task.objects.prefetch_related("tags").order_by(
            "is_done",
            "-created_at"
        )


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "catalog/task_form.html"
    success_url = reverse_lazy("catalog:index")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "catalog/task_form.html"
    success_url = reverse_lazy("catalog:index")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "catalog/task_confirm_delete.html"
    success_url = reverse_lazy("catalog:index")


def task_change_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect(reverse("catalog:index"))


class TagListView(ListView):
    model = Tag
    template_name = "catalog/tag_list.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "catalog/tag_form.html"
    success_url = reverse_lazy("catalog:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "catalog/tag_form.html"
    success_url = reverse_lazy("catalog:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "catalog/tag_confirm_delete.html"
    success_url = reverse_lazy("catalog:tag-list")
