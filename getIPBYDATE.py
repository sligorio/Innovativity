#!/usr/bin/env python3
import datetime
input_file = "test1"
output_file = "ipsDate.txt"
with open(input_file, "r") as f, open(output_file, "w") as out:
    out.truncate(0)
    last_login = {}
    ips_to_write = set()
    for line in f:
        data = line.strip().split()
        timestamp_str = " ".join(data[:3])
        ip = data[3]
        timestamp = datetime.datetime.strptime(timestamp_str, '%b %d %H:%M:%S')
        if ip in last_login:
            if (timestamp - last_login[ip]['time']).total_seconds() <= 120:
                last_login[ip]['count'] += 1
                if last_login[ip]['count'] >= 5:
                    ips_to_write.add(ip)
            else:
                if last_login[ip]['count'] >= 5:
                    ips_to_write.add(ip)
                last_login[ip] = {'time': timestamp, 'count': 1}
        else:
            last_login[ip] = {'time': timestamp, 'count': 1}
    for ip in ips_to_write:
        out.write(ip + '\n')

