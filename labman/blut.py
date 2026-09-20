import socket

# ESP32 Bluetooth MAC address
MAC_ADDRESS = "00:70:07:1A:08:CA"
PORT = 1  # Standard RFCOMM channel for ESP32 Bluetooth Serial

print(f"Connecting to {MAC_ADDRESS}...")

# Open a raw user-space Bluetooth RFCOMM socket
sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

try:
    sock.connect((MAC_ADDRESS, PORT))
    print("Connected! Streaming data to labmin.zip...")

    with open("labmin.zip", "wb") as f:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            f.write(data)

    print("Transfer complete! File saved as labmin.zip.")

except Exception as e:
    print(f"Error connecting: {e}")

finally:
    sock.close()
