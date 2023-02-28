import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_all_pet_parameters(redirected_to_my_pets):
    """Проверка, что у всех питомцев есть имя, возраст и  порода"""
    #Добавим неявное ожидание
    pytest.driver.implicitly_wait(10)
    names = pytest.driver.find_elements(By.XPATH, "//tbody//td[1]")
    pytest.driver.implicitly_wait(10)
    # Переменная породы
    breeds = pytest.driver.find_elements(By.XPATH, "//tbody//td[2]")
    pytest.driver.implicitly_wait(10)
    # Переменная возраста
    ages = pytest.driver.find_elements(By.XPATH, "//tbody//td[3]")
    #Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
    #Статистика с сайта
    my_data = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

    #Выясняем количество питомцев согласно статистики
    number = my_data[0].text.split("\n")
    number = number[1].split(":")
    number = int(number[1])

    #Проверяем, что у каждого питомца есть имя, порода и возраст
    assert len(names) == number
    assert len(breeds) == number
    assert len(ages) == number
    print("\n" f"Количество питомцев с именем: {len(names)}")
    print("\n" f"Количество питомцев с породой: {len(breeds)}")
    print("\n" f"Количество питомцев с возрастом: {len(ages)}")