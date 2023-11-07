from facebook_scraper import get_profile
from platform import system as reset
from os import system


target_user = input("Enter Target FB Userlink: ")
print("Sending requests...")
get_profile(target_user)

remove = ["- Kasalukuyan", "Kasalukuyang lungsod", "Bayang kinalakihan"]
tl = ["Enero", "Pebrero", "Marso", "Abril", "Mayo", "Hunyo", "Hulyo", "Agosto", "Setyembre", "Oktubre", "Nobyembre", "Disyembre"]
en = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

if reset().upper() == "WINDOWS":
	system('cls')
else:
	system('clear')


def get_name():
	try:
		if get_profile(target_user)['Name'] == "Hindi Makita ang Nilalaman":
			return "Private"
		else:
			get_profile(target_user)['Name']
	except:
		return "Private"

def get_id():
	try:
		return get_profile(target_user)['id']
	except:
		return "Private"

def get_work():
	try:
		return get_profile(target_user)['Trabaho'].replace(tl[0], en[0]).replace(tl[1], en[1]).replace(tl[2], en[2]).replace(tl[3], en[3]).replace(tl[4], en[4]).replace(tl[5], en[5]).replace(tl[6], en[6]).replace(tl[7], en[7]).replace(tl[8], en[8]).replace(tl[9], en[9]).replace(tl[10], en[10]).replace(tl[11], en[11])
	except:
		return "Private"

def get_loc():
	try:
		return get_profile(target_user)['Mga Lugar na Tinirhan']
	except:
		return "Private"

def get_friend():
	try:
		return get_profile(target_user)['Friend_count']
	except:
		return "Private"

def get_follower():
	try:
		return get_profile(target_user)['Follower_count']
	except:
		return "Private"

def get_quotes():
	try:
		return get_profile(target_user)['Mga Paboritong Quote']
	except:
		return "Private"


INFO = f"""User: {target_user}
FullName: {get_name()}
ID: {get_id()}
Work: {get_work()}
lives in: {get_loc()}
TotalFriends: {get_friend()}
TotalFollowers: {get_follower()}
Quotes: {get_quotes()}
""".replace(remove[0], "").replace(remove[1], "").replace(remove[2], "")


if __name__ == "__main__":
	print("Getting Info...")
	print(INFO)









