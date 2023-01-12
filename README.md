```
   _____ _                 _         __ _ _                                         _
  / ____(_)               | |       / _(_) |                                       | |
 | (___  _ _ __ ___  _ __ | | ___  | |_ _| | ___    ___ _ __   ___ _ __ _   _ _ __ | |_
  \___ \| | '_ ` _ \| '_ \| |/ _ \ |  _| | |/ _ \  / _ \ '_ \ / __| '__| | | | '_ \| __|
  ____) | | | | | | | |_) | |  __/ | | | | |  __/ |  __/ | | | (__| |  | |_| | |_) | |_
 |_____/|_|_| |_| |_| .__/|_|\___| |_| |_|_|\___|  \___|_| |_|\___|_|   \__, | .__/ \__|
                    | |                                                  __/ | |
                    |_|                                                 |___/|_|
                                                                By Jarwu | V1.0
    This is a simple file encryption procedures, security is low, mainly to prevent sensitive files from
being directly browsed by others or through similar to everything such software retrieved.
    Please backup the data to be encrypted before using this program to avoid data loss!!!

usage: file-encrypyt.py [-h] -m mode -f file -k key

options:
  -h, --help  show this help message and exit
  -m mode     encryption:e or decryption:d
  -f file     filename or directory
  -k key      Secrets key
```

# install
```
pip install -r requirements.txt
```

# example
```
python .\file-encrypyt.py -m e -f .\files\ -k 123
```