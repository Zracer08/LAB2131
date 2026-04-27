from utils import add_task, get_tasks

if __name__ == "__main__":
    print("Менеджер задач запущен!")
    
    add_task("Изучить основы DevOps")
    add_task("Настроить CI/CD в GitHub Actions")
    
    print("Текущие задачи:", get_tasks())