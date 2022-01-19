import time
import go
import ile

print('ver 1.1')
print('------------------------------------------------')

print(time.ctime())

print('------------------------------------------------')

nam = input("""What would you like?
1 add letters 
2 remove letters
--> """)
if nam == '1':
    go.go()
elif nam == '2':
    ile.ile()
elif nam == '':
    print('Nothing')
