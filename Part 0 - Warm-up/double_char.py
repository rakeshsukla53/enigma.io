__author__ = 'rakesh'

def double_char(str):

    doubleString = ''

    for i in list(str):

        doubleString += i + i

    return doubleString

print double_char('Hi-There')

