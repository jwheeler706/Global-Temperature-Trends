from __future__ import division

def update(num,max):
    bar = []
    ratio = num/max
    oldRatio = (num-1)/max
    if( num == 1):
        bar = ["[----------]"]
        print(''.join(bar))
        return True
    elif( ratio >= 0.1 and oldRatio < 0.1 ):
        bar = ["[!---------]"]
        print(''.join(bar))
        return True
    elif( ratio >= 0.2 and oldRatio < 0.2 ):
        bar = ["[!@--------]"]
        print(''.join(bar))
        return True
    elif( ratio >= 0.3 and oldRatio < 0.3 ):
        bar = ["[!@#-------]"]
        print(''.join(bar))
        return True
    elif( ratio >= 0.4 and oldRatio < 0.4 ):
        bar = ["[!@#$------]"]
        print(''.join(bar))
        return True
    elif( ratio >= 0.5 and oldRatio < 0.5 ):
        bar = ["[!@#$%-----]"]
        print(''.join(bar))
        return True
    elif( ratio >= 0.6 and oldRatio < 0.6 ):
        bar = ["[!@#$%^----]"]
        print(''.join(bar))
        return True
    elif( ratio >= 0.7 and oldRatio < 0.7 ):
        bar = ["[!@#$%^&---]"]
        print(''.join(bar))
        return True
    elif( ratio >= 0.8 and oldRatio < 0.8 ):
        bar = ["[!@#$%^&*--]"]
        print(''.join(bar))
        return True
    elif( ratio >= 0.9 and oldRatio < 0.9 ):
        bar = ["[!@#$%^&*+-]"]
        print(''.join(bar))
        return True
    elif( ratio == 1 ):
        bar = ["[!@#$%^&*+~]"]
        print(''.join(bar))
        return True
    else:
        return False
