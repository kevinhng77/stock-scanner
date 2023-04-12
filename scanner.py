import json
import os
from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
import datetime, time
from datetime import datetime
import socket

def proxy_server(host, port, dest_host, dest_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Proxy server listening on {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Received connection from {client_address[0]}:{client_address[1]}")
        proxies = {
        'http': 'http://localhost:8888',
        'https': 'https://localhost:8888'
        }

        remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote_socket.connect((dest_host, dest_port))

        client_request = client_socket.recv(4096)
        remote_socket.sendall(client_request)

        remote_response = remote_socket.recv(4096)
        client_socket.sendall(remote_response)

        client_socket.close()
        remote_socket.close()

# if __name__ == '__main__':
#     proxy_server('localhost', 8888, 'localhost', 8889)

def callNow():
        account_sid = "AC0dcd3d24de7ea7b04a8174dc18e22179"
        auth_token = "31ada64acedb8e0211fd9f9e2c5ffed6"
        client = Client(account_sid, auth_token)

        call = client.calls.create(
        url="http://demo.twilio.com/docs/voice.xml",
        to="+14152603133",
        from_="+18449292123"
        )

        print(call.sid)


try:

        url= 'https://www.investing.com/equities/pre-market'
        now = datetime.now()
        timeCompare = now.replace(hour=5, minute=30)
        r = requests.get(url, headers= {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        })
        print(r.text)
except Exception as e:
        print(e) 

# soup = BeautifulSoup(r.text)
# td_tags = soup.find_all('tr')
# print(td_tags)   
