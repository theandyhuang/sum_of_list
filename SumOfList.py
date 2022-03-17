def sum_of_list(list1):
    return sum(list1)
list1 = []
while True:
    number = input("請輸入一個整數計算加總，若要離開則輸入q: ")
    if number == "q":
        break
    number = int(number)
    list1.append(number)
print(list1)
print("剛剛輸入的數字加總為",sum_of_list(list1))

