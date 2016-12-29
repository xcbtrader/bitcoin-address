__author__ = 'xcbtrader'
# -*- coding: utf-8 -*-

from bitcoin import *

def crear_addr_HEX(nGen):
	priv = generar_HEX(nGen)
	pub = privtopub(priv)
	addr = pubtoaddr(pub)
	wif = encode_privkey(priv, 'wif')
	return addr, priv, wif

def generar_HEX(nDecimal):
	aHex = hex(nDecimal)
	aHex = aHex[2:].upper()
	aHex = ((64-len(aHex)) * '0') + aHex
	return aHex

nGen = int(input('Numero entero para crear direccion btc:? '))

addr, priv, wif = crear_addr_HEX(nGen)
print('####################################################')
print('ENTERO: ' +str(nGen))
print('ADDR: ' + addr)
print('PRIV: ' + priv)
print('WIF: ' + wif)
print('####################################################')
