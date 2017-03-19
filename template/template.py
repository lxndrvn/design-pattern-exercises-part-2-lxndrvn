

class CodecoolPersonTemplate(object):
	def __init__(self, name):
		self.name = name

	def favourite_coffee(self):
		raise NotImplementedError

	def drink_coffee(self):
		print("{0} drinks a {1}".format(self.name, self.favourite_coffee()))

	def morning_job(self):
		raise NotImplementedError

	def do_morning_job(self):
		print("{0} is {1}".format(self.name, self.morning_job()))

	def lunch(self):
		print("{0} stuffs their face.").format(self.name)

	def afternoon_job(self):
		raise NotImplementedError

	def do_afternoon_job(self):
		print("{0} is {1}".format(self.name, self.afternoon_job()))

	def late_afternoon_routine(self):
		raise NotImplementedError

	def do_afternoon_routine(self):
		print("{0} is {1}".format(self.name, self.late_afternoon_routine()))

class Mentor(CodecoolPersonTemplate):
	def favourite_coffee(self):
		return "double espresso"

	def morning_job(self):
		return "helping"

	def afternoon_job(self):
		return "keeping private mentoring"

	def late_afternoon_routine(self):
		return "preparing for the future"

class Student(CodecoolPersonTemplate):
	def favourite_coffee(self):
		return "simple espresso"

	def morning_job(self):
		return "learning"

	def afternoon_job(self):
		return "having private mentoring"

	def late_afternoon_routine(self):
		return "playing foosball"

def main():
	mentors = [Mentor("Immi")]
	students = [Student("Fani")]
	codecoolers = mentors + students
	print("It's morning. Rituals are coming...")
	for c in codecoolers:
		c.drink_coffee()
	print("Here comes the real work!")
	for c in codecoolers:
		c.do_morning_job()
	print("Finally lunchtime")
	for c in codecoolers:
		c.lunch()
	print("Neverending story...")
	for c in codecoolers:
		c.do_afternoon_job()
	print("Some freetime")
	for c in codecoolers:
		c.do_afternoon_routine()

main()

