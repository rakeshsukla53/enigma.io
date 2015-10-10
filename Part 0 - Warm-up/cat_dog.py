__author__ = 'rakesh'

def cat_dog(str):
    cat = 0
    dog = 0

    if len(str) < 3:
        return True

    for i in range(len(str)-2):

        if str[i] + str[i+1] + str[i+2] == 'cat': cat += 1
        elif str[i] + str[i+1] + str[i+2] == 'dog': dog += 1

    if cat == dog:
        return True
    else:
        return False




