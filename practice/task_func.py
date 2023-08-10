import requests
import yaml

with open("config.yaml", "r") as f:
	d = yaml.safe_load(f)


def auth():
	data = {
		"username": d["login"],
		"password": d["password"]
	}
	print(d["url_auth"])
	res = requests.post(url=d["url_auth"], data=data)
	return res.status_code


def post(title, description, content):
	headers = {
		'X-Auth-Token': d["token"]
	}
	data = {
		"title": title,
		"description": description,
		"content": content,
	}
	res = requests.post(url=d["url_post"], headers=headers, json=data)
	return res.json()["description"]


if __name__ == '__main__':
	print(auth())
	print(post("aa", "sss", "fff"))
