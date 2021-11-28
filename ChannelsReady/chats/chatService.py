from channels.generic.websocket import WebsocketConsumer

socket_list = []

class ChatService(WebsocketConsumer):
    # connect
    def connect(self):
        self.accept()
        socket_list.append(self)
        pass

    # receive
    def receive(self, text_data=None, bytes_data=None):
        print(text_data)
        for ws in socket_list:
            ws.send(text_data)
        pass

    # disconnect
    def disconnect(self, code):
        pass
