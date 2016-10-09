from bs4 import BeautifulSoup
import sys

def singleFile():
	paras = {}
	
	filename = 'coverage/report/junit/overview-summary.html'

	html_doc = open(filename, 'r').read()
	soup = BeautifulSoup(html_doc, 'lxml')

	paras['total'] = int(soup.find('a', attrs={'title' : 'Display all tests'}).get_text())
	paras['fails'] = int(soup.find('a', attrs={'title' : 'Display all failures'}).get_text())
	paras['errors'] = int(soup.find('a', attrs={'title' : 'Display all errors'}).get_text())
	paras['skipped'] = int(soup.find('a', attrs={'title' : 'Display all skipped test'}).get_text())

	return paras
