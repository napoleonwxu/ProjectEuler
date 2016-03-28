#coding:utf-8
'''
通过观察发现 68,19,7,1,71 出现了8次
猜测为' the ' （是常见的 5 字符组合）
' the '的 ASCII 是 32 116 104 101 32
跟 68 19 7 1 71
XOR 得
100 103 111 100 103
翻译过来是
dgodg
则推出密钥为 god
'''
'''
base = [68, 19, 7, 1, 71]
strs = ' the '
for i in xrange(5):
    print base[i] ^ ord(strs[i])
'''
def decryption(fileName, cips):
    res = 0
    nums = []
    f = open(fileName)
    for num in f.readline().split(','):
        nums.append(int(num))
    #print nums
    for i in xrange(len(nums)):
        res += nums[i] ^ ord(cips[i%len(cips)])
    return res

fileName = 'p059_cipher.txt'
print decryption(fileName, 'god')