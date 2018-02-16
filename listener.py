from fbchat import Client
import config
import messenger


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
            message = message_object.author + ": " + message_object.text + '\n'
            print(message)
            config.messagesBox.Value += message
