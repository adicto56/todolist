from django.shortcuts import render, redirect

def index(request):
    # Get tasks from session, each task is a dict: {'text': ..., 'done': ...}
    tasks = request.session.get('tasks', [])
    return render(request, 'index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        task_text = request.POST.get('task')
        if task_text:
            tasks = request.session.get('tasks', [])
            tasks.append({'text': task_text, 'done': False})  # new task is not done
            request.session['tasks'] = tasks
    return redirect('index')

def delete_task(request, task_id):
    tasks = request.session.get('tasks', [])
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        request.session['tasks'] = tasks
    return redirect('index')

def toggle_task(request, task_id):
    tasks = request.session.get('tasks', [])
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = not tasks[task_id]['done']  # toggle completion
        request.session['tasks'] = tasks
    return redirect('index')
