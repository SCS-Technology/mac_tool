#!/usr/bin/env python

# mac address checker, sends request to macvendors.com,
# checks U/L bit to see if the mac address has be altered to be
# locally significant vs globally.

# usage: ./mac_tool.py <address>

import argparse, requests

parser = argparse.ArgumentParser(description="Test MAC Address for U/L bit, also search MACvendors.com for vendor")
parser.add_argument("address", metavar="address", type=str, help="MAC address to test")

args = parser.parse_args()
# Initialising hex string
target_byte = args.address[0:2]

def get_vendor_id(MAC):
    # check online for MAC vendor
    url = f"https://api.MACvendors.com/{MAC}"
    re = requests.get(url)
    if re.status_code == 404:
        result = "Not Found"
    else:
        result = re.text
    return result


def hex_to_bin(data):
    
    scale = 16
    res = bin(int(data, scale))[2:].zfill(8)
    return res


# Printing initial string
print(f"Most significant byte of address {args.address} is:", target_byte)

# Code to convert hex to binary
res = hex_to_bin(target_byte)

# Print the resultant string
print("Binary value of this byte is:", str(res))

if str(res)[-2] == "1":
    print("U/L bit is set (1), MAC is local")
    print("Cannot look this up, it's likely randomly generated")
else:
    print("U/L bit is not set (0), MAC is global")
    vendor = get_vendor_id(args.address)
    print(f"Vendor: {vendor}")