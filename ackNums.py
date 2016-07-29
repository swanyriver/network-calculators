
import sys

#acks = [ int(line.split("Ack=")[1].split()[0] for line in sys.stdin.read() ]
acks = []
lines = sys.stdin.read().split('\n')

for line in lines:
	if "Ack=" in line:
		line = line.split("Ack=")[1].split()[0]
		acks.append(int(line))


print "%d\t\t%d\t\t%d"%(1, acks[0], acks[0])

for i in range(1, len(acks)):
	#print "%d\t\t%d\t\t%d"%(i, acks[i], acks[i]-acks[i-1])
	data = acks[i] - acks[i-1]
	print "%d\t\t%d\t\t%d\t\t%d"%(i, acks[i], data, data/2896 )



