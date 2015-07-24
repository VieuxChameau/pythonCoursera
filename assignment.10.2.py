def getHourFrom(hourMinuteSec):
	return hourMinuteSec.split(':')[0]


name = input("Enter file:")
if len(name) < 1:
	name = "mbox-short.txt"

handle = open(name)

countMailSendByHour = dict()
for line in handle:
	if line.startswith("From "):
		hour = getHourFrom(line.split()[5])
		countMailSendByHour[hour] = countMailSendByHour.get(hour, 0) + 1

for hour, count in sorted(countMailSendByHour.items(), key=lambda key_value: key_value[0]):
	print("%s %d" % (hour, count))
