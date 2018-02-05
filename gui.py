import imp
appJar = imp.load_source("appJar", "Dependencies/appJar/appjar.py")
from appJar import gui


def press(button):
    if button == "Cancel":
        messengerApp.stop()
    else:
        usr = messengerApp.getEntry("Username")
        pwd = messengerApp.getEntry("Password")
        print("User:", usr, "Password:", pwd)


messengerApp = gui("Messenger")

messengerApp.addLabelEntry("Username")
messengerApp.addLabelSecretEntry("Password")

messengerApp.addButtons(["Submit", "Cancel"], press)

messengerApp.go()
