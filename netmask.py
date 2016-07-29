def getDotted(num):
	bs = []
	for i in range(4):
		bs.append(num % 2**8)
		num >>= 8
	return ".".join(str(n) for n in reversed(bs))


cidr = raw_input().strip().split(" /")
netlength = int(cidr[1])
ip = [int(byte) for byte in cidr[0].split(".")]

print ip, netlength

decIP = 0
for num in ip:
	decIP <<=8
	decIP += num

#print decIP, getDotted(decIP)
hostmask = (1 << (32-netlength)) - 1
netmask = (2**32 - 1) - hostmask

print "hostmask: ", format(hostmask, '032b')
print "netmask : ", format(netmask, '032b')

print "------------------------------------"

print "netMask: ", getDotted(netmask)
print "net address", getDotted(decIP & netmask)
print "hostMask: ", getDotted(hostmask)
print "broadcast: ", getDotted((decIP & netmask) + hostmask)
print "num possible hosts: ", 2**(32-netlength)-2
print "host number:", decIP & hostmask
