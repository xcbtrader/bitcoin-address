__author__ = 'xcbtrader'
# -*- coding: utf-8 -*-

from bitcoin import *

def crear_addr_word(word):
	priv = sha256(word)
	pub = privtopub(priv)
	addr = pubtoaddr(pub)
	wif = encode_privkey(priv, 'wif')
	return addr, priv, wif

word = input('Entra la palabra para crear direccion bitcoin:? ')
addr, priv, wif = crear_addr_word(word)
print('####################################################')
print('WORD: ' + word)
print('ADDR: ' + addr)
print('PRIV: ' + priv)
print('WIF: ' + wif)
print('####################################################')
