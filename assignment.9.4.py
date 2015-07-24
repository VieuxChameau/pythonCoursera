def getMostProlificCommitter(countByMailSenders):
	largest = None
	mostProlificCommitter = None
	for mailSender, count in countByMailSenders.items():
		if largest is None or count > largest:
			largest = count
			mostProlificCommitter = mailSender
	return mostProlificCommitter


name = input("Enter file:")
if len(name) < 1:
	name = "mbox-short.txt"

handle = open(name)

countByMailSenders = dict()
for line in handle:
	if line.startswith("From "):
		mailSender = line.split()[1]
		countByMailSenders[mailSender] = countByMailSenders.get(mailSender, 0) + 1

mostProlificCommitter = getMostProlificCommitter(countByMailSenders)

print("%s %d" % (mostProlificCommitter, countByMailSenders[mostProlificCommitter]))
