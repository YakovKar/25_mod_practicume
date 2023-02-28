import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_pet_with_image(redirected_to_my_pets):
    """Проверка, что у половины карточек питомцев есть фото"""
    #Неявные ожидание
    pytest.driver.implicitly_wait(10)
    # Переменная с картинками
    images = pytest.driver.find_elements(By.XPATH, "//tbody//img")
    #Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody//td[1]")))
    names = pytest.driver.find_elements(By.XPATH, "//tbody//td[1]")

    #Цикл на проверку, что у половины питомцев есть фото
    count_pet_with_image = 0
    for i in range(len(images)):
        if images[i].get_attribute("src") != "":
            count_pet_with_image += 1
    assert count_pet_with_image / len(names) >= 0.5
    print("\n" f"Количество питомцев с фото: {count_pet_with_image}")
    print(f"Количество питомцев в таблице: {len(names)}")


