
import sys

#acks = [ int(line.split("Ack=")[1].split()[0] for line in sys.stdin.read() ]


# prefixes = {
# 	"10011110 00011110 10001111":0,
# 	"10011110 00011110 10001111 000":1,
# 	"10011110 00011110 10001111 01":2,
# 	"10011110 00011110 10001110 0001":3,
# 	"":4
# }

# prefixes = {
# "10011110 00011110 10001111": 	0,
# "10011110 00011110 10001111 000":	1,
# "10011110 00011110 10001111 01":	2,
# "10011110 00011110 10001110 0001": 	3,
# "":	4}


# ip = "158.30.142.90"
# ip = "158.30.142.30"

prefixes = {}

lines = []

while True:
	line = raw_input()
	if not line: break
	pre, outRoute = line.split('\t')
	prefixes[pre.strip()] = outRoute.strip()

prefixes[""] = "4"
print [(repr(k), repr(v)) for k,v in prefixes.items()]
print ""

ip = raw_input()

rout = " ".join((format(int(x), "08b") for x in ip.split(".")))
print ip, " = ", rout

#print list((k for k in prefixes.keys() if k in rout))

lonPref = max((k for k in prefixes.keys() if k in rout), key=len)
print "longest prefix:"
print lonPref
print rout

print "\nRoute:", prefixes[lonPref]