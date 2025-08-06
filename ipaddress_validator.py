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
    time.sleep(0.7)


# IP Address Function
def ipaddress_ip():
    # Get IP address from user
    print("""\nIPv4 Address e.g. ➡️  192.168.0.1 or 192.168.0.0/24
IPv6 Address e.g. ➡️  2001:0db8:85a3:0000:0000:8a2e:0370:7334 or 2001:db8:abcd:0012::/64""")

    # Call time function
    timing()

    # Get IP address
    enter_ip = input("\nEnter your IP address ➡️  ")
    try:
        # Pass IP address
        private_ip = ipaddress.ip_address(enter_ip)
        timing()
        print(f"\nYour {private_ip} IP address is valid ✅")

    except ValueError:
        try:
            # Try IP address with network prefix
            private_ip = ipaddress.ip_network(enter_ip, strict=False)
            timing()

            # Display IP and netmask to user
            print(f"\nYour {private_ip} IP address is valid ✅")
            print(f"\nYour subnet mask is {private_ip.netmask}")

            # Display usable hosts
            for host in private_ip.hosts():
                print(f"\nUsable IP addresses ➡️  {host}")
                print("----------------------------------------")

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
