#getting words from file
import hashlib
def file():
    dat = input("Enter file name[note file must be in the same directory of the application]....?\n ")
    print (hashlib.algorithms_guaranteed)
    type = input("Enter type of hashing....?")
    fh = open(dat, 'r')
    for lines in fh.readlines():
        for word in lines.split():
            print("{}".format(hashing(word,type)))
    leave()
def handle():
    hashfile = input("Enter hash file name[note file must be in the same directory of the application]....?\n")
    dict = input("Enter dictionary file name[note file must be in the same directory of the application]....?\n")
    type = input("Enter type of hashing....?")
    df = open(dict,'r')
    hf = open(hashfile,'r')
    hw=[]
    dhw=[]
    word=[]
    for hl in hf.readlines():
        if hl is not None:
            hw = hw.__add__(hl.split())
    for dl in df.readlines():
        for dw in dl.split():
            word.append(dw)
            dhw.append(hashing(dw,type))
    decrypt(hw,dhw,word)
    leave()
#hashing function
def hashing(word, type):
    word = word.encode("utf-8")
    hs = hashlib.new(type)
    hs.update(word)
    hashed = hs.hexdigest()
    return hashed
def decrypt(hw,dhw,word):
    for i in range(len(hw)):
        matchFound = '0'
        for j in range(len(dhw)):
            if hw[i] == dhw[j]:
                print(word[j], end=' ')
                matchFound = '1'
                break
        if matchFound == '0':
            print("()", end=' ')

#asking_user
def leave():
    out = input("Do you want to leave [Y or N]..?")
    if out is 'Y':
        data = input("<< GO Fuck Your Self >>")
    elif out is 'y':
        data = input("<< GO Fuck Your Self >>")
    elif out is 'N':
        choose()
    elif out is 'n':
        choose()
    else:
        data = input("<< GO Fuck Your Self >>")
#what to do ?
def choose():
    choice = input("""
 _   _           _       _ _
| | | |         | |     (_) |
| |_| | __ _ ___| |__    _| |_
|  _  |/ _` / __| '_ \  | | __|
| | | | (_| \__ \ | | | | | |_
\_| |_/\__,_|___/_| |_| |_|\__|
Make your choice:\n [Press 1 for hashing a file...]\n [Press 2 for decryption of a file...]""")
    if choice is '1':
        file()
    elif choice is '2':
        handle()
    else:
        print("fuck it")
choose()

