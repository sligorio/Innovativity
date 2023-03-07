#!/usr/bin/env python3

import sys
import re
import smtplib
import subprocess

file_to_check = "test1"
email_to_notify = "s.ligorio@innovativity.it"
# Construct the command to send the email
#sendMailCommand = f"echo '{body}' | mail -s '{subject}' {recipient}"
#ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
#ip_addresses = re.findall(ip_pattern, filetocheck)

#where i'll store 3 consecutive ip
recent_ips = ["","",""]

#open file to read
with open(file_to_check, "r") as f:
    for line in f:
        ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        
        if ip_match:
            ip = ip_match.group()

            # Update the recent IPs list with the current IP
            recent_ips.pop(0) #clear first position of list
            recent_ips.append(ip)#insert ip in the first free position

            # Check if we have three consecutive lines with the same IP
            if all(ip == recent_ips[0] for ip in recent_ips):
                # Send an email using the subprocess module
                 # Write the matched IP to the output file
                    output.write(ip + "\n")


                # Reset the recent IPs list to start from the first different IP
                recent_ips = [ip, "", ""]
            else:
                # Reset the recent IPs list to start from the current line
                recent_ips = ["", "", ""]    
