import socket
try:
    device = str(input("Enter the device under scrutiny: "))
    print(socket.gethostbyname(device))
except Exception as err_msg:
    print(err_msg)
finally:
    print("Execution complete!")
