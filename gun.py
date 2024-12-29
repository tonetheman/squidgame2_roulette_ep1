
import random
import logging

# shit stupid this is not in the damn docs
# some random garbage about numeric values
logging.basicConfig(level=logging.WARNING)

def round():
	# pick a bullet chamber 1-6
	chamber = random.randint(1,6)

	# pick a starting chamber
	start = random.randint(1,6)

	if start==chamber:
		return "dead"

	return "alive"

def simple_russian_roulette():
	# prob is 1/6 to die
	# prob is 5/6 to live
	alive_count = 0
	dead_count = 0
	count = 10000
	for i in range(count):
		res = round()
		if res=="alive":
			alive_count = alive_count + 1
		else:
			dead_count = dead_count + 1

	print("alive percent: ",alive_count/count)
	print("dead percent : ",dead_count/count)

class Gun:
	def __init__(self):
		self.current = 0
		self.chamber = 0
		self.firecount = 0
		logging.info("Gun created")
	def load(self):
		self.chamber = random.randint(1,6)
		self.current = random.randint(1,6)
		self.firecount = 0
		logging.info("Gun loaded {0} {1}".format(self.current, self.chamber))
	def fire(self):
		logging.info("Gun fired {0} {1}".format(self.current, self.chamber))
		# update the fire count no matter what
		self.firecount = self.firecount + 1

		# if the chamber is the same as the current chamber, then dead
		if self.chamber==self.current:
			return "dead"
		# we are still alive so move the current
		self.current = self.current + 1

		# if current goes over 6, then reset to 1
		# we will eventually die
		if self.current>6:
			self.current = 1

		return "alive"

def one_round():
	# get a gun
	gun = Gun()
	# load it
	gun.load()
	while True:
		# fire the gun
		res = gun.fire()
		# if we are dead, then break the game is over
		if res=="dead":
			break
		# otherwise we just keep going with the same gun
		# this ensures we will die eventually
	
	# return the number of fires it took to kill us
	return gun.firecount

def eventual_roulette():
	count = 1000
	totals = {}
	for i in range(count):
		res = one_round()
		if res in totals:
			totals[res] = totals[res] + 1
		else:
			totals[res] = 1

	# this is even at 1/6 probability
	for i in totals:
		print(i, totals[i])

	# around 1.67% chance of dying on any given round?
	print(100*totals[1]/count)

	print("in this game")
	print("the number of people who died on first round (round 1) {0}".format(totals[1]))
	print("the number of people who died on second round (round 2) {0}".format(totals[1]+totals[2]))
	print("the number of people who died on third round (round 3) {0}".format(totals[1]+totals[2]+totals[3]))
	print("usually around half of the people die on the third round")
	print("the number of people who died on fourth round (round 4) {0}".format(totals[1]+totals[2]+totals[3]+totals[4]))


# one_round()
eventual_roulette()
