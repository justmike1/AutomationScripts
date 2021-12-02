#   You don't need any telegram libraries or curl scripts
import requests as r

base_url = "https://api.telegram.org/YOURBOTID/sendDocument"
my_files = open("FILE.pdf", "rb")
parameters = {
  "chat_id": "111111111",     # get your chat id from @useridinfobot
  "caption": "Good morning everyone!"
}
files = {
  "document": my_files
}
resp = r.get(base_url, data=parameters, files=files)
print(resp.status_code)   # Just to make sure or to monitor errors
