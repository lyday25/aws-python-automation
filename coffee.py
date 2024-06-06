#create a python logic that will insert user input into an empty coffee array
coffee=[]
while True:
    shopped_item = input("Enter shop items: ")
    if shopped_item == "":
        break
    else:
        coffee.append(shopped_item)
        print(coffee)
# 
print("These are the coffee items: " + str(coffee))
