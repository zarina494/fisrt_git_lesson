import reguests
def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandboxcfcfbe65c9814d799bb34688336e685c.mailgun.org/messages",
		auth=("api", "04a9cef30c03d70bb4850a8ffc05eaad-9b1bf5d3-4d96573"),
		data={"from": "Sadykova-zarina@inbox.ru",
			"to": ["maximneveraa@gmail.com"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})
send_simple_message()