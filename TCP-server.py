import socket
import threading

# target_host = '127.0.0.1'
# target_port = 80

IP = '127.0.0.1'
PORT = 80


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print('[*] Listening on {IP}:{PORT}'
          .format(IP=IP, PORT=PORT))

    while True:
        client, address = server.accept()
        print('[*] Accepted connection from {addressF}:{addressS}'
              .format(addressF=address[0], addressS=address[1]))

        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print('[*] Received: {data}'.format(data={request.decode("utf-8")}))
        sock.send(bytes('Hello from server!', encoding='UTF-8'))
        sock.close()


if __name__ == '__main__':
    main()
