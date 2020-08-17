#!/usr/bin/python3
# coding=utf-8

#######################################################
# File           : CLI.py                             #
# Author         : DulLah                             #
# Github         : https://github.com/dz-id           #
# Facebook       : https://www.facebook.com/dulahz    #
# Telegram       : https://t.me/DulLah                #
# Python version : 3.8+                               #
#######################################################
#         RECODE? OKE CANTUMKAN NAMA PEMBUAT          #
#######################################################

import platform, os, random, time

__BANNER__ = '''
  !b! ___ ___  ____   _____ 
  !b!|   T   T|    \ |     | !m!(!p!MULTI BRUTE FORCE FACEBOOK!m!)
  !b!| _   _ ||  o  )|   __j !m!-------------------------------
  !b!|  \_/  ||     T|  l_   !h!Dev      !m!: !p!DulLah
  !b!|   |   ||  O  ||   _]  !h!FB       !m!: !p!https//fb.me/dulahz
  !b!|   |   ||     ||  T    !h!Github   !m!: !p!https://github.com/dz-id
  !b!l___j___jl_____jl__j    !h!Version  !m!: !p!3.0
'''

osname = platform.system().lower()

list = {}

if osname[:3].lower() == 'lin':
    list['!m!'] = '\033[1;91m'
    list['!h!'] = '\033[1;92m'
    list['!k!'] = '\033[1;93m'
    list['!p!'] = '\033[1;97m'
    list['!c!'] = '\033[1;96m'
    list['!u!'] = '\033[1;95m'
    list['!b!'] = '\033[1;94m'
    list['!t!'] = '\033[1;90m'
    list['!r!'] = '\033[0m'
else:
    list['!m!'] = ''
    list['!h!'] = ''
    list['!k!'] = ''
    list['!p!'] = ''
    list['!c!'] = ''
    list['!u!'] = ''
    list['!b!'] = ''
    list['!t!'] = ''
    list['!r!'] = ''

def banner():
    clear()
    prints(__BANNER__, blank_left=2)

def clear():
    os.system('clear' if osname[:3].lower() == 'lin' else 'cls')

def br(num=0):
    if num == 0:
        return False
    if type(num).__name__ == 'int':
        return print('\n' *int((num-1)))
    return False

def progressBar(text='', max=10):
    count = 0
    message = '\r{0:>4}!m![!ran!{1:'+str(int(max)-1)+'s}!m!] !p!{2} {3:.0f}% '
    for i in range(max):
        count+=1
        write(message.format((''), ('=' *i), (text), (count * 100 / max)))
        time.sleep(0.1)
    write('\r')
    br(2)

def color(string=''):
    randomList = [
        '!m!', '!h!',
        '!k!', '!p!',
        '!c!', '!u!',
        '!b!', '!t!'
    ]

    for key in list:
        string = string.replace(key, list[key])

    randoms = random.choice(randomList)

    string = string.replace('!ran!', list[randoms])

    return(list['!r!']+string)

def inputs(string='', blank_left=None, blank_right=None):
    if type(string).__name__ in ['dict', 'list']:
        return input(string)

    string = color(string)

    if blank_right != None and type(blank_right).__name__ == 'int':
        string = (string+(' ' * blank_right))
    if blank_left != None and type(blank_left).__name__ == 'int':
        string = ((' ' * blank_left)+string)

    return input(string)

def prints(string='', with_flush=False, blank_left=None, blank_right=None):
    if type(string).__name__ in ['dict', 'list']:
        return print(string)

    string = color(string)

    if blank_right != None and type(blank_right).__name__ == 'int':
        string = (string+(' ' * blank_right))
    if blank_left != None and type(blank_left).__name__ == 'int':
        string = ((' ' * blank_left)+string)
    if with_flush == True:
        return print(end=f'\r{string}', flush=with_flush)

    return print(string)

def write(string='', blank_left=None, blank_right=None):
    if type(string).__name__ in ['dict', 'list']:
        os.sys.stdout.write(string)
        return os.sys.stdout.flush()

    string = color(string)

    if blank_right != None and type(blank_right).__name__ == 'int':
        string = (string+(' ' * blank_right))
    if blank_left != None and type(blank_left).__name__ == 'int':
        string = ((' ' * blank_left)+string)

    os.sys.stdout.write(string)
    os.sys.stdout.flush()