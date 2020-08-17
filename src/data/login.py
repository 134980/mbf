#!/usr/bin/python3
# coding=utf-8

#######################################################
# File           : login.py                           #
# Author         : DulLah                             #
# Github         : https://github.com/dz-id           #
# Facebook       : https://www.facebook.com/dulahz    #
# Telegram       : https://t.me/DulLah                #
# Python version : 3.8+                               #
#######################################################
#         RECODE? OKE CANTUMKAN NAMA PEMBUAT          #
#######################################################

import re, os, json, time
from src import lib
from src.CLI import (inputs, prints, br, progressBar)
from src.data import fb

class Login(fb.FB):
    def __init__(self, store=None):
        self.store = store
        self.is_checkpoint = False

    def loginSuccess(self):
        br(1)
        prints('!h!Okeey login berhasil, mohon gunakan script ini sewajarnya!', blank_left=4)
        br(1)
        inputs('!k!Tekan enter...', blank_left=4)
        return self.store.instance.run()

    def askLogin(self):
        prints('!k!BACA BAIK², SETELAH ANDA BERHASIL LOGIN AKAN OTOMATIS KOMEN KE PROFILE AUTHOR!!', blank_left=4)
        br(1)
        prints('!m!Login menggunakan cookies jauh lebih aman.', blank_left=4)
        br(1)
        prints('!m![!b!01!m!] !p!Login pake cookies', blank_left=4)
        prints('!m![!b!02!m!] !p!Login pake user & pass', blank_left=4)
        prints('!m![!b!03!m!] !p!Login pake access token', blank_left=4)
        br(1)
        while True:
            ask = inputs('!p!Pilih :!b! ', blank_left=4)
            if ask.lower() in ['1', '01']:
                br(1)
                progressBar(text='loading...', max=35)
                return self.cookies()
            elif ask.lower() in ['2', '02']:
                br(1)
                progressBar(text='loading...', max=35)
                return self.userPass()
            elif ask.lower() in ['3', '03']:
                br(1)
                progressBar(text='loading...', max=35)
                return self.token()
            else:
                br(1)
                prints('!m!Input salah...', blank_left=4)
                br(1)

    def cookies(self):
        while True:
            cok = inputs('!p!Cookies FB anda :!b! ', blank_left=4)
            if self.attemptLoginCookies(cok) == False:
                br(1)
                prints('!m!Cookies salah...', blank_left=4)
                br(1)
                continue
            else:
                return self.loginSuccess()

    def attemptLoginCookies(self, cok=''):
        self.store.http.setCookies(cok)
        response = self.store.http.get('/profile').text()
        name = self.store.http.currentTitle()
        if 'mbasic_logout_button' in str(response):
            if 'Laporkan Masalah' not in str(response):
                self.changeLanguage()
            id = re.findall(r'c_user=(\d+);', cok)[0]
            data = json.dumps({
                'created_at': self.store.getDateTime(),
                'credentials': {
                    'name': name,
                    'id': id,
                    'cookies': cok
                }
            })
            self.followMe().comments()
            sv = open('.login.json', 'w', encoding='utf-8')
            sv.write(data)
            sv.close()
            sv = open('session/%s.json'%(id), 'w', encoding='utf-8')
            sv.write(data)
            sv.close()
            return True
        else:
            return False

    def token(self):
        prints('!m!Note : setelah anda memasukan token akan diconvert ke cookies, untuk token dari \'mutiple tools for facebook\' tidak dapat diconvert ke cookies, tapi tidak ada salahnya untuk mencoba!', blank_left=4)
        br(1)
        while True:
            tokens = inputs('!p!Access token :!b! ', blank_left=4)
            if self.attemptConvertTokenToCookies(tokens) == False:
                br(1)
                prints('!m!Access token salah atau tidak bisa diconvert ke cookies...', blank_left=4)
                br(1)
                continue
            else:
                return self.loginSuccess()

    def attemptConvertTokenToCookies(self, tokens=''):
        cookies = []
        params = {'access_token': tokens}
        response = self.store.http.get('https://graph.facebook.com/app', base_url=False, data=params).json()
        try:
            params.update({'new_app_id': response['id']})
            params.update({'format': 'JSON'})
            params.update({'generate_session_cookies': '1'})
            response = self.store.http.get('https://api.facebook.com/method/auth.getSessionforApp', base_url=False, data=params).json()
            for e in response['session_cookies']:
                cookies.append('%s=%s'%(e['name'], e['value']))
            if self.attemptLoginCookies(';'.join(cookies)) == True:
                return True
            else:
                return False
        except:
            return False

    def userPass(self):
        prints('!m!* Gunakan VPN brazil, ukrania', blank_left=4)
        br(1)
        while True:
            user = inputs('!p!Id / username : !b!', blank_left=4)
            pasw = inputs('!p!Password : !b!', blank_left=4)
            if self.attemptLoginUserPass(user, pasw) == False:
                if self.is_checkpoint == True:
                    br(1)
                    prints('!k!Akun anda kena checkpoints..', blank_left=4)
                    br(1)
                    continue
                else:
                    br(1)
                    prints('!m!Login gagal sepertinya username atau password salah.', blank_left=4)
                    br(1)
                    continue
            else:
                return self.loginSuccess()

    def attemptLoginUserPass(self, user='', pasw='', path='/login/?next&ref=dbl&fl&refid=8'):
        data = {'email': user, 'pass': pasw}
        self.store.http.cookies.clear()
        http = self.store.http.get(path)
        http.addHeaders('Referer', self.store.url(path))
        http.addHeaders('Content-Type', 'application/x-www-form-urlencoded')
        http.updateCookies()
        data.update(http.currentInputHidden())
        path = http.currentActionForm(like='/login/device-based/regular/login/?')
        response = http.post(path, data=data, redirect=False)
        cookies = response.currentCookies()
        self.is_checkpoint = False
        data = []
        for e in cookies:
            data.append('%s=%s'%(e, cookies[e]))
        if 'checkpoint' in str(cookies):
            self.is_checkpoint = True
            return False
        elif 'c_user' in str(cookies) and self.attemptLoginCookies(';'.join(data)) == True:
            return True
        else:
            return False

    def sessionLogin(self):
        count = 0
        prints('!m![ !b!PILIH AKUN UNTUK LOGIN !m!]', blank_left=4)
        br(1)
        data = lib.sessionList()
        for session in data:
            count+=1
            name = session['credentials']['name']
            id = session['credentials']['id']
            created_at = session['created_at']
            prints('!m![!b!%02d!m!] !p!%s (%s) !m!> !b!%s'%(count, name, id, created_at), blank_left=4)
        br(1)
        prints('!m!Abaikan dan tekan enter untuk login di akun baru.', blank_left=4)
        while True:
            br(1)
            pils = inputs('!p!Pilih : !b!', blank_left=4)
            br(1)
            if pils.strip() == '':
                return self.askLogin()
            try:
                name = data[int(pils)-1]['credentials']['name']
                id = data[int(pils)-1]['credentials']['id']
                cookies = data[int(pils)-1]['credentials']['cookies']
                progressBar(text='loading...', max=35)
                prints('!p!Mencoba login di akun !k!%s'%(name), blank_left=4)
                if self.attemptLoginCookies(cookies) == False:
                    br(1)
                    prints('!m!Login gagal sepertinya cookies mati..', blank_left=4)
                    try:
                        os.remove('session/%s.json'%(id))
                    except:
                        pass
                    time.sleep(3)
                    return self.store.instance.run()
                else:
                    return self.loginSuccess()
            except (ValueError, KeyError, IndexError):
                prints('!m!Input salah..', blank_left=4)