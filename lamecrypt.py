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

    def helpinfo(self):
        """
        This function returns the help message (str) of this crypto script.
        """
        hilfe = """usage:
        python(3) lamecrypt.py -e <YourString>\tencrypts string <YourString>
        python(3) lamecrypt.py -d <YourString>\tdecrypts string <YourString>
        python(3) lamecrypt.py -h\tdisplays this message """
        return hilfe


crypt = lamecrypt()
parser = argparse.ArgumentParser()
