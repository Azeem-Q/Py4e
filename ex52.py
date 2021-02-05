largest = None
smallest = None
numList = []
while True:
    
    try:
        num = input("Enter a number: ")
        num = int(num)
        numList.append(num)
        
    except:
        if num == "done" : 
            break
        else:
            print('Invalid input')
   
    finally:
        for i in numList:
            if largest is None:
                largest = i
            elif largest < i:
                largest = i
            
    
        for i in numList:
            if smallest is None:
                smallest = i
            elif smallest > i:
                smallest = i
            

    
    
print("Maximum is", largest)
print("Minimum is", smallest)