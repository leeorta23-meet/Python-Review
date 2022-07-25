def create_youtube_video(title, description):
	return {"title": title, "description": description, "likes": 0 , "dislikes": 0, "comments": {} }
	

title = input("What is your title?:")
description = input("What is your description?:")

new_video = create_youtube_video(title, description)

print("")
print("Title:" + title)
print ("Description:" + description)

def likes(new_video):
	if "likes" in new_video:
		new_video["likes"] +=1
	return new_video


def dislikes(new_video):
	if "dislikes" in new_video:
		new_video["dislikes"] +=1
	return new_video


def add_comment(new_video, username, comment_text):
	if "comments" in new_video:
		new_video["comments"][username] = comment_text
		return new_video

username = "dogsyyy"
comment_text = "liked the video"





likes(new_video)
dislikes(new_video)
add_comment(new_video, username, comment_text)

print(new_video)
