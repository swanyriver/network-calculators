
samples = (0.088937536,
0.089684318,
0.090634622,
0.090677556,
0.090614918,
0.090602681)


samples = [17.5, 27.1, 17.1]
W = .4

EstimatedRTT = 38.4

for SampleRTT,i in zip(samples, range(1,len(samples)+1)):
	EstimatedRTT = ((1-W) * EstimatedRTT) + (W * SampleRTT)
	print "sample RTT num:%d = %f"%(i,SampleRTT)
	print "New Estimated RTT= (%f * %f) + (%f * %f)"%(1-W, EstimatedRTT, W, SampleRTT)
	print "segment num:%d EstimatedRTT: %f\n"%(i, EstimatedRTT)
