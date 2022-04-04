cobol = ['C','O','B','O','L']
while True:
    n = input().upper().split('-')
    if n[0] == 'FIM':
        break
    else:
        for i in range(len(n)):
            if n[i].startswith(cobol[i]) == True:
                if i == len(n)-1:
                    print('GRACE HOPPER')
                continue
            elif n[i].endswith(cobol[i]) == True:
                if i == len(n)-1:
                    print('GRACE HOPPER')
                continue
            else:
                print('BUG')
                break