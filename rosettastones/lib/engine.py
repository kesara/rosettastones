##############################################################################
# engine.py
# Rosetta Stones Web Application
# 
# Copyright (C) 2015 Kesara Rathnayake
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################

from binascii import hexlify
import hashlib

from rsa import newkeys
from simplecrypt import encrypt

KEY_SIZE = 512
HASHING = 'sha512'
ENCODING = 'UTF-8'

def generate_keys():
    (pub_key, pvt_key) = newkeys(KEY_SIZE)
    pub_key = pub_key.save_pkcs1().decode(ENCODING)
    pvt_key = pvt_key.save_pkcs1().decode(ENCODING)
    enc_pvt_key = encrypt(pub_key, pvt_key)
    return (pub_key, hexlify(enc_pvt_key))

def get_hash(key):
    hash = hashlib.new(HASHING)
    hash.update(key)
    return hash.hexdigest()
