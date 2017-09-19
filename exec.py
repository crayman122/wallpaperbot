#Made by Red in 2017
#Greetings from Cleveland!
#http://reddragonte.ch/
#Licensed under the GPL v3.0s
#Wallpaper scraper for reddit


import praw #Python Reddit API Wrapper
import os #To run system commands and manage filesystem the easy way.
import time

reddit = praw.Reddit(client_id='<client id>',
                     client_secret='<client secret>',
                     password='<user account password>',
                     user_agent='<user agent name>',
                     username='<user account name>') #Log in to reddit.

subreddit = reddit.subreddit('earthporn') #Set subreddit to r/earthporn, could possibly add different subreddits in the future.

def getWallpapers():
	for submission in reddit.subreddit('earthporn').hot(limit=25): #get 25 hottest submissions
		url = submission.url #Begin URL Parsing
		if ".jpg" in url or ".jpeg" in url or ".png" in url: #Determine if URL is acceptable image format.
			os.system("wget -P /var/www/html/stuff/wallpaper %s" %(url)) #Download image into folder, format could cause problems, but probably wont. URLs are automatically santized by the browser.
		else:
			pass
	os.system("rm /var/www/html/stuff/wallpaper/*.1") #Remove duplicates
	os.system("rm /var/www/html/stuff/wallpaper/*.2") #Remove double duplicates
	
	os.system("rm /war/www/html/stuff/wallpaper/All.zip") #Remove existing zip file
	os.system("zip /var/www/html/stuff/wallpaper/All.zip /var/www/html/stuff/wallpaper/*") #Zip into single file, perfect for downloading
	
while True:		
	if int(time.strftime("%H", time.gmtime())) == 00 and int(time.strftime("%M", time.gmtime())) == 0: #Run the script at a certain time, mainly midnight of every day
		getWallpapers()
		time.sleep(60)
	else:
		time.sleep(60) #used to prevent thread from taking 100% of CPU all the time
