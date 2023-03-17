'''
Source: https://www.youtube.com/watch?time_continue=249&v=Pv_pJgVu8WI&embeds_euri=https%3A%2F%2Fwww.freecodecamp.org%2Flearn%2Fscientific-computing-with-python%2Fpython-for-everybody%2Fnetworking-text-processing&embeds_origin=https%3A%2F%2Fwww.freecodecamp.org&source_ve_path=MTM5MTE3&feature=emb_logo

In the 1960's and 1970's strings were simply represented as 8 bit characters.
But in today's as things have complex it is not possible restrict characters to 8 bit
and say that the only things computers understand is ASCII. This is where Unicode comes
to the rescue. Unicode is billions of characters for every language and every
character set. Since there is so much space in Unicode its easy to take very small
variations of characters.

** Multi-Byte Characters **
To represent the wide range of characters computers must handle, we represent characters
with more than one byte.
> UTF-16 - Fixed length - Two bytes
> UTF-32 - Fixed Length - Four bytes
> UTF-8 - 1-4 bytes
    ~ Dynamic in length
    ~ Upwards compatible with ASCII
    ~ Automatic detection between ASCII and UTF-8
    ~ UTF-8 is recommended practice for encoding data to be exchanged between systems

But if we are to send Unicode over the network, it would be way too large.
It'd be this UTF-32, which instaed of being 8 bytes per character would be 4 bytes per
character. So it'd take all of these data that we build and make it 4 times larger.
And it'd way too difficult. So what they come with is ways to compress this.
UTF-16 is a subset of Unicode, its used in some countries. But the best practice for
moving data across the internet or in file that you are moving between computers is UTF-8.

In Python 3.0 onwards, all strings internally are UNICODE. When we talk to a network
resource using sockets or talk to a database we have to encode and decode (usually to UTF-8)

'''

print(ord('H'))
print(ord('o'))
print(ord('\n'))
