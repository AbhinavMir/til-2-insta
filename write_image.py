import numpy as np
import cv2
import textwrap
import random
import praw
import csv

# Made by the amazing Arun and Abhinav
# stay wired

reddit = praw.Reddit(client_id='3bniLTu50WAOYg', client_secret='9X9f5WFLz_AEYT6S1f7dieDtr8Q', user_agent='til-2-insta')

def callscraper():
    #scrapes r/todayilearned
    posts_list=[]
    top_posts = reddit.subreddit('todayilearned').new(limit=1)
    for post in top_posts:
        print("________")
        print(post.title)
        posts_list.append(post.title)
        print("_____")
        print(post.author)
        author=post.author

        with open("output.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(posts_list)

    #print(posts_list[0])

    img = cv2.imread('images/black.png')
    print(img.shape)

    height, width, channel = img.shape

    text_img = np.ones((height, width))
    print(text_img.shape)
    font = cv2.FONT_HERSHEY_SIMPLEX

    text = posts_list[0]
    wrapped_text = textwrap.wrap(text, width=25)
    x, y = 0,0
    font_size = 1
    font_thickness = 2

    i = 0
    for line in wrapped_text:
        textsize = cv2.getTextSize(line, font, font_size, font_thickness)[0]

        gap = textsize[1] + 10

        y = int((img.shape[0] + textsize[1]) / 2) - (int(len(wrapped_text)/2) - i) * gap
        x = int((img.shape[1] - textsize[0]) / 2)

        cv2.putText(img, line, (x, y), font,
                    font_size, 
                    (255,255,255), 
                    font_thickness, 
                    lineType = cv2.LINE_AA)
        i +=1

    cv2.imwrite('post.jpg',img)

