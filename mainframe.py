import wx
import functions
from login import LoginDialog
from messenger import MessageDialog
from fbchat import Client

if "2.8" in wx.version():
    import wx.lib.pubsub.setupkwargs
    from wx.lib.pubsub import pub
else:
    from wx.lib.pubsub import pub


########################################################################
class MyPanel(wx.Panel):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)


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

