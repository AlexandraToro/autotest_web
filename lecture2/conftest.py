import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import pytest

with open("./testdata.yaml") as f:
	testdata = yaml.safe_load(f)
	browser = testdata['browser']

login = testdata['login']


@pytest.fixture(scope="session")
def browser():
	if browser == 'firefox':
		service = Service(executable_path=GeckoDriverManager().install())
		options = webdriver.FirefoxOptions()
		driver = webdriver.Firefox(service=service, options=options)
	else:
		service = Service(executable_path=ChromeDriverManager().install())
		options = webdriver.ChromeOptions()
		driver = webdriver.Chrome(service=service, options=options)
	yield driver
	driver.quit()


@pytest.fixture
def title_api():
	return "New post"


@pytest.fixture
def description_api():
	return "New description"


@pytest.fixture
def content_api():
	return "New content"

#
# @pytest.fixture()
# def sel_1():
# 	return '//*[@id="login"]/div[1]/label/input'
#
#
# @pytest.fixture()
# def x_selector2():
# 	return '//*[@id="login"]/div[2]/label/input'
#
#
# @pytest.fixture()
# def x_selector3():
# 	return '//*[@id="app"]/main/div/div/div[2]/h2'
#
#
# @pytest.fixture()
# def btn_selector():
# 	return 'button'
#
#
# @pytest.fixture()
# def result():
# 	return '401'
#
#
# @pytest.fixture()
# def auth():
# 	return '//*[@id="app"]/main/nav/ul/li[3]/a'
#
#
# @pytest.fixture()
# def result2():
# 	return f'Hello, {login}'
#
#
# @pytest.fixture()
# def add_post():
# 	return '//*[@id="create-btn"]'
#
#
# @pytest.fixture()
# def input_title():
# 	return '//*[@id="create-item"]/div/div/div[1]/div/label'
#
#
# @pytest.fixture()
# def post_title():
# 	return 'Title of practice#2'
#
#
# @pytest.fixture()
# def input_description():
# 	return '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea'
#
#
# @pytest.fixture()
# def post_description():
# 	return 'Description of post in practice#2'
#
#
# @pytest.fixture()
# def input_content():
# 	return '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea'
#
#
# @pytest.fixture()
# def post_content():
# 	return 'Content of post in practice#2'
#
#
# @pytest.fixture()
# def create_post():
# 	return '/html/body/div/main/div/div/form/div/div/div[7]/div/button'
#
#
# @pytest.fixture()
# def check_post():
# 	return '//*[@id="app"]/main/div/div[1]/h1'
#
