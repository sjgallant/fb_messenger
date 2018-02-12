from fbchat import Client

pwd = raw_input("Enter password: ")
client = Client("sj-gallant@comcast.net", pwd)

client.listen()