import subprocess
import javacoverage
import junit

def getScore(**kwargs):
	p = subprocess.Popen("sh mv.sh && sh run.sh && java Test/unitTest", shell = True,
						stdout = subprocess.PIPE,
						stderr = subprocess.PIPE,
						**kwargs)
	ph_out, ph_err = p.communicate()
	#return ph_out
	print "ph_out : " + str(ph_out)
	return 100

def getCodeStyleResult(JavaFile):
	return open('codestyle', 'r').read()

def getSchemaResult():
	p = subprocess.Popen('java testSchema', shell=True,
		         stdout=subprocess.PIPE,
		         stderr=subprocess.PIPE)

	ph_ret = p.wait()
	ph_out, ph_err = p.communicate()
	return ph_out

def getUnitTestScore():
	return junit.singleFile()

def getCoverageResult(filename, classname):
	result = []

	for i in xrange(len(filename)):
		result.append(javacoverage.singleFile(filename[i], classname[i]))
	return result
