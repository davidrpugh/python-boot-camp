import urllib2

# declare a global variable
BASE_URL  = 'http://www.greenteapress.com/thinkpython/code/'

# file you wish to download
tmp_file_name = 'BadKangaroo.py'

# open a connection
url      = BASE_URL + tmp_file_name
tmp_file = urllib2.urlopen(url)

# download the contents of the file
data     = tmp_file.read()

# open a file with the same name 
with open(tmp_file_name, "w") as code:
    # write the downloaded contents to this file
    code.write(data)
    # never forget to close your file!
    code.close()
