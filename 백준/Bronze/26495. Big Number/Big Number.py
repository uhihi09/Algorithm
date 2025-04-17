a = input()
for i in range(len(a)):
    if a[i] == "0":
        print('''0000
0  0
0  0
0  0
0000
''')
    elif a[i] == "1":
        print('''   1
   1
   1
   1
   1
''')
    elif a[i] == "2":
        print('''2222
   2
2222
2
2222
''')
    elif a[i] == "3":
        print('''3333
   3
3333
   3
3333
''')
    elif a[i] == "4":
        print('''4  4
4  4
4444
   4
   4
''')
    elif a[i] == "5":
        print('''5555
5
5555
   5
5555
''')
    elif a[i] == "6":
        print('''6666
6
6666
6  6
6666
''')
    elif a[i] == "7":
        print('''7777
   7
   7
   7
   7
''')
    elif a[i] == "8":
        print('''8888
8  8
8888
8  8
8888
''')
    elif a[i] == "9":
        print('''9999
9  9
9999
   9
   9
''')