def locate():
    try:
        import geocoder
        from geopy.geocoders import Nominatim
        address = input("Enter the IP Address: ")
        geolocator = Nominatim(user_agent="geoapiExercises")
        ip = geocoder.ip(address)
        x = ip.latlng
        location = geolocator.reverse(f'{x[0]}, {x[1]}')
        print(f"{location}\n{x}")
    except Exception as err_msg:
        print(err_msg)
    finally:
        if not Exception:
            print("*|--Execution Completed!--|*")
        else:
            print("*|--Execution Failed--|*")


def web():
    try:
        from urllib.request import urlopen
        url = str(input("Enter the URL: "))
        page = urlopen(url)
        html_bytes = page.read()
        html_page = html_bytes.decode("UTF-8")
        print(html_page)
    except Exception as err_msg:
        print(err_msg)
    finally:
        if not Exception:
            print("*|--Execution Completed--|*")
        else:
            print("*|--Execution Failed--|*")


def run():
    selections = [1, 2, 3, 4, 5]
    num = int(input("Select the module to run: "))

    def first():
        if num == 1:
            locate()
        elif num == 2:
            web()
        else:
            print("--Module does not exist!--")
    while num not in selections:
        num = int(input("Select a valid module (1-5): "))
    else:
        first()
