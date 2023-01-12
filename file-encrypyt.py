import argparse
import os
from Crypto.Cipher import AES
from alive_progress import alive_bar

AES_BLOCK_SIZE = AES.block_size
AES_KEY_SIZE = 16


def pad_bytes(bytes):
    while len(bytes) % AES_BLOCK_SIZE != 0:
        bytes += ' '.encode()
    return bytes


def pad_key(key):
    if len(key) > AES_KEY_SIZE:
        return key[:AES_KEY_SIZE]
    while len(key) % AES_KEY_SIZE != 0:
        key += ' '.encode()
    return key


def encrypt(key, filename):
    c_key = pad_key(key.encode())
    encryptor = AES.new(c_key, AES.MODE_ECB)

    with open(filename, 'rb') as f:
        file_bytes = f.read()
        f.close()

    file_bytes = pad_bytes(file_bytes)
    encrypt_data = encryptor.encrypt(file_bytes)

    with open(filename + '.enc', "wb") as fs:
        fs.write(encrypt_data)
        fs.close()

    os.remove(filename)


def decrypt(key, filename):
    c_key = pad_key(key.encode())
    decrypter = AES.new(c_key, AES.MODE_ECB)

    with open(filename, 'rb') as f:
        file_bytes = f.read()
        f.close()
    de_bytes = decrypter.decrypt(file_bytes)

    with open(filename[:-4], 'wb') as f:
        f.write(de_bytes)
        f.close()

    os.remove(filename)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", dest="mode", metavar='mode', help="encryption:e or decryption:d", required=True)
    parser.add_argument("-f", dest="file", metavar='file', help="filename or directory", required=True)
    parser.add_argument("-k", dest="key", metavar='key', help="secret key", required=True)
    args = parser.parse_args()

    is_dir = False
    if os.path.isdir(args.file):
        is_dir = True
    if is_dir:
        files = os.listdir(args.file)
        new_files_path = []
        for file in files:
            file_path = args.file + '/' + file
            if not os.path.isdir(file_path):
                new_files_path.append(file_path)

        with alive_bar(new_files_path.__len__()) as bar:
            for file in new_files_path:
                if args.mode == 'e':
                    encrypt(args.key, file)
                elif args.mode == 'd':
                    decrypt(args.key, file)
                bar()
    else:
        if args.mode == 'e':
            encrypt(args.key, args.file)
        elif args.mode == 'd':
            decrypt(args.key, args.file)


if __name__ == "__main__":
    version = '1.0'
    description = '''This is a simple file encryption procedures, security is low, mainly to prevent sensitive files from 
being directly browsed by others or through similar to everything such software retrieved.
    Please backup the data to be encrypted before using this program to avoid data loss!!!'''
    banner = '''
   _____ _                 _         __ _ _                                         _   
  / ____(_)               | |       / _(_) |                                       | |  
 | (___  _ _ __ ___  _ __ | | ___  | |_ _| | ___    ___ _ __   ___ _ __ _   _ _ __ | |_ 
  \___ \| | '_ ` _ \| '_ \| |/ _ \ |  _| | |/ _ \  / _ \ '_ \ / __| '__| | | | '_ \| __|
  ____) | | | | | | | |_) | |  __/ | | | | |  __/ |  __/ | | | (__| |  | |_| | |_) | |_ 
 |_____/|_|_| |_| |_| .__/|_|\___| |_| |_|_|\___|  \___|_| |_|\___|_|   \__, | .__/ \__|
                    | |                                                  __/ | |        
                    |_|                                                 |___/|_|        
                                                                By Jarwu | V{} 
    {}                                                            
'''.format(version, description)
    try:
        print(banner)
        main()
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt Detected.")
        print("Exiting...")
        exit(0)
