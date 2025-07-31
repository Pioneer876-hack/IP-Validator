# Import modules
import ipaddress
import time

# Use raw string for intro and assign to a variable
ip_intro = r"""
 ___ ___  __   __    _ _    _      _           
|_ _| _ \ \ \ / /_ _| (_)__| |__ _| |_ ___ _ _ 
 | ||  _/  \ V / _` | | / _` / _` |  _/ _ \ '_|
|___|_|     \_/\__,_|_|_\__,_\__,_|\__\___/_|  
"""
# Display intro to user
print(ip_intro)


# Time pause function
def timing():
    """Time pause before showing code"""
    time.sleep(1.0)


# IP Address Function
def ipaddress_ip():
    # Get IP address from user
    print("\nIP Address e.g. ➡️ 192.168.0.1")

    # Call time function
    timing()

    enter_ip = input("\nEnter your IP address ➡️ ")
    try:
        # Pass IP address
        private_ip = ipaddress.ip_address(enter_ip)
        timing()
        print(f"\nYour {private_ip} IP address is valid ✅")

    except ValueError:
        print("\nEntered IP address is incorrect ❌")


while ipaddress_ip:
    # Call function
    ipaddress_ip()

    # Call time function
    timing()

    # Ask user if they want to quit
    quit_user = input("\nWould you like to quit? Y/y or N/n 👀: ").capitalize()
    if quit_user == 'Y':
        print("\nThank you for using IP Validator! 🤖")
        break
    continue
