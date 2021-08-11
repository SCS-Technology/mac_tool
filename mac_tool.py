#!/usr/bin/env python

# Python code to demonstrate
# conversion of a hex string
# to the binary string

import argparse, requests

parser = argparse.ArgumentParser(description="Test MAC Address for U/L bit")
parser.add_argument("address", metavar="address", type=str, help="MAC address to test")

args = parser.parse_args()
# Initialising hex string
if not args.address:
    print("type something")
    target_byte = args.address[0:2]

def get_vendor_id(mac):
    # check online for mac vendor
    url = f"https://api.macvendors.com/{mac}"
    re = requests.get(url)
    return re.text


def hex_to_bin(data):
    
    scale = 16
    res = bin(int(data, scale))[2:].zfill(8)
    return res


# Printing initial string
print(f"Most significant byte of address {args.address} is:", target_byte)

# Code to convert hex to binary
res = hex_to_bin(target_byte)

# Print the resultant string
print("Binary value is", str(res))

if str(res)[-2] == "1":
    print("U/L bit is set (1), mac is local")
    print("Cannot look this up, it's likely randomly generated")
else:
    print("U/L bit is not set (0), mac is global")
    vendor = get_vendor_id(args.address)
    print(f"Vendor is {vendor}")

