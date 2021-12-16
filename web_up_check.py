import requests
import re
import os

url = os.environ['URL']

 # Checks if URL is valid
def check_1(url):
# Regex to check valid URL
    regex = ("((http|https)://)(www.)?" +
		    "[a-zA-Z0-9@:%._\\+~#?&//=]" +
		    "{2,256}\\.[a-z]" +
		    "{2,6}\\b([-a-zA-Z0-9@:%" +
		    "._\\+~#?&//=]*)")
	
	# Compile the ReGex
    p = re.compile(regex)

    if (re.search(p, url)):
        return True
    else:
        return False


 # Checks if web URL returns 200 status code to http head request
def check_2(url):
    try:
        response = requests.head(url)
         
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

# Checks both conditions
def web_ok(url):
    is_up = check_1(url) and check_2(url)
    if is_up:
        return "OK"
    else:
        return "Failure"

print(web_ok(url))
 



