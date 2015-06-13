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
from contextlib import contextmanager
from hashlib import new as new_hash
from sqlite3 import connect as sqlite_conn

from rsa import newkeys, encrypt as rsa_encrypt, PublicKey
from simplecrypt import encrypt as simple_encrypt

KEY_SIZE = 512
HASHING = "sha512"
ENCODING = "UTF-8"
ISO_ENCODING = "ISO-8859-1"
TEMP_DB = "temp.db"


def generate_keys():
    """
    Generate key pair
    """
    (pub_key, pvt_key) = newkeys(KEY_SIZE)
    pub_key = pub_key.save_pkcs1().decode(ENCODING)
    pvt_key = pvt_key.save_pkcs1().decode(ENCODING)
    enc_pvt_key = simple_encrypt(pub_key, pvt_key)
    return (pub_key, hexlify(enc_pvt_key))


def get_hash(key):
    """
    Get hash value for a key.
    """
    hash = new_hash(HASHING)
    hash.update(key)
    return hash.hexdigest()


def encrypt(key, message):
    """
    Encrypt message with Public Key
    """
    public_key = PublicKey.load_pkcs1(key.encode(ENCODING))
    enc_msg = rsa_encrypt(message.encode(ENCODING), public_key)
    return enc_msg.decode(ISO_ENCODING)


@contextmanager
def temp_db_connect():
    """
    Connection to temporary database
    """
    connection = sqlite_conn(TEMP_DB)
    cursor = connection.cursor()
    try:
        yield cursor
    finally:
        connection.close()


def temp_store(id, key):
    """
    Store master key in temporary database.
    """
    with temp_db_connect() as c:
        c.execute("""INSERT INTO keys VALUES(?, ?);""", (id, key))
        c.connection.commit()
