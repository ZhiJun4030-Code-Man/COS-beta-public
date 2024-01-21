from random import  randint
from time import sleep
def hexman(min,max):
    return hex(randint(min,max))
def printProgress(iteration, total, prefix='', suffix='', decimals=1, barLength=100):
    """
    zhijun的小指南
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    import sys
    formatStr = "{0:." + str(decimals) + "f}"
    percent = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = '=' * filledLength + ' ' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()

def cicon(time,how):
    if time==True:
        print('   _____               _                                         ____     _____ ')
        sleep(how)
        print('  / ____|             | |                                       / __ \   / ____|')
        sleep(how)
        print(' | |        ___     __| |   ___    _ __ ___    __ _   _ __     | |  | | | (___  ')
        sleep(how)
        print(" | |       / _ \   / _` |  / _ \  | '_ ` _ \  / _` | | '_ \    | |  | |  \___ \ ")
        sleep(how)
        print(' | |____  | (_) | | (_| | |  __/  | | | | | || (_| | | | | |   | |__| |  ____) |')
        sleep(how)
        print('  \_____|  \___/   \__,_|  \___|  |_| |_| |_| \__,_| |_| |_|    \____/  |_____/ ')
    if time == False:
        print('   _____               _                                         ____     _____ ')
        print('  / ____|             | |                                       / __ \   / ____|')
        print(' | |        ___     __| |   ___    _ __ ___    __ _   _ __     | |  | | | (___  ')
        print(" | |       / _ \   / _` |  / _ \  | '_ ` _ \  / _` | | '_ \    | |  | |  \___ \ ")
        print(' | |____  | (_) | | (_| | |  __/  | | | | | || (_| | | | | |   | |__| |  ____) |')
        print('  \_____|  \___/   \__,_|  \___|  |_| |_| |_| \__,_| |_| |_|    \____/  |_____/ ')


