#!/usr/bin/env python3
import sys
import re
import subprocess

logFail = "getFailedLog"
file_to_check = "test1"
output_file= "ips.txt"
# Open the output file in write mode to overwrite the previous contents
with open(output_file, "w") as output_file_obj:
    # Open the input file in read mode
    with open(file_to_check, "r") as input_file:
        current_ip = None
        consecutive_count = 0
        for line in input_file:
            ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)

            if ip_match:
                ip = ip_match.group()

                # If this is the same IP as the last line, increment the count
                if ip == current_ip:
                    consecutive_count += 1
                # Otherwise, reset the count and update the current IP
                else:
                    current_ip = ip
                    consecutive_count = 1

                # Check if we have three or more consecutive lines with the same IP
                if consecutive_count >= 3:
                    
                    # Write the matched IP to the output file
                    output_file_obj.write(ip + "\n")

                    # Reset the consecutive count to start from the first different IP
                    while True:
                        next_line = input_file.readline()
                        next_ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", next_line)
                        if next_ip_match and next_ip_match.group() == ip:
                            continue
                        else:
                            current_ip = next_ip_match.group() if next_ip_match else None
                            consecutive_count = 1
                            break
