from fbchat import Client


# Subclass of client to handle messages when they come in
class Listener(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)

        """
            message_object.text = contents of message
            message_object.mentions = array of all users mentioned?
            message_object.emoji_size = 
            message_object.sticker = fbchat.models.Sticker object
            message_object.attachments = 
        """
        if message_object.text is not None:
            print("message_object.text = ", message_object.text)
        if message_object.mentions is not None:
            print("message_object.mentions = ", message_object.mentions)
        if message_object.emoji_size is not None:
            print("message_object.emoji_size = ", message_object.emoji_size)()
        if message_object.sticker is not None:
            print("message_object.sticker = ", message_object.sticker)
        if message_object.attachments is not None:
            print("message_object.attachments = ", message_object.attachments)


pwd = input("Password: ")
client = Listener("sj-gallant@comcast.net", pwd)
client.listen()
