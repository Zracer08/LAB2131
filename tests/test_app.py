import pytest
from utils import add_task, get_tasks, clear_tasks

@pytest.fixture(autouse=True)
def reset_tasks():
    clear_tasks()

def test_add_task():
    assert add_task("Купить молоко") == "Задача 'Купить молоко' добавлена."
    assert "Купить молоко" in get_tasks()

def test_get_tasks():
    add_task("Задача 1")
    add_task("Задача 2")
    
    assert len(get_tasks()) == 2
    assert get_tasks() == ["Задача 1", "Задача 2"]