#!/usr/bin/python3
# coding=utf-8

#######################################################
# File           : MBF.py                             #
# Author         : DulLah                             #
# Github         : https://github.com/dz-id           #
# Facebook       : https://www.facebook.com/dulahz    #
# Telegram       : https://t.me/DulLah                #
# Python version : 3.8+                               #
#######################################################
#         RECODE? OKE CANTUMKAN NAMA PEMBUAT          #
#######################################################

from src import lib
from src.store import Store
from src.CLI import (inputs, prints, banner, br, progressBar)
from time import sleep
import os

class MBF:
    def __init__(self, store=None):
        self.store = store
        store.instance = self

    def run(self):
        banner()
        if lib.isLogin() == False:
            if len(lib.sessionList()) == 0:
                return self.store.login.askLogin()
            else:
                return self.store.login.sessionLogin()
        if lib.isActive(self) == False:
            br(1)
            prints('!m!Sepertinya cookies mati.', blank_left=4)
            br(1)
            inputs('!k!Tekan enter untuk login kembali..', blank_left=4)
            return self.run()
        id = self.store.object['credentials']['id']
        name = self.store.object['credentials']['name']
        prints('!m!-!r!' * 55, blank_left=2)
        prints('!m![!b!>!m!] !p!Nama akun !m!:!k! %s!r!' %(name), blank_left=4)
        prints('!m![!b!>!m!] !p!IDs       !m!:!k! %s!r!' %(id), blank_left=4)
        prints('!m!-!r!' * 55, blank_left=2)
        for index in self.store.menu:
            prints(self.store.menu[index]['name'], blank_left=4)
        try:
            br(1)
            pils = int(inputs('!p!dz-id/>!b! ', blank_left=4))
            pils = '%02d'%(pils,)
            function = self.store.menu[pils]['func']
        except (ValueError, KeyError, IndexError):
            br(1)
            prints('!m!Input salah...', blank_left=4)
            sleep(2)
            return self.run()

        br(1)

        progressBar(text='loading...', max=35)

        return function()

    def back(self):
        inputs('!k!Tekan enter untuk kembali..', blank_left=4)
        return self.run()

    def clearDumpCache(self, count=0):
        list = lib.cacheDumpList()
        if len(list) == 0:
            br(1)
            prints('!m!Belum ada cache...', blank_left=4)
            br(1)
            return self.back()
        br(1)
        prints('!m![ !b!LIST SEMUA CACHE DARI HASIL DUMP!r! !m!]', blank_left=4)
        br(1)
        for cache in list:
            count+=1
            num = '%02d'%(count,)
            prints('!m![!b!%s!m!] !p!%s'%(num, cache['name']), blank_left=4)
        br(1)
        prints('!m!Guanakan (,)(comma) untuk pilihan selanjutnya, contoh: 1,2,3 . type \'all\' untuk menghapus semua cache.', blank_left=4)
        prints('!m!Hapus cache untuk menghemat penyimpanan!, abaikan dan tekan enter untuk kembali.', blank_left=4)
        br(1)
        select = inputs('!p!Pilih : !b!', blank_left=4)
        if select.lower() in ["all", "'all'"]:
            for delete in list:
                try:
                    name = delete['name']
                    path = delete['path']
                    os.remove(path)
                    prints('!h! - %s - Dihapus!r!' %(name), blank_left=6)
                except:
                    pass
            br(1)
            return self.back()
        br(1)
        for e in select.strip().split(','):
            try:
                name = list[int(e)-1]['name']
                path = list[int(e)-1]['path']
                os.remove(path)
                prints('!h! - %s - Dihapus!r!' %(name), blank_left=6)
            except:
                pass
        br(1)
        return self.back()
    
    def resultCrack(self):
        while True:
            ask = inputs('!p!Ingin melihat hasil CP/OK? !m![!p!CP/OK!m!]!p! : !b!', blank_left=4)
            if ask.lower() == 'cp':
                data = lib.resultCrack(name='CP')
                break
            elif ask.lower() == 'ok':
                data = lib.resultCrack(name='OK')
                break
            else:
                br(1)
                prints('!m!Input salah...', blank_left=4)
                br(1)
        if len(data) == 0:
            br(1)
            prints('!m!Belum ada hasil...', blank_left=4)
            br(1)
            return self.back()
        br(1)
        prints('!m![ !b!LIST SEMUA HASIL %s!r! !m!]'%(ask.upper()), blank_left=4)
        for res in data:
            br(2)
            prints('!m!> !p!Tanggal !b!%s !p!: !m!%s'%(res['created_at'], res['total']), blank_left=4)
            for e in res['list']:
                prints('!m!- !p!%s'%(e), blank_left=6)
        br(2)
        type = inputs('!m!Ketik \'delete\' untuk menghapus semua hasil atau enter untuk kembali !p!: !b!', blank_left=4)
        if type.lower() in ["delete","'delete'"]:
            os.remove('result/%s.json'%(ask.upper()))
            br(1)
            prints('!h!Semua hasil \'%s\' berhasil dihapus!'%(ask), blank_left=4)
            br(1)
            return self.back()

        return self.run()

    def changeAccount(self):
        try:
            os.remove('.login.json')
        except:
            pass
        self.store.http.cookies.clear()
        return self.run()

