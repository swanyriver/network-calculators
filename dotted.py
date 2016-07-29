def decFromBin(binSt):
	out = 0
	mask = 1
	for c in reversed(binSt):
		if c == "1": out += mask
		mask *= 2
	return out

ipBin = raw_input().strip()
print ".".join(str(decFromBin(byte)) for byte in ipBin.split() )