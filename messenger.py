import wx
import functions
import config
import threading

if "2.8" in wx.version():
    import wx.lib.pubsub.setupkwargs
    from wx.lib.pubsub import pub
else:
    from wx.lib.pubsub import pub


########################################################################
class MessageDialog(wx.Dialog):
    """ Class to define message menu """
    def __init__(self):
        """ Constructor """
        wx.Dialog.__init__(self, None, title="Send Message")

        # Message info
        msg_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.message = wx.TextCtrl(self, style=wx.TE_BESTWRAP | wx.EXPAND)
        config.messagesBox = wx.TextCtrl(self, style=wx.TE_READONLY | wx.TE_MULTILINE | wx.TE_BESTWRAP)

        msg_box_sizer = wx.BoxSizer(wx.HORIZONTAL)
        msg_box_sizer.Add(config.messagesBox, wx.ALL, 10)
        msg_sizer.Add(self.message, 0, wx.ALL | wx.EXPAND, 5)

        # pass info
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

        """ Add buttons to their own horizontal sizer
            then add btn_sizer to main_sizer """
        # Starts listening
        self.startThread()

        # Send Button
        send_btn = wx.Button(self, label="Send")
        send_btn.SetDefault()
        send_btn.Bind(wx.EVT_BUTTON, self.sendMessage)
        msg_sizer.Add(send_btn, 0, wx.ALL, 5)

        # Logout Button
        logout_btn = wx.Button(self, label="Logout")
        logout_btn.Bind(wx.EVT_BUTTON, self.logout)
        btn_sizer.Add(logout_btn, 0, wx.ALL | wx.CENTER, 5)

        main_sizer.Add(msg_box_sizer, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(msg_sizer, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(btn_sizer)

        self.SetSizer(main_sizer)
        self.Maximize(True)

        # Adds Icon image to window
        icon = wx.Icon('Images\icon.ico', wx.BITMAP_TYPE_ICO, 32, 32)
        wx.Frame.SetIcon(self, icon)

    def sendMessage(self, event):
        """ Send message """
        # Gets value of message box
        msg = self.message.GetValue()
        # Sends message
        functions.send_message(config.client, msg)
        # Clears textbox
        self.message.Value = ""
        config.messagesBox.Value += "Me: " + msg + '\n'

    def logout(self, event):
        config.client.logout()
        config.listener.logout()
        self.Destroy()

    def startListen(self):
        config.client.listen()

    def startThread(self):
        thread = threading.Thread(target=self.startListen)
        thread.start()




