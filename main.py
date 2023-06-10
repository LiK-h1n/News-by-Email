from requests import get
from send_email import send_email

topic = "rap"

api_key = "6ae6c63b83aa40778bef53d74ec8bd33"
url = (
    "https://newsapi.org/v2/everything?"
    f"q={topic}&"
    "searchIn=content&"
    "sortBy=relevancy&"
    "language=en&"
    "apiKey=6ae6c63b83aa40778bef53d74ec8bd33"
)
request = get(url)
content = request.json()

message = f"Subject: {topic.title()} News\n"
for article in content["articles"][:20]:
    message = message + article["title"] + "\n" + article["url"] + 2 * "\n"

message = message.rstrip().encode("utf-8")

send_email(message)
