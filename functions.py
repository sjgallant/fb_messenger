import wx
import mainframe
from fbchat import Client
from fbchat.models import *


def login(username, password):
    print( __name__)
    client = Client(username, password)

    if client.isLoggedIn():
        return True, client
    else:
        return False, None


def send_message(client, message):
    client.send(Message(text=message), thread_id=client.uid, thread_type=ThreadType.USER)


if __name__ == "__main__":
    app = wx.App(False)
    frame = mainframe.MainFrame()
    app.MainLoop()

