import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_availability_of_all_pets(redirected_to_my_pets):
    """Проверка присутствия всех питомцев"""
    names = pytest.driver.find_elements(By.XPATH, "//tbody//td[1]")
    #Использую имя питомцев для сравнения со статистикой на сайте
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

    my_data = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

    number = my_data[0].text.split("\n")
    number = number[1].split(":")
    number = int(number[1])

    assert len(names) == number
    print("\n" f"Количество питомцев в статистике пользователя: {number}")
    print(f"Количество питомцев в таблице: {len(names)}")