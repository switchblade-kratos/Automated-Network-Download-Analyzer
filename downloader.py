import socket
import ssl
import time

def download_file(host, port, path):
    # Create TCP connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    # Wrap with SSL (HTTPS)
    context = ssl.create_default_context()
    secure_sock = context.wrap_socket(sock, server_hostname=host)

    # Create HTTP GET request
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

    # Start time
    start_time = time.time()

    # Send request
    secure_sock.sendall(request.encode())

    # Receive data
    total_data = b""
    while True:
        data = secure_sock.recv(4096)
        if not data:
            break
        total_data += data

    # End time
    end_time = time.time()
    secure_sock.close()

    # Remove HTTP headers
    header_end = total_data.find(b"\r\n\r\n") + 4
    body = total_data[header_end:]

    # Calculate metrics
    file_size = len(body)
    time_taken = end_time - start_time
    speed = file_size / time_taken if time_taken > 0 else 0

    return file_size, time_taken, speed