
from vidstream import AudioSender, AudioReceiver, ScreenShareClient, CameraClient, StreamingServer
from vidstream import VideoClient

import tkinter as tk

import socket
import threading


_local_ip_address = socket.gethostbyname(socket.gethostname())

# import requests
# _public_ip_address = requests.get('https://api.ipify.org').text


# In local area network [using the same wifi]
#   - All clients need to know each other's local ip addresses
#   - Each client will host on its local address and connect to the
#     others'

# On the open internet
#   - All clients connect to each others public ip address
#   - All clients host on their private ip addresses
# listening_PORT = 9999 |-> Should be different for each script
# Streaming_PORT = 9999 |-> Should be different for each script
# Server = StreamingServer(_local_ip_address, streaming_PORT)
# Client = CameraClient(_public_ip_address, listening_PORT)


streaming_PORT = 7777
Server = StreamingServer(_local_ip_address, streaming_PORT)

listening_PORT = 6666
receiver = AudioReceiver(_local_ip_address, listening_PORT)

def start_listening():
    streaming_thread = threading.Thread(target=Server.start_server)
    receiving_thread = threading.Thread(target=receiver.start_server)
    streaming_thread.start()
    receiving_thread.start()

foreign_streaming_PORT = 9999
def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0, 'end-1c'), foreign_streaming_PORT)
#   ^
#   It is defined here so whenever the button is clicked we restart the Camera client connection
    camera_client_thread = threading.Thread(target=camera_client.start_stream)
    camera_client_thread.start()

def start_screen_sharing():
    screen_sharing_client = ScreenShareClient(text_target_ip.get(1.0, 'end-1c'), foreign_streaming_PORT)
#   ^
#   It is defined here so whenever the button is clicked we restart the Screen client connection
    screen_sharing_client_thread = threading.Thread(target=screen_sharing_client.start_stream)
    screen_sharing_client_thread.start()

def start_audio_stream():
    audio_sending_PORT = 8888
    audio_sender = AudioSender(text_target_ip.get(1.0, 'end-1c'), audio_sending_PORT)
#   ^
#   It is defined here so whenever the button is clicked we restart the Audio client connection
    audio_sending_thread = threading.Thread(target=audio_sender.start_stream)
    audio_sending_thread.start()


# GUI
window = tk.Tk()
window.title("Application v0.0.0 Alpha")
window.geometry("300x200")

label_target_ip = tk.Label(window, text="Target IP:")
label_target_ip.pack()

text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

btn_listen = tk.Button(window, text="Start Listening", width=50, command=start_listening)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text="Start Camera Stream", width=50, command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen = tk.Button(window, text="Start Screen Sharing", width=50, command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio = tk.Button(window, text="Start Audio Stream", width=50, command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()