#SHEET1
#A2.
a=5**9
print(a)
a=3//2
print(a)
a=7//3
print(a)
a=7/3
print(a)
a=6==6
print(a)
a=20
a+=30
a%=3
print(a)
a=True * False
print(a)
a=True & False
print(a)
a=True and False
print(a)
a=((6>3) and (7<4) or(18==3))and (9>3)
print(a)
a=True is False
print(a)
a=((True==False)or(False>True))and(False<=True)
print(a)
#A3.
s1="Nice to have it"
s2="here"
print(s1 + s2)
#A4.
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
k=a[3][1][2]
print(k)
#A5.only at end
a+=[s1+s2]
print(a)
#A6.
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

for x in numbers:
    if x == 237:
        print(x)
        break;
    elif x % 2 == 0:
        print(x)
#A7.
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))
#A8.
#A9.
a = int(input("enter a number:"))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)
#A10.
#A11.
phrase = input("Input words: ")
phrase_list = phrase.split(",")
phrase_list.sort()
print((', ').join(phrase_list))
#A12.
#A13.
all_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
string = "kunal1sharma2"
total_digits = 0
total_letters = 0
for s in string:
    if s in all_digits:
        total_digits += 1
    elif s in all_letters:
        total_letters += 1
 
print("Total letters found :-", total_letters)
print("Total digits found :-", total_digits)
#A14.
#A15.
n = int(input())
divBy7 = [i for i in range(0, n) if (i % 7 == 0)]
print(divBy7)
#A16.

