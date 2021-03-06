import sys, os, re
import pg, pgdb


def index(req):
    #Extracting the POST variable
    form = req.form
    acct = form['userAccountID']

    # Connecting to Database...
    
    # Query for the Subject List using Stored Proc

    # Get values

    # Parse it to html

    html = '<ul id="student-subjects-list-object" data-role="listview" data-filter="true">'
  
    html = concat(html, generate_li_item("CSC171BBB"))
    html = concat(html, generate_li_item("CSC188MOP"))
    html = concat(html, generate_li_item("CSC199MMM"))
    html = concat(html, "")
    
    # Close DB
    
    # Return it...
    return html

def generate_li_item(subjectSectionID):
    #Get the subject name, section, instructor...
    subjectCode = ""
    subjectDesc = ""
    sectionCode = ""
    instructor  = ""
    #Parse it to html..
    html = '<li id="'+subjectSectionID+'"><a href="Javascript:_queryHandler.doQuerySetChild()">'
    html = concat(html, 'Subject Title')
    html = concat(html, '<div class="ui-li-aside">Descriptive Text ni siya</div></a></li>')
    return html


def concat(str1, str2):
    return str1 + str2

