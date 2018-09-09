"""
lamecrypt version 0.5.1
Copyright (C) 2018 Alex Tze

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import argparse


class lamecrypt:

    def __init__(self):
        pass

    def encrypt(self, string):
        """
        This function encrypts an ASCII string using a Caesar cipher-like cipher. It adds the value of all ASCII character codes of the string by 2 (for the sake of simplicity).
        """
        ordinals = []
        enc_str = ""
        for i in range(len(string)):
            ordinals.append(ord(string[i]))
            ordinals[i] += 2
            enc_str += chr(ordinals[i])
        return enc_str

    def decrypt(self, string):
        """
        This function decrypts an ASCII string encrypted by the previous function.
        """
        ordinals = []
        dec_str = ""
        for i in range(len(string)):
            ordinals.append(ord(string[i]))
            ordinals[i] -= 2
            dec_str += chr(ordinals[i])
        return dec_str


crypt = lamecrypt()
parser = argparse.ArgumentParser()
parser.add_argument("string", type=str,
                    help="string to encrypt or decrypt")
parser.add_argument("-e", "--encrypt", help="encryption mode")
parser.add_argument("-d", "--decrypt", help="decryption mode")
args = parser.parse_args()
if args.encrypt:
    print(crypt.encrypt(args.string))
elif args.decrypt:
    print(crypt.decrypt(args.string))
