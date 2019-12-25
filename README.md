# til-2-insta

**ReadMe for TIL-bot**

**About**:

TIL-Bot is an automated bot that scrapes data from reddit's <a href="https://reddit.com/todayileaned">Today-I-Learned</a> sub and posts them to Instagram.

**Technical How-to:**

I used Python's PRAW module, which is *Python Wrapper for Reddit API*. You can perform GET, POST, UPDATE, DELETE using this.

Secondly, I used Pythonic OpenCV to turn this data into a picture.

Lastly, I used Instagram API to upload a new Image every 6 hours to <a href="https://instagram.com/todayilearnedbot">the page</a>.

This script was NOT an API and was running on an Amazon EC2 instance. It was one long script with multiple dependencies.

Due to this we eventually ran out of space on our Instance and had to stop.

**Future work**

Feel free to pull this repo and work more on it.

As of now, I plan to add the following features-

1) Turn this into an API, run a script to call API every 24 hours.

2) Use GANs to make new abstract backgrounds.

____________

Feel free to mail me at contact@abhinavmir.tech

Developed by CleanPegasus and Abhinavmir.
Follow @todayilearnedbot on Instagram.
