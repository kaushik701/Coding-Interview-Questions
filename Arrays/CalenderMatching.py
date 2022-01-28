# O(c1+c2) time | O(c1+c2) space
def calenderMatching(calender1,dailyBounds1,calender2,dailyBounds2,meetingDuration):
	updatedCalender1 = updateCalender(calender1,dailyBounds1)
	updatedCalender2 = updateCalender(calender2,dailyBounds2)
	mergedCalender = mergeCalenders(updatedCalender1,updatedCalender2)
	flattenedCalender = flattenedCalender(mergedCalender)
	return getMatchingAvail(flattenedCalender,meetingDuration)

def updateCalender(calender,dailyBounds):
	updatedCalender = calender[:]
	updatedCalender.insert(0,['0:00',dailyBounds[0]])
	updatedCalender.append([dailyBounds[1],'23:59'])
	return list(map(lambda m: [timeToMinutes(m[0]),timeToMinutes(m[1])],updatedCalender))

def mergeCalenders(calender1,calender2):
	merged = []
	i,j = 0,0
	while i < len(calender1) and j < len(calender2):
		meeting1,meeting2 = calender1[i],calender2[j]
		if meeting1[0] < meeting2[0]:
			merged.append(meeting1)
			i += 1
		else:
			merged.append(meeting2)
			j += 1
	while i < len(calender1):
		merged.append(meeting1)
		i += 1
	while j < len(calender2):
		merged.append(meeting2)
		j += 1
	return merged

def flattenedCalender(calender):
	flattened = [calender[0][:]]
	for i in range(1,len(calender)):
		currentMeeting = calender[i]
		previousMeeting = flattened[-1]
		currentStart,currentEnd = currentMeeting
		previousStart,previousEnd = previousMeeting
		if previousEnd >= currentStart:
			newPreviousMeeting = [previousStart,max(previousEnd,currentEnd)]
			flattened[-1] = newPreviousMeeting
		else:
			flattened.append(currentMeeting[:])
	return flattened

def getMatchingAvail(calender,meetingDuration):
	matchingAvailabilities = []
	for i in range(1 ,len(calender)):
		start = calender[i-1][1]
		end = calender[i][0]
		if availabilityDuration >= meetingDuration:
			matchingAvailabilities.append([start,end])
	return list(map(lambda m: [minutesToTime(m[0]),minutesToTime(m[1])],updatedCalender))

def timeToMinutes(time):
	hours,minutes = list(map(int,time.split(':')))
	return hours * 60 + minutes

def minutesToTime(minutes):
	hours = minutes // 60
	mins = minutes % 60
	hoursString = str(hours)
	minutesString = '0' + str(mins) if mins < 10 else str(mins)
	return hoursString + ':' + minutesString