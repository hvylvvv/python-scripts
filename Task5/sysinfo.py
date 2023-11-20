'''
Python script that gets system information like distro info, 
memory(total, used, free), CPU info (model, core numbers, speed), current user, system load average, and IP address.

Uses arguments for specifying resources. (For example, -d for distro -m for memory, -c for CPU,
 -u for user info, -l for load average, -i for IP address).
'''
#######!/usr/bin/env python3

import os
import psutil
import platform
import socket
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--distro", action="store_true", help="Get distro info")
parser.add_argument("-m", "--memory", action="store_true", help="Get memory info")
parser.add_argument("-c", "--cpu", action="store_true", help="Get CPU info")
parser.add_argument("-u", "--user", action="store_true", help="Get current user info")
parser.add_argument("-l", "--load", action="store_true", help="Get system load average")
parser.add_argument("-i", "--ip", action="store_true", help="Get IP address")
args = parser.parse_args()

if args.distro:
    distro_info = platform.platform()
    print(f"Distro Info: {distro_info}")

if args.memory:
    memory_info = psutil.virtual_memory()
    print(f"Memory Info (Total: {memory_info.total}, Used: {memory_info.used}, Free: {memory_info.available})")

if args.cpu:
    cpu_info = f"Model: {platform.processor()}, Cores: {os.cpu_count()}, Speed: {psutil.cpu_freq().max} MHz"
    print(f"CPU Info: {cpu_info}")

if args.user:
    user_info = psutil.users()
    print(f"Current User Info: {user_info[0].name}")

if args.load:
    load_average = os.getloadavg()
    print(f"System Load Average: {load_average}")

if args.ip:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"IP Address: {ip_address}")
