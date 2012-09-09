# the def of an item object. any values needed for a specific item can be 
# added after object creation, these are the basics for a VANILLA item.
#
# weight -> also so far. used to determine the amount of space it will
# take up in my inventory
#
# desc -> what to say when running EXAMINE [object] (a small knife)
#
# yell -> what to say when running LOOK in a room (there is a knife here)
# 
# contents -> used only for items like boxes and wallets
class item:
	def __init__(self, kind, weight, desc, yell, contents):
		self.kind = kind
		self.weight = weight
		self.desc = desc
		self.yell = yell
		self.contents = contents

# Ok, so this defines a room object. args are pretty self-explanatory, just for
# my own benefit:
# When creating the first room, all border args must be set as None
# (obviously, since there are no other rooms). 
#
# Each border arg is another room object. 
#
# name and desc are both string values.
#
# items is a list (defined there, not a list object, that would be too much
# work for me :)

class room:
	def __init__(self, name,  desc, items):
		self.name = name
		self.nb = None
		self.sb = None
		self.eb = None
		self.wb = None
		self.db = None
		self.ub = None
		self.neb = None
		self.swb = None
		self.nwb = None
		self.seb = None
		self.desc = desc
		self.contents = items
		self.visited = False

class plyr:
	def __init__(self, inven, name, score, location):
		self.inven = inven
		self.name = name
		self.score = score
		self.location = location

	def look(self):
		print self.location.name + '\n' + self.location.desc + '\n'
		for x in self.location.contents:
			print x.yell + '\n'
	
	def examine(self, what):
		inRoom = False
		for x in self.location.contents:
			if x.kind == what:
				inRoom = True
				print x.desc
				break
			else:
				inRoom = False
				continue
		if not inRoom:
			for x in self.inven:
				if x.kind == what:
					here = True
					print x.desc
					break
				else:
					here = False
					continue
			if not here:
				print "I can't see that here!"


	def go(self, direction):
        	if direction == 'north' or direction == 'n':
        	        if self.location.nb == None:
				print "You can't go that way!"
			else:
				self.location = self.location.nb
        	elif direction == 'south' or direction == 's':
			if self.location.sb == None:
				print "You can't go that way!"
			else:
        	        	self.location = self.location.sb
        	elif direction == 'east' or direction == 'e':
        	        if self.location.eb == None:
				print "You can't go that way!"
			else:
				self.location = self.location.eb
        	elif direction == 'west' or direction == 'w':
        	        if self.location.wb == None:
				print "You can't go that way!"
			else:
				self.location = self.location.wb
        	elif direction == 'northeast' or direction == 'ne':
			if self.location.neb == None:
				print "You can't go that way!"
			else:
				self.location = self.location.neb
		elif direction == 'southeast' or direction == 'se':
			if self.location.seb == None:
				print "You can't go that way!"
			else:
				self.location = self.location.seb
		elif direction == 'northwest' or direction == 'nw':
			if self.location.nwb == None:
				print "You can't go that way!"
			else:
				self.location = self.location.nwb
		elif direction == 'southwest' or direction == 'sw':
			if self.location.swb == None:
				print "You can't go that way!"
			else:
				self.location = self.location.swb
		elif direction == 'up' or direction == 'u':
			if self.location.ub == None:
				print "You can't go that way!"
			else:
				self.location = self.location.ub
		elif direction == 'down' or direction == 'd':
			if self.location.db == None:
				print "You can't go that way!"
			else:
				self.location = self.location.db
		else:
			print "Where's that?"
        	
		if self.location.visited:
                	print "You're in " + self.location.name
        	else:
        	        self.location.visited = True
        	        self.look()

	def take(self, what):
		inRoom = False
		for x in self.location.contents:
			if x.kind == what:
				inRoom = True
				self.location.contents.remove(x)
				self.inven.append(x)
				print 'Taken.'
				break
			else:
				inRoom = False
				continue
		if not inRoom:
			print "I can't see that here!"

	def drop(self, what):
		if len(self.inven) == 0:
			print 'You have nothing to drop!'
		else:
			for x in self.inven:
				if x.kind == what:
					onHand = True
					self.inven.remove(x)
					self.location.contents.append(x)
					print 'Dropped.'
					break
				else:
					onHand = False
					continue
			if onHand == False:
				print "You aren't holding that!"
	def showInven(self):
		if len(self.inven) == 0:
			print "You aren't holding anything."
		else:
			print 'You are carrying:\n'
			for x in self.inven:
				print x.kind

def doIntro(player):
	player.look()
	player.location.visited = True

def getInput(player):
	userin = raw_input('> ').lower().split(' ')
	parseInput(userin, player)

# TODO find a better way to do this!
def parseInput(userin, player):
# case 1 - no command sent
	if userin[0] == '':
		print 'Did you hear something?'
# case 2 - directions
	elif userin[0] == 'go':
		player.go(userin[1])
	elif userin[0] == 'n' or userin[0] == 's' or userin[0] == 'e' or userin[0] == 'w' or userin[0] == 'ne' or userin[0] == 'nw' or userin[0] == 'se' or userin[0] == 'sw' or userin[0] == 'd' or userin[0] == 'u':
		player.go(userin[0])
# case 3 - look
	elif userin[0] == 'look':
		player.look()
# case 4 - examine
	elif userin [0] == 'examine' or userin[0] == 'x':
		player.examine(userin[1])
# case 5 - get/take
	elif userin [0] == 'get' or userin[0] == 'take':
		player.take(userin[1])
# case 6 - drop/throw
	elif userin[0] == 'drop' or userin[0] == 'throw':
		player.drop(userin[1])
# case 7 - quit
	elif userin[0] == 'quit':
		if raw_input('Are you sure? (y/n) ').lower() == 'y':
			quit()
		else:
			print 'Ok.'
# case 8 - inven/inventory
	elif userin[0] == 'inventory' or userin[0] == 'inven':
		player.showInven()
	elif userin[0] == 'help':
		print 'I can do that too. Help! Help! HELP!!! See?'
	else:
		print 'And how do you suppose I do that?'
