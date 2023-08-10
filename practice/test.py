from task_func import post,auth


def test_step1():
	assert auth() == 200, "TEST1 FAIL"


def test_step2(title, description, content):
	assert post(title, description, content) == description, "TEST2 FAIL"
	
