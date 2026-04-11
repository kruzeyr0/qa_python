import pytest
from api_client import APIClient

@pytest.fixture(scope="class")  # Фікстура для створення клієнта API та аутентифікації перед виконанням тестів
def auth_client():
    client = APIClient()
    client.authenticate("test_user", "test_pass")  # Використовуємо правильні облікові дані для аутентифікації
    return client