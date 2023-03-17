
import tkinter as tk

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

from Server import Server

def start_listening():
    connection()
    exit()

# GUI
import customtkinter
from GUI import GUI


def login():
    GUI.init(dimensions=(500, 350))
    frame = GUI.attach(customtkinter.CTkFrame, master=GUI.instance)._with(pady=20, padx=60, fill="both", expand=True)

    _label = GUI.attach(customtkinter.CTkLabel, master=frame, text="Login")._with(pady=12, padx=10)

    _username = GUI.attach(customtkinter.CTkEntry, master=frame, placeholder_text="Username")._with(pady=12, padx=10)
    _password = GUI.attach(customtkinter.CTkEntry, master=frame, placeholder_text="Password", show="*")._with(pady=12, padx=10)

    def handle_login():
        GUI.instance.destroy()
        #TODO: Actually Implement login logic
        connect()

    _button = GUI.attach(customtkinter.CTkButton, master=frame, text="Login", command=handle_login)._with(pady=12, padx=10)
    _checkbox = GUI.attach(customtkinter.CTkCheckBox, master=frame, text="Remember Me")._with(pady=12, padx=10)
    GUI.run()

def connect():
    GUI.init(dimensions=(300, 200))
    frame = GUI.attach(customtkinter.CTkFrame, master=GUI.instance)._with(pady=20, padx=60, fill="both", expand=True)

    _label = GUI.attach(customtkinter.CTkLabel, master=frame, text="Input Target IP")._with(pady=6, padx=10)
    
    global target_IP
    target_IP = GUI.attach(customtkinter.CTkEntry, master=frame, placeholder_text= "        IP Address", height=1)._with(pady=6, padx=10)
    btn_listen = GUI.attach(customtkinter.CTkButton, master=frame, text="Connect", command=start_listening)._with(anchor=tk.N, pady=6, padx=10)
    
    GUI.run()

def connection():
    # GUI.instance.destroy()
    if target_IP.get() != '':
        #TODO: Perform more checks to see if IP is valid and within usable range
        Server.set_destination(target_IP.get())

    Server.listen()

    GUI.init(dimensions=(300, 150))
    frame = GUI.attach(customtkinter.CTkFrame, master=GUI.instance)._with(pady=15, padx=60, fill="both", expand=True)
    
    btn_camera = GUI.attach(customtkinter.CTkButton, master=frame, text="Start Camera Stream", command=Server.stream_camera)._with(anchor=tk.N, pady=6, padx=10)
    btn_screen = GUI.attach(customtkinter.CTkButton, master=frame, text="Start Screen Sharing", command=Server.stream_screen)._with(anchor=tk.N, pady=6, padx=10)
    btn_audio = GUI.attach(customtkinter.CTkButton, master=frame, text="Start Audio Stream", command=Server.stream_audio)._with(anchor=tk.N, pady=6, padx=10)

    GUI.run()


if __name__ == "__main__":
    login()