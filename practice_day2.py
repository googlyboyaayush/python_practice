# number = [10,20,30,50,40,60]
# print(number)

# number = [10,20,30,50,40,60] #index o se start hota hai
# print(number[4])
# print(number[1])

# number = [10,20,30,50,40,60] #numbers add krna
# number.append(690)
# print(number)

# number = [10,20,30,50,40,60]
# print(number[0::2])
# print(number[ ::-1])

# numbers=[]
# for i in range(5):
#     number= int(input("Enter a number:"))
#     numbers.append(number)
# print("List",numbers)
# total_sum =sum(numbers)
# print("Sum","=",total_sum)
# max_num=max(numbers)
# print("MAx","=",max_num)

# number = [2,7,4,9,6,12,45,78,132,63,54,85,]
# count1 = 0
# count2 = 0

# for num in number:
#     if num%2==0:
#         count1+=1
#     elif num%2!=0:
#         count2+=1
        
# print("Even Count",count1)
# print("Odd Count",count2)

# sales = [1200,1500,1100,1800,2000]
# total_sales = sum(sales)
# print(total_sales)
# avarage = total_sales/len(sales)
# maximum = max(sales)
# minimum = min(sales)
# print(maximum)
# print(minimum)
# print(avarage)
# count = 0
# for num in sales:
#     if num> avarage:
#         count+=1
# print(count)

   
# marks = [45,67,89,34,90,56,72]
# total = sum(marks)
# avarage = total/len(marks)
# Highest_marks = max(marks)
# Lowest_marks = min(marks)
# Pass_count = 0
# for m in marks:
#    m >= 40
#    Pass_count+=1
# print("Total number", total)
# print("Avarage marks",avarage)
# print("Highest marks", Highest_marks)
# print("Lowest marks",Lowest_marks)
# print("Number of Student",Pass_count)

# new_list =[]
# for i in marks:
#    if i> 70:
#       new_list.append(i)
# print(new_list)
# sort_list =sorted(new_list)
# print(sort_list)

day=0
tempreture = [30,32,35,28,40,38,25]
# for temp in tempreture:
#     if temp>35:
#      day+=1
# print(day)
# for index,temp in enumerate(tempreture):
#    print("Day",index,"Tempreturet",temp)

# highest_temp = max(tempreture)
# print("Highest_tempretur", highest_temp)

# for index,temp in enumerate(tempreture):
#    if temp == highest_temp:
#       print("Highest tempreture index", index,",",temp)

# number = [20,20,20,203,0]
# for num in number:
#     print(num)
# for index,value in enumerate(number):
#     print(index,value)

marks=[55,88,76,90,60]
for index, mark in enumerate(marks,start=1):
    if mark>80:
        print(index,mark) 
       