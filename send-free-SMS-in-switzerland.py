import re
import mechanize
import sys

browser=mechanize.Browser()
browser.open('http://www.die-startseite.ch/Bern/')
browser.select_form(name='smsBooster')



browser['intlPrefix'] = ['0041'+sys.argv[1][1:3]]
browser['SMSEingabe'] = sys.argv[1][3:]
browser.form.new_control('text','smsMessage',{'value':''})
browser.form.fixup()
browser.form['smsMessage'] = sys.argv[2]
#browserowser['field1'] = 'value'
#browserowser['field2'] = 'value'
#browserowser['field3'] = 'value'
browser.submit()
