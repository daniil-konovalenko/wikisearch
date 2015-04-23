init = open('core/__init__.py', 'w')
init.close()

import re
import operator
import os
import sys
sys.path.append(os.getcwd() + '\\core')
sys.path.append(os.getcwd() + '\\core\\externals\\httplib2')
from core.externals import httplib2
from core.pywikibot import pagegenerators

result_pages = dict()
URL_start = u'https://ht.wikipedia.org/wiki/'

# Tables in the wikitext are presented in the following way:
# {|
# |Content
# |}


def tables_search(string):
    rex_table = re.compile("\{\|[^\}]*\|\}")
    return len(rex_table.findall(string))

# Generates ordered HTML list from list of tuples


def ordered_list_links(inp_list):
    result = '<ol>\n'
    for elem in inp_list:
        result = result + '<li><a href="%s">%s -- %s</a></li>\n' % (URL_start+
                                                                    elem[0],
                                                                    elem[0],
                                                                    elem[1])
    result = result + '</ol>'
    return result


# Generator for pages
gen = pagegenerators.AllpagesPageGenerator(content=True, step=5000)
j = 0
for page in gen:
    text = page.text
    title = page.title()
    number_of_tables = tables_search(text)
    if number_of_tables != 0:
        result_pages[title] = number_of_tables

    print(j, 'from 56840 articles retrieved')
    j += 1


result_pages_sorted = sorted(result_pages.items(),
                             key=operator.itemgetter(1), reverse=True)

html_out = """
<!DOCTYPE html>
<html>
<head>
    <title>Tables</title>
    <meta charset="UTF-8">
</head>
<body>
<h3>Max number of tables</h3>
%s
</body>
</html>
""" % ordered_list_links(result_pages_sorted[:5])

output_file = open('output.html', 'w', encoding='utf8')
print(html_out, file=output_file)
print('SUCCESS')
output_file.close()
