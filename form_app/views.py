from django.shortcuts import render

TASKS = []

# Create your views here.
def create_task(request):
    print(request.GET)

    task = request.GET.get('task')

    if task:
        TASKS.append(task)
    print(TASKS)

    return render(
        request,
        'form_app/task_form.html',
        context={
            'tasks': TASKS
        })