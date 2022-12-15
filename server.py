
from vidstream import AudioSender, AudioReceiver, ScreenShareClient, CameraClient, StreamingServer
from vidstream import VideoClient

import socket
import threading


class Server:

    localhost_ip_address = socket.gethostbyname(socket.gethostname())
    import requests
    public_ip_address = requests.get('https://api.ipify.org').text

    @staticmethod
    def broadcaster(streaming_PORT):
        return StreamingServer(Server.localhost_ip_address, streaming_PORT)

    @staticmethod
    def audio_receiver(listening_PORT):
        return AudioReceiver(Server.localhost_ip_address, listening_PORT)

    foreign_streaming_PORT = 7777
    foreign_audio_PORT = 6666
    destination_ip_address = localhost_ip_address

    @staticmethod
    def set_destination(destination):
        Server.destination_ip_address = destination

    @staticmethod
    def listen(streaming_PORT = 9999, listening_PORT = 8888):
        streaming_thread = threading.Thread(target=Server.broadcaster(streaming_PORT).start_server)
        receiving_thread = threading.Thread(target=Server.audio_receiver(listening_PORT).start_server)
        streaming_thread.start()
        receiving_thread.start()
    
    @staticmethod
    def stream_camera():
        camera_client = CameraClient(Server.destination_ip_address, Server.foreign_streaming_PORT)
    #   ^
    #   It is defined here so whenever the button is clicked we restart the Camera client connection
        camera_client_thread = threading.Thread(target=camera_client.start_stream)
        camera_client_thread.start()

    @staticmethod
    def stream_screen():
        screen_share_client = ScreenShareClient(Server.destination_ip_address, Server.foreign_streaming_PORT)
    #   ^
    #   It is defined here so whenever the button is clicked we restart the Screen client connection
        screen_share_client_thread = threading.Thread(target=screen_share_client.start_stream)
        screen_share_client_thread.start()
    
    @staticmethod
    def stream_audio():
        audio_broadcast_client = AudioSender(Server.destination_ip_address, Server.foreign_audio_PORT)
    #   ^
    #   It is defined here so whenever the button is clicked we restart the Audio client connection
        audio_broadcast_client_thread = threading.Thread(target=audio_broadcast_client.start_stream)
        audio_broadcast_client_thread.start()
