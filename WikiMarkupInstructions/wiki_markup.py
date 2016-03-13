
#-----Statement of Authorship----------------------------------------#
#
#  By submitting this task the signatories below agree that it
#  represents our own work and that we both contributed to it.  We
#  are aware of the University rule that a student must not
#  act in a manner which constitutes academic dishonesty as stated
#  and explained in QUT's Manual of Policies and Procedures,
#  Section C/5.3 "Academic Integrity" and Section E/2.1 "Student
#  Code of Conduct".
#
#  First student's no: n8857954
#  First student's name: Damon Jones
#  Portfolio contribution: 85%
#
#  Second student's no: PUT 2ND STUDENT'S NUMBER HERE
#  Second student's name: PUT 2ND STUDENT'S NAME HERE
#  Portfolio contribution: 15%
#
#  Contribution percentages refer to the whole portfolio, not just this
#  task.  Percentage contributions should sum to 100%.  A 50/50 split is
#  NOT necessarily expected.  The percentages will not affect your marks
#  except in EXTREME cases.
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  WIKI-MARKUP
#
#  This task involves defining a function which converts plain
#  text files to HTML files.  It allows users to markup their
#  text using a simpler notation than is used by HTML.  The markup
#  notation is instead based on the one used by Wikipedia.  See the
#  instructions for details.
#
#--------------------------------------------------------------------#



#-----Automatic Tests------------------------------------------------#
#
#  To test your function we have provided some text files. Your
#  function is required to generate corresponding HTML files.  The
#  "doctest" script below doesn't actually test your solution, it
#  just calls your function.  To see the outcome you need to inspect
#  the generated HTML files in a web browser.
#
"""
NB: This test script is executed to create the HTML files.  Passing
these 'tests' does NOT necessarily mean that you have completed the
task.

Step A: Delete old HTML files, if any

>>> from os import remove
>>> try:
...     remove('Test1_Plaintext.html')
... except:
...     pass
>>> try:
...     remove('Test2_Dashes.html')
... except:
...     pass
>>> try:
...     remove('Test3_Emphasis.html')
... except:
...     pass
>>> try:
...     remove('Test4_Headings.html')
... except:
...     pass
>>> try:
...     remove('Test5_ParagraphsAndLists.html')
... except:
...     pass
>>> try:
...     remove('Test6_HeadingsAndLists.html')
... except:
...     pass
>>> try:
...     remove('Test7_AllWikiMarkups.html')
... except:
...     pass

Step B: Create new HTML files

Test 0: Special case, source file does not exist
>>> wiki_markup('Test0_Nonexistent')
False

Test 1: A plain text file with no markups at all
>>> wiki_markup('Test1_Plaintext')
True

Test 2: Some text containing en-dashes and em-dashes
>>> wiki_markup('Test2_Dashes')
True

Test 3: Some text containing markups for emphasis
>>> wiki_markup('Test3_Emphasis')
True

Test 4: Some text containing headings
>>> wiki_markup('Test4_Headings')
True

Test 5: Text containing paragraphs and lists
>>> wiki_markup('Test5_ParagraphsAndLists')
True

Test 6: Text containing headings and lists
>>> wiki_markup('Test6_HeadingsAndLists')
True

Test 7: A file containing all of our markups
>>> wiki_markup('Test7_AllWikiMarkups')
True

------------

Additional tests will appear here when your solution is marked to
ensure that it works in general.

"""
# 
#--------------------------------------------------------------------#



#-----Students' Solution---------------------------------------------#
#
#  Complete the task by filling in the template below.

from re import sub

##  **** DEFINE YOUR wiki_markup FUNCTION HERE ****

#
#--------------------------------------------------------------------#





def wiki_markup(files):
    
## Try Allows for the return of a true\false value with sucess or execptions\failure respectively.
    try:
### Get Webpage Content From Textfile ###
## Loading file to string
        txt = open(files+'.txt', 'U')
        text = txt.read()

## Markup- Character Swapins
        text = sub('---', '&mdash', text)
        text = sub('--', '&ndash', text)
        
## Objects that use the same symbols must be loaded with those that only match greater numbers of symbols first
## otherwise those that use fewer symbols will trigger on and remove the symbols used by the larger.
        text = sub('===([^=]*)===', '<h2>\\1</h2>', text)
        text = sub('==([^=]*)==', '<h1>\\1</h1>', text)
        text = sub("'''([^']*)'''", '<b>\\1</b>', text)
        text = sub("''([^']*)''", '<i>\\1</i>', text)
        
## List type commands must be run before their respective list items as the types use the list item notation
## to distinguish their type
        text = sub('\[([^\[\]]*#[^#\[\]]*#[^\[\]]*)\]','<ol>\\1</ol>',text)
        text = sub('#([^#]*)#','<li>\\1</li>', text)
        text = sub('\[([^\[\]]*\*[^\*\[\]]*\*[^\[\]]*)\]','<ul>\\1</ul>',text)
        text = sub('\*([^\*]*)\*','<li>\\1</li>', text)

## Paragraph tags are done last as otherwise they would convert the list opening tags
        text = sub("\[([^\[\]]*)\]", '<p>\\1</p>', text)

### Compile Webpage ###
## Create HTML file
        html = open(files+'.html', 'w')

## Add Head section with file name title, open body section
        html.write('<head> \n <title>'+files+'</title> \n</head> \n <body> \n')
        
## Write Content and close body
        html.write(text + '\n </body>')
        
## Close file
        html.close()
        
## Return Sucess or failure as true\false
    except Exception:
        return False
    return True





#-----Testing--------------------------------------------------------#
#
#  The code below will run the tests.  You can comment it out
#  while developing your solution, but leave it uncommented when
#  you submit this portfolio task.  WARNING: Running this code will
#  delete old copies of the HTML files.
#
if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)
#
#--------------------------------------------------------------------#

    
