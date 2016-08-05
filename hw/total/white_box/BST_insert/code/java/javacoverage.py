from bs4 import BeautifulSoup
import sys

def singleFile(filename, classname):
	paras = {}
	
	paras['filename'] = filename
	filename = 'coverage/report/jacoco/default/' + filename + '.html'

	html_doc = open(filename, 'r').read()
	soup = BeautifulSoup(html_doc, 'lxml')
	css_class = soup.find(class_ = "source lang-java linenums")
	fc = css_class.find_all(class_ = "fc")
	fc = [x.get_text().rstrip() for x in fc if x.get_text().rstrip() != '']
	nc = css_class.find_all(class_ = "nc")
	nc = [x.get_text().rstrip() for x in nc if x.get_text().rstrip() != '']
	lines = css_class.get_text().split('\n')
	lines = [x.rstrip() for x in lines if x.rstrip() != '']

	stmt_text = []
	for x in lines:
		if x in nc:
			stmt_text.append('- %s'%x)
		elif x in fc:
			stmt_text.append('+ %s'%x)
		else:
			stmt_text.append('  %s'%x)
	stmt_text = '\n'.join(stmt_text)

	paras['stmt_text'] = stmt_text

	bfc = css_class.find_all(class_ = "bfc")
	bfc = [x.get_text().rstrip() for x in bfc if x.get_text().rstrip() != '']
	bpc = css_class.find_all(class_ = "bpc")
	bpc = [x.get_text().rstrip() for x in bpc if x.get_text().rstrip() != '']
	lines = css_class.get_text().split('\n')
	lines = [x.rstrip() for x in lines if x.rstrip() != '']

	branch_text = []
	for x in lines:
		if x in bpc:
			branch_text.append('- %s'%x)
		elif x in bfc:
			branch_text.append('+ %s'%x)
		else:
			branch_text.append('  %s'%x)
	branch_text = '\n'.join(branch_text)

	paras['branch_text'] = branch_text

	s = open('coverage/report/jacoco/report.csv', 'r').readlines()[1:]

	for x in s:
		x = x.split(',')
		if x[2] == classname:
			paras['exec_stmt'] = int(x[3]) + int(x[4])
			paras['miss_stmt'] = int(x[3])
			paras['file_branch'] = int(x[5]) + int(x[6])
			paras['file_taken'] = int(x[6])
			paras['file_partial'] = 0
			break
	return paras
