#なぜかdURLファイルにはb'とか\nとかが入るのでこれで削除する

try:
    while(1):
        unCleansedUrl = input()

        cleansedUrl = unCleansedUrl[2:len(unCleansedUrl)-1 -4]
        print(cleansedUrl)
except EOFError:
    pass

