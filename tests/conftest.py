import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)   # implicit wait

    driver.get("https://www.fitpeo.com/")   # Hit FitPeo webpage

    request.cls.driver = driver

    yield
    driver.close()
