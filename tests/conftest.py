import shutil
import os
import pytest

@pytest.fixture(scope="session", autouse=True)
def cleanup_results():
    # Путь к папке с результатами
    results_dir = "test-results"
    # Если папка существует, удаляем её целиком
    if os.path.exists(results_dir):
        shutil.rmtree(results_dir)
    # Создаем пустую папку заново
    os.makedirs(results_dir)
