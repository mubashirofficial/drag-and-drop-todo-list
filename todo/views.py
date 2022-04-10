from django.shortcuts import render, redirect
from.models import Tasks
from django.db.models import Max
from django.views.generic.list import ListView
# Create your views here.

class home(ListView):
    template_name = 'todo.html'
    model = Tasks
    context_object_name = 'tasks'

    def get_queryset(self):
        return Tasks.objects.all()



def add_players(request):
    name = request.POST.get('pname')
    Tasks.objects.get_or_create(task=name, order=get_max_order())
    ts = Tasks.objects.all()
    return redirect('home')

def get_max_order() -> int:
    existing_tasks = Tasks.objects.all()
    if not existing_tasks.exists():
        return 1
    else:
        current_max = existing_tasks.aggregate(max_order=Max('order'))['max_order']
        return current_max + 1

def delete_player(request, pk):
    Tasks.objects.get(pk=pk).delete()
    reorder()
    return redirect('home')


def reorder():
    existing_tasks = Tasks.objects.filter()
    if not existing_tasks.exists():
        return
    number_of_tasks = existing_tasks.count()
    new_ordering = range(1, number_of_tasks + 1)

    for order, task_order in zip(new_ordering, existing_tasks):
        task_order.order = order
        task_order.save()

def sort(request):
    tasks_pks_order = request.POST.getlist('task_order')
    tasks = []
    for idx, task_pk in enumerate(tasks_pks_order, start=1):
        pl = Tasks.objects.get(pk=task_pk)
        pl.order = idx
        pl.save()
        tasks.append(pl)




def tasklist(request):
    ts = Tasks.objets.all()
    return render(request, 'list.html', {'tasks': ts})

