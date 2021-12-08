import telnetlib
import sys
import re

host = "localhost"
port = "5554"

telnet = telnetlib.Telnet(host, port)

auth_token = sys.argv[1]

telnet.write(bytes("auth " + auth_token + "\n", 'utf-8'))

accel_point=[4,3,1]
telnet.write(bytes("sensor set acceleration {0}:{1}:{2}\n".format(accel_point[0],accel_point[1],accel_point[2]), 'utf-8'))
#result = telnet.read_until(b"OK", 10)
#print(result.decode("utf-8"))

telnet.write(bytes("sensor get acceleration\n", 'utf-8'))
result3 = telnet.read_until(b"acceleration = 4:3:1", 10)
print(result3.decode("utf-8"))