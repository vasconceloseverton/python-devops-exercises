import socket

def check_port(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        return result == 0
