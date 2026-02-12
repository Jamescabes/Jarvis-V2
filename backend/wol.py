import socket
import struct

def send_wol_packet(mac_address: str):
    """
    Sends a Wake-on-LAN magic packet to the specified MAC address.
    """
    try:
        # Format MAC address
        if len(mac_address) == 12:
            pass
        elif len(mac_address) == 17:
            mac_address = mac_address.replace(mac_address[2], '')
        else:
            raise ValueError("Incorrect MAC address format")

        # Create magic packet
        data = bytes.fromhex('F' * 12 + mac_address * 16)
        
        # Send via UDP broadcast
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(data, ('255.255.255.255', 9))
        sock.close()
        return True
    except Exception as e:
        print(f"Error sending WOL packet: {e}")
        return False
