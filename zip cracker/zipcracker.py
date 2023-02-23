import zipfile




count = 1
passwordListFile = input("Password list file name : ")
lockedZipFile = input("Locked zip file name : ")
with open(passwordListFile,'rb') as text:
    for entry in text.readlines():
        password = entry.strip()
        try:
            with zipfile.ZipFile(lockedZipFile,'r') as zf:
                zf.extractall(pwd=password)
                data = zf.namelist()[0]
                print('''********************\n[+] Password found! --> %s\n ~%s\n ~%s\n********************''' 
                    % (password.decode('utf8'),data))
                break
        except:
            number = count
            print('[%s] [-] Password failed! - %s' % (number,password.decode('utf8')))
            count += 1