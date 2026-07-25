import socket
import threading
from datetime import datetime

print("=" * 50)
print("Simple Python Port Scanner")
print("=" * 50)

target = input("Enter Target IP or Website: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid Host")
    exit()

print(f"\nScanning Target: {target_ip}")
print(f"Started at: {datetime.now()}")
print("-" * 50)


def scan_port(port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    result = scanner.connect_ex((target_ip, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    scanner.close()


for port in range(1, 1025):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()