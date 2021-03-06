import socket
import argparse
import threading


def connection_scan():
    target_ip = input("Please provide the IP Address: ")
    target_port = [20, 21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443, 8080, 8181, 318]
    for port in target_port:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, port))
            s.send(b'Banner query\r\n')
            results = s.recv(100)
            print("[+] {}/tcp open".format(port))
            print("[+] {}".format(str(results)))
        except OSError:
            print("[-] {}/tcp closed".format(port))
        finally:
            s.close()


def port_scan():
    target = input("Enter the target: ")
    port_num = [20, 21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443, 8080, 8181, 318]
    for x in port_num:
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

        t = threading.Thread(target=connection_scan, args=(target, int(x)))
        t.start()


def argument_parser():
    parser = argparse.ArgumentParser(description="TCP port scanner")
    parser.add_argument("-o", "--host", nargs="?", help="Host IP Address")
    parser.add_argument("-p", "--ports", nargs="?", help="Comma-separated port list")


def run():
    selections = [1, 2, 3, 4, 5]
    num = int(input("Select the module to run: "))

    def first():
        if num == 1:
            connection_scan()
        elif num == 2:
            port_scan()
        else:
            print("--Module does not exist!--")
    while num not in selections:
        num = int(input("Select a valid module (1-5): "))
    else:
        first()


run()
