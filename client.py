import socket


def send_message_to_server(msg):

    bytes_to_send = str.encode(msg)

    server_address_port = ("192.168.0.12", 20001)

    buffer_size = 1024

    # Create a UDP socket at client side

    udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Send to server using created UDP socket
    udp_client_socket.connect(server_address_port)
    udp_client_socket.sendto(bytes_to_send, server_address_port)

    msg_from_server = udp_client_socket.recvfrom(buffer_size)

    msg = "Message from Server {}".format(msg_from_server[0])

    handle_result(msg)


def handle_result(result):

    print(result)


if __name__ == "__main__":

    send_message_to_server("Hello!")
