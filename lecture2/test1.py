import time

import yaml
from module import Site

with open("./testdata.yaml") as f:
	testdata = yaml.safe_load(f)
site = Site(testdata['address'])
login = testdata['login']
password = testdata['password']


def test_step1(sel_1, x_selector2, x_selector3, result, btn_selector):
	input1 = site.find_element('xpath', sel_1)
	input1.send_keys("test")
	input2 = site.find_element('xpath', x_selector2)
	input2.send_keys("test")
	btn = site.find_element('css', btn_selector)
	btn.click()
	err_label = site.find_element('xpath', x_selector3)
	res = err_label.text
	assert res == result


def test_step2(sel_1, x_selector2, auth, result2, btn_selector):
	input1 = site.find_element('xpath', sel_1)
	input1.clear()
	input1.send_keys(login)
	input2 = site.find_element('xpath', x_selector2)
	input2.clear()
	input2.send_keys(password)
	btn = site.find_element('css', btn_selector)
	btn.click()
	auth = site.find_element('xpath', auth)
	res = auth.text
	assert res == result2


def test_step3(add_post, input_title, post_title, input_description, post_description, input_content,
               post_content, create_post, check_post):
	add_post_btn = site.find_element('xpath', add_post)
	add_post_btn.click()
	input_title = site.find_element('xpath', input_title)
	input_title.send_keys(post_title)
	input_description = site.find_element('xpath', input_description)
	input_description.send_keys(post_description)
	input_content = site.find_element('xpath', input_content)
	input_content.send_keys(post_content)
	create_post_btn = site.find_element('xpath', create_post)
	create_post_btn.click()
	time.sleep(10)
	res = site.find_element('xpath', check_post)
	res = res.text
	site.close()
	assert post_title == res
