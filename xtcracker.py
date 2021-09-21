import hashlib


print("author dnanjer ")
print("subscribe xtacin")

flag =0

pass_hash = input("masukan file md5: ")

wordlist = input("file name: ")

try:
  pass_file = open (worlist, "r")

except:
    print("tidak ada file")
    quit()


for word in pass_file:



    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip)().hexdigest()
    print(word)
    print(digest)
    print(pass_hash)


    if digest == pass_hash:
        print("passwod tidak diketahui")
        print("paswword ini adalah" + word )
        break

if flag ==0:
    print("password/pass no list direktori")
