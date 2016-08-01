import subprocess

p = subprocess.Popen('java -jar /usr/share/java/checkstyle-7.0-all.jar -c /google_checks.xml Test/unitTest.java Test/arith.java', shell=True,
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE)

ph_ret = p.wait()
ph_out, ph_err = p.communicate()

warning = 0
l = ph_out.split('\n')
for x in l:
	if x[:6] == '[WARN]':
		warning += 1

print warning
