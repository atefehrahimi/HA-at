file sample.ini include 3 sections , server(name IP) and ports(for check ports) and time(for delay time).

file lib.py include 3 functions : ping (for ping IP), telnet(for telnet), check_ports(for check which ports is open).


file main.py ,in this file import configparse and read config file and save server in variable hostname , ports in port_option, time in time_delay.
