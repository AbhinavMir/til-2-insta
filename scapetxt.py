import praw
import csv

reddit = praw.Reddit(client_id='3bniLTu50WAOYg', client_secret='9X9f5WFLz_AEYT6S1f7dieDtr8Q', user_agent='til-2-insta')

#scrapes r/todayilearned



posts_list=[]
top_posts = reddit.subreddit('todayilearned').top(limit=1)
for post in top_posts:
    print("________")
    print(post.title)
    posts_list.append(post.title)
    
    with open("output.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(posts_list)

#print(posts_list[0])

