#!/usr/bin/env python3

import sys
import re
import subprocess

logFail = "getFailedLog"
file_to_check = "test1"
output_file = "ips.txt"



# Open the output file in write mode to overwrite the previous contents
with open(output_file, "w") as output_file_obj:
    output_file_obj.truncate(0)
    # Open the input file in read mode
    with open(file_to_check, "r") as input_file:
        recent_ips = [""] * 3
        for line in input_file:
            ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)

            if ip_match:
                ip = ip_match.group()

                # Update the recent IPs list with the current IP
                recent_ips.pop(0)
                recent_ips.append(ip)

                # Check if we have three consecutive lines with the same IP
                if all(ip == recent_ips[0] for ip in recent_ips):
                    # Write the matched IP to the output file
                    output_file_obj.write(ip + "\n")

                    # Reset the recent IPs list to start from the first different IP
                    recent_ips = [ip, "", ""]
                else:
                # Reset the recent IPs list to start from the current line
                    output_file_obj.write("--"+ip + "\n")
                    #output_file_obj.write("---\n")
                    recent_ips = ["", "", ""]

