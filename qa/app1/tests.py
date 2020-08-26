import pyDes
import base64

Key = "national"  #加密的key

Iv = None   #偏移量


def bytesToHexString(bs):
    '''
    bytes转16进制
    '''
    return ''.join(['%02X ' % b for b in bs])
def hexStringTobytes(str):
    '''
    16进制转bytes
    '''
    str = str.replace(" ", "")
    return bytes.fromhex(str)

# 加密
def encrypt_str(data):
    # 加密方法
    #padmode填充方式
    #pyDes.ECB模式
    method = pyDes.des(Key, pyDes.ECB, Iv, pad=None, padmode=pyDes.PAD_PKCS5)
    # 执行加密码 hex输出
    k = method.encrypt(data)
    data = bytesToHexString(k).replace(' ','')
    #bs64手粗
    #data =base64.b64encode(k)
    return data

# 解密
def decrypt_str(data):
    method = pyDes.des(Key, pyDes.ECB, Iv, pad=None, padmode=pyDes.PAD_PKCS5)
    k =hexStringTobytes(data)
    #bs64
    #k = base64.b64decode(data)
    return method.decrypt(k)


# Encrypt = encrypt_str("008610000085660")
# print(Encrypt)
aaa = 'AD71741B338F295A87CCDB481E083C8A'
Decrypt = decrypt_str(aaa)
print(Decrypt)