import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

@pytest.fixture(scope="function")
def driver():
    edge_options = Options()
    edge_options.add_argument("--headless")
    service = Service()
    driver = webdriver.Edge(service=service, options=edge_options)
    yield driver
    driver.quit()