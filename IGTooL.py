import pyfiglet
import requests
import os
import json
import shutil
from bs4 import BeautifulSoup
import webbrowser 
import wikipedia

main=pyfiglet.figlet_format(" IGTooL By Devshimitsu")
print(main)

print("\n \n[.]  Download Profile Picture")
print("[.]  Get Profile Detail")
print("[.]  Devshimitsu's Instagram Account")

try:
	inp=int(input("\nType Number: "))
	if inp == 1:
		try:
			header = {
				"User-Agent": "Chrome/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
			}

			INSTA_URL = "https://www.instagram.com/"
			USER_ID = input("Instagram Username: ")
			TAIL = "/?__a=1"
			URL = INSTA_URL + USER_ID + TAIL
			response = requests.get(URL, headers=header).json()
			hd_image_location = response["graphql"]["user"]["profile_pic_url_hd"]
			hd_image_response = requests.get(hd_image_location, stream=True)
			with open(USER_ID+".jpg", "wb") as out_file:
				shutil.copyfileobj(hd_image_response.raw, out_file)
		except:
			print("\nWrong UserName\n")
		


	elif inp == 2:
		try:
			URL = "https://www.instagram.com/{}/"
			def parse_data(s):
				data = {}
				s = s.split("-")[0]
				s = s.split(" ")
				data['Followers'] = s[0] 
				data['Following'] = s[2] 
				data['Posts'] = s[4]
				return data
			def scrape_data(username):
				r = requests.get(URL.format(username))
				s = BeautifulSoup(r.text, "html.parser")
				meta = s.find("meta", property ="og:description")
				return parse_data(meta.attrs['content']) 
			if __name__=="__main__":
				username = input("your Instagra UserName: ")
				data = scrape_data(username)
				print(data) 

		except:
			print("\nWrong UserName\n")

	elif inp == 3:
		try:
			wikipedia.summary("Instagram")
			webbrowser.open("https://www.instagram.com/devshimitsu/")

		except:
			print("\n Check Your Internet Connection \n")
		
	else:
		print("Wrong Option")
except:
	print("Check Your Internet Connection")
