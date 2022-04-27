import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignores SSl certificate errors - Optional to make it work for HTTPS as well else it will only open HTTP
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Accessing web address
web_address_input = 'http://py4e-data.dr-chuck.net/comments_42.xml'
web_address_read = urllib.request.urlopen(web_address_input, context=ctx).read()

# Parsing the XML
xml_parsed = ET.fromstring(web_address_read)

# Creating list of all the comment under comments
list_ = xml_parsed.findall('comments/comment')

#initiating sum as 0
sum = 0

# Iterating comment for count
for comment in list_:
    # Adding one by one all the count
    sum = sum + int(comment.find('count').text)
print("Retriving ", web_address_input)
# print(f"Retrieved {characters} characters")
print("Count: ", len(list_))
print("Sum:", sum)
