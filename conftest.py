import pytest
from settings import valid_email, valid_password
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(autouse=True)
def testing():
    """Открытие драйвера Chrome и переход на страницу авторизации"""
    pytest.driver = webdriver.Chrome("D:\\python_selen\\chromedriver_win32\\chromedriver.exe")
    #Переходим на страницу авторизации
    pytest.driver.get("https://petfriends.skillfactory.ru/login")

    yield

    pytest.driver.quit()

@pytest.fixture()
def redirected_to_my_pets():
    """Функция перехода на страницу 'Мои питомцы'"""
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    pytest.driver.find_element(By.ID, "email").send_keys(valid_email)

    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
    pytest.driver.find_element(By.ID, "pass").send_keys(valid_password)

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    pytest.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.nav-link[href='/my_pets']")))
    pytest.driver.find_element(By.CSS_SELECTOR, "a.nav-link[href='/my_pets']").click()
