import wx
import functions
from fbchat import Client

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

        msg_lbl = wx.StaticText(self, label="Message:")
        msg_sizer.Add(msg_lbl, 0, wx.ALL | wx.CENTER, 5)
        self.message = wx.TextCtrl(self)
        msg_sizer.Add(self.message, 0, wx.ALL, 5)

        # pass info
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(msg_sizer, 0, wx.ALL, 5)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

        """ Add buttons to their own horizontal sizer
            then add btn_sizer to main_sizer """
        # Send Button
        send_btn = wx.Button(self, label="Send")
        send_btn.SetDefault()
        send_btn.Bind(wx.EVT_BUTTON, self.sendMessage)
        btn_sizer.Add(send_btn, 0, wx.ALL | wx.CENTER, 5)

        # Logout Button
        logout_btn = wx.Button(self, label="Logout")
        logout_btn.Bind(wx.EVT_BUTTON, self.logout)
        btn_sizer.Add(logout_btn, 0, wx.ALL | wx.CENTER, 5)

        main_sizer.Add(btn_sizer)

        self.SetSizerAndFit(main_sizer)

        # Adds Icon image to window
        icon = wx.Icon('Images\icon.ico', wx.BITMAP_TYPE_ICO, 32, 32)
        wx.Frame.SetIcon(self, icon)

    def sendMessage(self, event):
        """ Send message """
        # Gets value of message box
        msg = self.message.GetValue()
        # Sends message
        functions.send_message(client, msg)
        # Clears textbox
        self.message.Value = ""

    def logout(self, event):
        global client
        client.logout()
        self.Destroy()
