
# README

## In local area network [using the same wifi]
- All clients need to know each other's local ip addresses
- Each client will host on its local address and connect to the others'

## On the open internet
- All clients connect to each others public ip address
- All clients host on their private ip addresses

    import requests
    _public_ip_address = requests.get(\'https://api.ipify.org').text

    Server = StreamingServer(_local_ip_address, streaming_PORT)
    Client = CameraClient(_public_ip_address, listening_PORT)


listening_PORT = 9999 |-> Should be different for each script

Streaming_PORT = 8888 |-> Should be different for each script [^footnote]
[^footnote]: The ports should be flipped if communicating with each other

-----
## To Run

`py application.py`
- if you want to test by connecting to yourself
    `py other.py`

---
## Find Target IP address
You can test it by using your local ipv4 address to connect to 
yourself

If you do not know how to just press connect the script will 
connect to your address automatically

If you want to test the connection between two machines

- Open your command line or powershell
- [on Windows]
    `ipconfig`
    `#Look for the ipv4 address`
- [on Linux]
    `ifconfig`
    `#Look for INET address`