#!/bin/bash

# Set variables for the email
recipient="s.ligorio@innovativity.it"
subjectDate="Alert: more then 5 failed login in less then 2 minutes, IP BLOCKED"
subject="Alert: 3 failed log in a row"
body=""

    # Loop through the file and send an email for every 3 failed login attempts
   
    while read line; do
            # Set the body of the email to the current line
             body="$line"

                    # Send the email
                       echo "this IP: $body failed to log 3 times in a row" | mail -s "$subject" "$recipient"
                done < ips.txt

    while read line; do
            # Set the body of the email to the current line
                body="$line"
                    #
		    #
		    #
		    #
		    #insert if case that if the ip is already in the iptables it doesnt resend the mail and block it
 		    # Send the email
		
		   if ! iptables -L INPUT -v -n | grep -q "$line"; then
		 	echo "this IP: $body failed to log more then 5 times in less then 2 minutes" | mail -s "$subjectDate" "$recipient"
     # Block the IP using iptables
                        ip=$(echo "$line" | awk '{print $1}')
                        iptables -A INPUT -s "$ip" -j DROP
		   fi
    		done < ipsDate.txt
