"""
lamecrypt version 0.5.5
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
        This function encrypts an ASCII string using a Caesar cipher-like cipher. It subtracts 2 from the value of all ASCII character codes by 2 (for the sake of simplicity).
        """
        ordinals = []
        enc_str = ""
        for i in range(len(string)):
            ordinals.append(ord(string[i]))
            ordinals[i] -= 2
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
            ordinals[i] += 2
            dec_str += chr(ordinals[i])
        return dec_str


crypt = lamecrypt()
parser = argparse.ArgumentParser(
    description="(lame) ASCII string encryption/decryption utility")
group = parser.add_mutually_exclusive_group()
group.add_argument("-e", "--encrypt", action="store_true",
                   help="encryption mode, should be followed by a plain text string")
group.add_argument("-d", "--decrypt", action="store_true",
                   help="decryption mode, should be followed by an encrypted string")
args = parser.parse_args()
if args.encrypt:
    print(crypt.encrypt(args.encrypt))
elif args.decrypt:
    print(crypt.decrypt(args.decrypt))
else:
    print(
        "usage: python lamecrypt.py [-e | -d] YourStringHere\nRun \"python lamecrypt.py -h\" for more detailed help")
