import wx
import functions
from fbchat import Client

if "2.8" in wx.version():
    import wx.lib.pubsub.setupkwargs
    from wx.lib.pubsub import pub
else:
    from wx.lib.pubsub import pub


########################################################################
class LoginDialog(wx.Dialog):
    """
    Class to define login dialog
    """
    # ----------------------------------------------------------------------
    def __init__(self):
        """ Constructor """
        wx.Dialog.__init__(self, None, title="Login")

        # user info
        user_sizer = wx.BoxSizer(wx.HORIZONTAL)

        user_lbl = wx.StaticText(self, label="Username:")
        user_sizer.Add(user_lbl, 0, wx.ALL | wx.CENTER, 5)
        self.user = wx.TextCtrl(self)
        user_sizer.Add(self.user, 0, wx.ALL, 5)

        # pass info
        p_sizer = wx.BoxSizer(wx.HORIZONTAL)

        p_lbl = wx.StaticText(self, label="Password:")
        p_sizer.Add(p_lbl, 0, wx.ALL | wx.CENTER, 5)
        self.password = wx.TextCtrl(self, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        p_sizer.Add(self.password, 0, wx.ALL, 5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(user_sizer, 0, wx.ALL, 5)
        main_sizer.Add(p_sizer, 0, wx.ALL, 5)

        btn = wx.Button(self, label="Login")
        btn.SetDefault()
        btn.Bind(wx.EVT_BUTTON, self.onLogin)
        main_sizer.Add(btn, 0, wx.ALL | wx.CENTER, 5)

        exitbtn = wx.Button(self, label="Exit")
        exitbtn.Bind(wx.EVT_BUTTON, self.onExit)
        main_sizer.Add(exitbtn, 0, wx.ALL, 5)

        self.SetSizer(main_sizer)

        # Adds Icon image to window
        icon = wx.Icon('Images\icon.ico', wx.BITMAP_TYPE_ICO, 32, 32)
        wx.Frame.SetIcon(self, icon)

    # ----------------------------------------------------------------------
    def onLogin(self, event):
        """
        Check credentials and login
        """

        user_password = self.password.GetValue()
        user_username = self.user.GetValue()

        login = functions.login(user_username, user_password)
        global client
        client = login[1]

        if login[0]:
            self.Destroy()
        else:
            print("Username or password is incorrect!")

    # ----------------------------------------------------------------------
    def onExit(self, event):
        self.Destroy()

########################################################################
class MyPanel(wx.Panel):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)


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


########################################################################
class MainFrame(wx.Frame):
    """ Main Frame that dialogs are launched from """
    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Main App")
        panel = MyPanel(self)

        # Ask user to login
        dlg = LoginDialog()
        dlg.ShowModal()

        dlg = MessageDialog()
        dlg.ShowModal()

        return

    # ----------------------------------------------------------------------
    def myListener(self, message, arg2=None):
        """
        Show the frame
        """
        self.Show()

    # ----------------------------------------------------------------------

