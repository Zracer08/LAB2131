tasks = []

def add_task(task_name):
    tasks.append(task_name)
    return f"Задача '{task_name}' добавлена."

def get_tasks():
    return tasks

def clear_tasks():
    tasks.clear()
    return "Список задач очищен."