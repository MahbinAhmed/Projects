import requests

r = requests.get("https://upload.wikimedia.org/wikipedia/commons/6/62/Natural_Beauty_of_BD.jpg")
# print(r.content)
with open("downloaded.png","wb") as f:
    f.write(r.content)
print("Image downloaded successfully!")

