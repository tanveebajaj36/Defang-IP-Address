def ip_address(address):
    new_address = ""
    split_address = address.split(".")
    seperator = "[.]"
    new_address = seperator.join(split_address)
    return new_address
ipaddress = ip_address("1.1.2.3")
print(ipaddress)