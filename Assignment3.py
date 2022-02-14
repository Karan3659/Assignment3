#Question1
print('                 QUESTION1')
string1=str(input('Enter the string:'))
words=string1.lower().split()
if len(words)==1:
    words=words[0]
dict1=dict()
for word in words:
    if word in dict1:
        dict1[word]+=1
    else:
        dict1[word]=1
print(dict1)     




#Question2
print ("    \n\n\n Question 2")
def checking_leap_year(year: int) -> bool:                                                                                
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
while True:
    date = int(input("Day - "))
    month = int(input("Month - "))
    year = int(input("Year - "))
    if (date < 1) or (date > 31) or (month < 1) or (month > 12) or (year < 1800) or (year > 2025):                  
        print("Please use the given conditions for entering the current date\nC1 : 1<=month<=12\nC2 : 1<=day<=31\nC3 : 1800<=year<=2025")
        continue
    if month in (4,6,9,11) and date == 31:                                                                          
        print("The given month has only 30 days\nPlease enter a valid date")
        continue
    elif month == 2 and date >= 29:                                                                                 #Condition for no. of days in February
        if checking_leap_year and date != 29:
            print("The given month has only 29 days\nPlease enter a valid date")
            continue
        elif not checking_leap_year(year):
            print("The given month has only 28 days\nPlease enter a valid date")
            continue
    break
if month == 2:                                                                                                      
    if checking_leap_year(year):
        max_days = 29
    else:
        max_days = 28
elif month in (4,6,9,11):
    max_days = 30
else:
    max_days = 31
if date == max_days:                                                                                               
    date = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
else:
    date += 1
print("Next Date is: %d/%d/%d" % (date,month,year))



#Question3
print("    \n\n\n Question3")
list1=eval(input("Enter the list of numbers"))
list2=[]
for x in list1:
    list2.append((x,x*x))
print("\nList containing (n,n square) is shown below:")
print(list2)



#Question4
print ("    \n\n\n Question4")
given_table = [ ["A+","Outstanding",10],
                ["A","Excellent",9],
                ["B+","Very Good",8],
                ["B","Good",7],
                ["C+","Average",6],
                ["C","Below Average",5],
                ["D","Poor",4] ]
while True:                                                                                                         #loop for making sure the user inputs the value between 4 and 10
    grade_point = eval(input("Enter the grade point of the student: "))
    if 4 <= grade_point <= 10:
        break
    else:
        print("The grade point must be between 4 and 10")
for i in given_table:                                                                                       
    for j in i:
        if j == int(grade_point):
            print("Your Grade is '%s' and %s Performance" % (i[0],i[1]))
            break



#Question 5
print ("        \n\n\n Question 5")
string = "ABCDEFGHIJK"
j = 0
while len(string) - j*2 >= 1:
    print(" "*j + string[0 : len(string) - j*2])
    j += 1

    


#Question 6
print('       \n\n\n  QUESTION 6')
repeat="Y"
dic={}
dic2={}
list_sid=[]
list_2=["Y","y","n","N"]
while repeat=="Y" or repeat=="y":
    name = str(input("Enter student name:"))
    sid = int(input("Enter student SID:"))
    while sid in list_sid:
        print("\nThis SID is already entered:\nPlease enter unique SID\n")
        sid=int(input("Enter student SID:"))
    list_sid.append(sid)
    while sid<0:
        print("\nError\nSID can't be negative\n")
        sid=int(input("Enter student SID:"))
    else:
        dic.update({sid: name})
        dic2.update({name:sid})
        repeat = str(input("Enter Y to continue or N to end:"))
    if repeat=="N" or repeat=="n":
        break
    while (not (repeat in list_2)):
        print("\nError\nPlease enter valid input['Y' or 'N']")
        repeat=str(input("\nEnter Y to continue or N to end:"))
#a
print("\nQ.6(a)")
print("The Dictionary containing {'SID':'Name'} is shown below")
print(dic)
# b
print("\nQ.6(b)")
list_k=sorted(dic2)
dic3={}
for ele in list_k:
    dic3.update({dic2.get(ele):ele})
print("The Dictionary after sorting according to name:")
print(dic3)

# c
print("\nQ.6(c)")
sort_dic = sorted(dic)
dic4 = {}
for va in sort_dic:
    dic4.update({va: dic.get(va)})
print("The Dictionary after sorting according to SID:")
print(dic4)
# d
print("\nQ.6(d)")
enter_sid = int(input("Enter SID to get name of student:"))
output_name = str(dic.get(enter_sid))
print(f"Name of student with SID {enter_sid} is {output_name}.")




#Question 7
print ("    \n\n\n Question 7")
a = 0
b = 1
sum = 0
while True:                                                                     
    num = int(input("Enter the no. of terms of the Fibonacci sequence: "))
    if num < 0:
        print("Number of terms must be non-negative\nPlease enter again\n")
        continue
    if num == 0:
        print("As the number of terms = 0, the average of all terms = 0")
        break
    else:
        print("The Fibonacci sequence is as follows:")
        print(a,end=" ")
        for i in range(1,num):
            sum += b
            print(b, end=" ")
            c = a + b
            a = b
            b = c
        print("\nThe average of the terms of Fibonacci sequence upto %d terms is %0.2f" % (num,sum/num))
        break



#Question 8

print("    \n\n\n\ Question 8")
#Given Sets
set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}
#printing the given sets
print(f"Set1= {set1}\nSet2= {set2}\nSet3= {set3}")
#a
print("\nQ.8(a)")
print("\nA new Set of all 'elements that are in Set1 and Set2 but not both' is:")
set_sym_dif=set1.symmetric_difference(set2)
print(set_sym_dif)
#b
#set1 Union set2
print("\nQ.8(b)")
print("\nA new set of all elements that are 'in only one of the three sets Set1,Set2 and Set3' is:")
set_u1=set1.union(set2)

#set1 Union set2 Union set3
set_uf=set_u1.union(set3)

#set1 intersection set2
set_i1=set1.intersection(set2)

#set1 intersection set2 intersection set3
set_if=set_i1.intersection(set3)

#set1 intersection set2
set_12=set1.intersection(set2)

#set2 intersection set3
set_23=set2.intersection(set3)

#set3 intersection set1
set_13=set1.intersection(set3)

#final required set
set_f1=set_uf-set_12-set_23-set_13
print(set_f1)
#c
print("\nQ.8(c)")
set_c1=set_12.union(set_23)
set_c2=set_c1.union(set_13)
set_final=set_c2-set_if
print("\nA new set of elements that are 'exactly in two of the sets Set1, Set2 and Set3' is:")
print(set_final)
#d
print("\nQ.8(d)")
set_d={1,2}
set_d.clear()
for i in range(1,11):
    set_d.add(i)
set_new=set_d-set1
print("\nA new set of all Integers in the 'range 1 to 10' that are 'not in Set1' is:")
print(set_new)
#e
print("\nQ.8(e)")
set_e=set_d-set_uf
print("\nA new set of all Integers in the range 1 to 10 that are not in Set1,Set2 and Set3.")
print(set_e)





    
