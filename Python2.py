import socket
import argparse
import threading


def connection_scan():
    target_ip = input("Please provide the IP Address: ")
    target_port = int(input("Please provide the port: "))
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        s.send(b'Banner query\r\n')
        results = s.recv(100)
        print("[+] {}/tcp open".format(target_port))
        print("[+] {}".format(str(results)))
    except OSError:
        print("[-] {}/tcp closed".format(target_port))
    finally:
        s.close()


def port_scan():
    target = input("Enter the target: ")
    port_num = input("Please provide the port number: ")
    try:
        target_ip = socket.gethostbyname(target)
    except OSError:
        print("[^] Cannot resolve {}".format(target))
        return

    try:
        target_name = socket.gethostbyaddr(target_ip)
        print("[*] Scan results for {}".format(target_name[0]))
    except OSError:
        print("[*] Scan results for {}".format(target_ip))

    t = threading.Thread(target=connection_scan, args=(target, int(port_num)))
    t.start()


def argument_parser():
    parser = argparse.ArgumentParser(description="TCP port scanner")
    parser.add_argument("-o", "--host", nargs="?", help="Host IP Address")
    parser.add_argument("-p", "--ports", nargs="?", help="Comma-separated port list")


num = int(input("Enter the function to run: "))
if num == 1:
    connection_scan()
elif num == 2:
    port_scan()
