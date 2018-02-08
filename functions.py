import wx
import messenger
from fbchat import Client
from fbchat.models import *


def login(username, password):
    client = Client(username, password)

    if not client.isLoggedIn():
        client.login(username, password)
    else:
        print "Login successful"
        client.logout()


if __name__ == "__main__":
    app = wx.App(False)
    frame = messenger.MainFrame()
    app.MainLoop()
