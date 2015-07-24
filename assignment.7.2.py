# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
nbLines = 0
sumSpam = 0
for line in fh:
	if not line.startswith("X-DSPAM-Confidence:"):
		continue
	pos = line.find('.')
	sumSpam += float(line[pos - 1:])
	nbLines += 1

averageSpam = (sumSpam / nbLines)
print("Average spam confidence:", averageSpam)
