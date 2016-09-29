import csv

class scoresData(object):
	def __init__(self, path):
		self.scores = {'Code Style':'', 'Coverage Rate':'', 'Unittest Score':'', 'Scheme Score':'', 'Black Box':''}
		self.path = path

	def saveCodeStyle(self, codestyle):
		self.scores['Code Style'] = codestyle

	def saveCoverage(self, coverage):
		self.scores['Coverage Rate'] = coverage

	def saveUnittest(self, unittest):
		self.scores['Unittest Score'] = unittest

	def saveScheme(self, scheme):
		self.scores['Scheme Score'] = scheme

	def saveBlackBox(self, blackbox):
		self.scores['Black Box'] = blackbox

	def save(self):
		'''with open(self.path, 'w') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=' ',
		                    quotechar=' ', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow(['Code Style', 'Coverage Rate', 'Unittest Score', 'Scheme Score', 'Black Box'])
			spamwriter.writerow(self.scores)'''
		with open(self.path, 'w') as csvfile:
			scorenames = ['Code Style', 'Coverage Rate', 'Unittest Score', 'Scheme Score', 'Black Box']
			writer = csv.DictWriter(csvfile, fieldnames=scorenames)

			writer.writeheader()
			writer.writerow(self.scores)

		print self.scores

