__author__ = 'xcbtrader'
# -*- coding: utf-8 -*-

from bitcoin import *

def crear_addr_aleat():
	priv = random_key()
	pub = privtopub(priv)
	addr = pubtoaddr(pub)
	wif = encode_privkey(priv, 'wif')
	return addr, priv, wif

addr, priv, wif = crear_addr_aleat()
print('#################################################3###')
print('ADDR: ' + addr)
print('PRIV: ' + priv)
print('WIF: ' + wif)
print('#################################################3###')
