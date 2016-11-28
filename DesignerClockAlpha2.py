"""
####################################################################################
#   The objective of this program is to emulate the output of a designer clock in  #
#   the python console.                                                            #
####################################################################################
"""
#----------------------------------------------------------------------------------#
# Imported Libraries

import datetime
import time
#----------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------#
#variables

currenttime = datetime.datetime.now()

nowhour = currenttime.hour
nowmin = currenttime.minute

#----------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------#
# this section prints off a blank 11 x 10 grid of underscores
TimeBoard = [["_"] * 11 for row in range(11)]

def clearboard():
	TimeBoard = [[" "] * 11 for row in range(11)]
	return TimeBoard


def printboard(board):
	for row in TimeBoard:
		print " ".join(row)


print "Before telling time"

printboard(TimeBoard)

print " "
#----------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------#
# This section has a list of letters to be used in the board.

timechar = [
["i", "t", "l", "i", "s", "b", "f", "a", "m", "p", "m"],
["a", "c", "q", "u", "a", "r", "t", "e", "r", "d", "c"],
["t", "w", "e", "n", "t", "y", "f", "i", "v", "e", "x"],
["h", "a", "l", "f", "b", "t", "e", "n", "f", "t", "o"],
["p", "a", "s", "t", "e", "r", "u", "n", "i", "n", "e"],
["o", "n", "e", "s", "i", "x", "t", "h", "r", "e", "e"],
["f", "o", "u", "r", "f", "i", "v", "e", "t", "w", "o"],
["e", "i", "g", "h", "t", "e", "l", "e", "v", "e", "n"],
["s", "e", "v", "e", "n", "t", "w", "e", "l", "v", "e"],
["t", "e", "n", "s", "e", "o", "c", "l", "o", "c", "k"]
]

#----------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------#
# Converts current time to a fun readable string
if nowmin >= 30:
	# This increases the hour, to adjust for the foresight of the strings e.g. 'quarter to' etc.
	nowhour +=1

if nowhour >= 13:
	# This little bit of code is to prevent the display of military time
	nowhour -= 12



def replaceempty(TBrow,TBslicestart,TBsliceend):
	TimeBoard[TBrow][TBslicestart : TBsliceend] = timechar[TBrow][TBslicestart : TBsliceend]	
	


def simplehour(hour):
	# Converting the hour, to a string
	print "After telling time:"
	clearboard()
	TimeBoard[0][0:2] = timechar[0][0:2]
	TimeBoard[0][3:5] = timechar[0][3:5]

	if hour == 1:
		replaceempty(5, 0, 3)
		return "one"
	elif hour == 2:
		replaceempty(6, 9, 11)
		return "two"
	elif hour == 3:
		replaceempty(5, 7, 11)
		return "three"
	elif hour == 4:
		replaceempty(6, 0, 5)
		return "four"
	elif hour == 5:
		replacempty(6, 5, 9)
		return "five"
	elif hour == 6:
		replaceempty(5, 4 ,7)
		return "six"
	elif hour == 7:
		replaceempty(8, 0, 5)
		return "seven"
	elif hour == 8:
		replaceempty(7, 0, 6)
		return "eight"
	elif hour == 9:
		replaceempty(4, 8, 12)
		return "nine"
	elif hour == 10:
		replaceempty(9, 0, 3)
		return "ten"
	elif hour == 11:
		replaceempty(7, 6, 12)
		return "eleven"
	elif hour == 12:
		replaceempty(8, 6, 12)
		return "twelve"
	else:
		return "hour time error"

def simpleminute(min):
	""" Converting the minutes, to strings.
	Note: that the minutes are NOT exact, 
	but will either be right on time, 
	or up to 5 minutes ahead of time"""

	if min >=(1) and min <(6):
		replaceempty(2, 6, 10)  #five
		replaceempty(4, 0, 4)  #past
		printboard(TimeBoard)
		return "five past"

	elif min >= (6) and min < (11):
		replaceempty(4, 5, 10)
		printboard(TimeBoard)
		return "ten past"

	elif min >= (11) and min < (16):
		replaceempty(1, 1, 1)  #a
		replaceempty(1, 3, 9)  #quarter
		replaceempty(4, 0, 4)  #past
		printboard(TimeBoard)
		return "a quarter past"

	elif min >= (16) and min < (21):
		replaceempty(2, 1, 7)  #twenty
		replaceempty(4, 0, 4)  #past
		printboard(TimeBoard)
		return "twenty past"

	elif min >= (21) and min < (26):
		replaceempty(2, 0, 10)  #twentyfive
		replaceempty(4, 0, 4)  #past
		printboard(TimeBoard)
		return "twentyfive past"

	elif min >= (26) and min < (31):
		replaceempty(3, 0, 4)  #half
		replaceempty(4, 0, 4)  #past
		printboard(TimeBoard)
		return "half past"

	elif min >= (31) and min < (36):
		replaceempty(2, 0, 10)  #twentyfive
		replaceempty(3, 10, 11)  #to
		printboard(TimeBoard)
		return "twentyfive to"

	elif min >= (36) and min < (41):
		replaceempty(2, 0, 6)
		replaceempty(3, 9, 11)
		printboard(TimeBoard)
		return "twenty to"

	elif min >= (41) and min < (46):
		replaceempty(1, 0, 1)
		replaceempty(1, 2, 9)
		replaceempty(4, 0, 5)
		printboard(TimeBoard)
		return "a quarter to"

	elif min >= (46) and min < (51):
		replaceempty(3, 5, 8)
		replaceempty(3, 9, 11)
		printboard(TimeBoard)
		return "ten to"

	elif min >= (51) and min < (56):
		replaceempty(2, 6, 10)
		replaceempty(3, 9, 11)
		printboard(TimeBoard)
		return "five to"

	elif min >= (56) and min < (60):
		printboard(TimeBoard)
		return ""

	else:
		printboard(TimeBoard)
		return "minute time error"


printhour = simplehour(nowhour)
printmin = simpleminute(nowmin)

'''
print " "
print "--------Bug Check----------"
print " "
print "Hour from currenttime: %s" % currenttime.hour
print "nowhour value is: %s" % nowhour
print "The String of the Hour: %s" % printhour
print " "

print "Minute from currenttime: %s" % currenttime.minute
print "nowmin value is: %s" % nowmin
print "The String of the Minute: %s" % printmin
print " "
print "------End Bug Check--------"
print " "

print "it is %s %s o'clock. " % (printmin, printhour)
print " "
'''
#----------------------------------------------------------------------------------#

