import pytest
import collections
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_uniqueness_of_names(redirected_to_my_pets):
    """Проверка, что у всех питомцев разные имена """
    #Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody//td[1]")))
    names = pytest.driver.find_elements(By.XPATH, "//tbody//td[1]")
    list_of_names = [names[i].text for i in range(len(names))]
    unique_names = list(set(list_of_names)) #Исключение повторяющихся имен
    assert collections.Counter(list_of_names) == collections.Counter(unique_names)