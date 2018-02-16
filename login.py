import wx
import functions
import config

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

        # Add buttons
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

        btn = wx.Button(self, label="Login")
        btn.SetDefault()
        btn.Bind(wx.EVT_BUTTON, self.onLogin)
        btn_sizer.Add(btn, 0, wx.ALL | wx.CENTER, 5)

        exitbtn = wx.Button(self, label="Exit")
        exitbtn.Bind(wx.EVT_BUTTON, self.onExit)
        btn_sizer.Add(exitbtn, 0, wx.ALL, 5)

        main_sizer.Add(btn_sizer)

        self.SetSizerAndFit(main_sizer)

        # Adds Icon image to window
        icon = wx.Icon('Images\icon.ico', wx.BITMAP_TYPE_ICO, 32, 32)
        wx.Frame.SetIcon(self, icon)

    # ----------------------------------------------------------------------
    def doNothing(self, event):
        return

    def onLogin(self, event):
        """
        Check credentials and login
        """

        user_password = self.password.GetValue()
        user_username = self.user.GetValue()

        login = functions.login(user_username, user_password)
        config.client = login[1]

        if login[0]:
            self.Destroy()
        else:
            print("Username or password is incorrect!")

    # ----------------------------------------------------------------------
    def onExit(self, event):
        self.Destroy()
