#!/usr/bin/python
import urllib
import re
import sys
from bs4 import BeautifulSoup
import my_data
from my_data import required_data
if len(sys.argv)!=2:
 	print >> sys.stderr, "Error with command line argument"
  	sys.exit(1)
myhtml = urllib.urlopen(sys.argv[1]).read()
soup = BeautifulSoup(myhtml)
experiment_title = soup.find_all('header',id="experiment-article-heading")[0].text 
experiment_data = {}
experiment_title = experiment_title.strip() 
all_sections = soup.find_all('section',id=re.compile("experiment-article-section-[0-9]"))
for section in all_sections:
	heading = str(section.find_all('div',class_="heading")[0].text).strip()
	contents_list = section.find_all('div',class_="content")[0].contents
	content = ''
	for i in contents_list:
		if i != '\n':
			content = content+str(i)
	experiment_data[heading] = content

manual_data = '' 

for key in experiment_data:
	section_title = key 
	section_data = experiment_data[key]
 	manual_data=manual_data+'''<div id="'''+section_title+'''" class="manual-section">
       <p class="manual-section-title">'''+section_title+'''</p><hr />
       <div class="manual-section-description">'''+section_data+'''
       </div>
 	</div>'''

template_start = '''
<!DOCTYPE html>
<html> '''+required_data['head']+'''<body>'''+required_data['navbar']+'''<div class="row">'''+required_data['lab-index']+'''<div class="col-lg-10 lab-manual">'''

template_end = '''</div></div>'''+required_data['scripts']+'''</body>
</html>'''

print template_start+manual_data+template_end