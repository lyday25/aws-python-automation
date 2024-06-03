#Initial value should be increased by any number put in the interface

def tasksum():
    counter=0
    basket=[]
    while True:
        number=int(input("Enter your number: "))
        counter=counter+number
        if counter >= 120:
            break
        else:
            print(counter)
            basket.append(counter)
            print(basket)
    print("This is my final value: " + str(counter)) 
    
tasksum()       
            
    
