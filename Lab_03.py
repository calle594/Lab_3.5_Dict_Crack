import hashlib

# list of passwords
dic = ['123', '1234', '12345', '123456', '1234567', '12345678',
       'password', 'qwerty', 'abc', 'abcd', 'abc123', '111111',
       'monkey', 'arsenal', 'letmein', 'trustno1', 'dragon',
       'baseball', 'superman', 'iloveyou', 'starwars',
       'montypython', 'cheese', '123123', 'football', 'batman', 'BATMAN']

hashes = []

# list of corresponsing md5 hashes
for x in dic:
    md5hash = hashlib.md5(x.encode('utf-8'))
    hashes.append(md5hash.hexdigest())

# zip dic and hashes to create dictionary(rainbow table)
rainbow = dict(zip(hashes, dic))


def dict_attack(password_hash):
    """Check password hash against dictionary of common passwords"""
    print(f'Cracking hash: {password_hash}')
    password_found = rainbow.get(password_hash)

    if password_found:
        print(f'Password recovered: {password_found}')
    else:
        print(f'Password not recovered')


def main():
    print('[dict_crack] Tests')
    # test case
    password_hash = '478bf2de70f915a6320a5451c3d7fdb9'
    dict_attack(password_hash)


if __name__ == '__main__':
    main()
