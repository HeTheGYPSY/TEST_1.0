import socket
try:
    device = str(input("Enter the device under scrutiny: "))
    print(socket.gethostbyname(device))
except Exception as err_msg:
    print(err_msg)
finally:
    print("----------First Execution complete!----------")
    try:
        address = input("Enter the IP Address: ")
        print(socket.gethostbyaddr(address))
    except Exception as err:
        print(err)
    finally:
        print("----------Second Execution complete!----------")
