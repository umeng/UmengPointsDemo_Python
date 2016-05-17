# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
class prpcrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC
        self.iv = self.key[:16]

    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)
        length = 32
        count = len(text)
        amount = length - (count % length)
        if amount == 0:
            amount = length
        pad_chr = chr(amount & 0xFF)
        new_text = text + (pad_chr * amount)
        ciphertext = cryptor.encrypt(new_text)
        return ciphertext
