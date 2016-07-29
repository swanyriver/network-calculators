
ipDot = raw_input().strip().split('.')
print ipDot

binIP = " ".join(str(format(int(byte), '08b')) for byte in ipDot )
print binIP

answer = ""
while not answer:
	answer = raw_input().strip()

print "matches" if binIP == answer else "doesnt match" 