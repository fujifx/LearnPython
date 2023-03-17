import urllib.request, urllib.parse, urllib.error

'''
** Using urllib in Python **
Since HTTP is so common, we have a library that does all the socket work
for us and makes web pages look like a file.
'''

# Reading a text file
file_handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in file_handle:
    words = line.decode().strip()
    print(words)
    for word in words:
        counts[word] = counts.get(word, 0) + 1      # count of each character
print(counts)

# Reading Web Pages

web_page_handle = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
# web_page_handle = urllib.request.urlopen('http://www.dr-chuck.com/page2.htm')

for line in web_page_handle:
    print(line.decode().strip())