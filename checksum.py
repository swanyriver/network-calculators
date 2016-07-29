import random

def ones_comp_add(num1,num2, size=16):
    MOD = 1 << size
    result = num1 + num2
    return result if result < MOD else (result+1) % MOD

def swapBytes(num):
    return ( (num & 0xFF) << 8 ) + (num >> 8)

def displaySegment(seg):
    i=0
    while i+1<len(seg):
        print format(seg[i], '04x') + ',' + format(seg[i+1], '04x')
        i+=2

def betterDisplaySegment(seg):
    for i in range(len(seg)):
        print format(seg[i] >> 8, '02x') + "," + format(seg[i] & 0xFF, '02x'),
        if i & 1: 
            print ""
        else: print ",",

displaySegment = betterDisplaySegment
print "small segment generated with first 16bits left as 0 for checksum:"
segmentLines = 5
segment = [random.randint(0, (1<<16)-1) for _ in range(2*segmentLines)]
segment[0] = 0
displaySegment(segment)

checksum= (~reduce(ones_comp_add, segment)) & 0xFFFF
print "\nsegment checksum (1s compliment of 1s compliment sum):", format(checksum, '04x'), "\n"

segment[0] = checksum
displaySegment(segment)
print "1's compliment sum of entire segment including checksum:", format(reduce(ones_comp_add, segment), '04x'), "\n"

segment = map(swapBytes, segment)
displaySegment(segment)
print "1s compliment sum of same segment in opposite endian:", format(reduce(ones_comp_add, segment), '04x'), "\n"
