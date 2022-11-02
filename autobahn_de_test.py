from itertools import zip_longest

def Prime(n):  
            for i in range(2,n//2+1):  
                if(n%i==0):  
                    return(0)  
            return(1)  

def dict_list(dicts):
    result = []
    for k, v in dicts.items():
            result.append(f"[{k}:{v}]")
    print(result)

if __name__ == '__main__':
    
    print("Please select your use case (1 or 2):")
    print("""
        1: Find first N prime number, and print the result
        2. Sort and combine these 2 lists and print the result 
    """)
    choice = int(input('Your choice: '))

    if choice == 1:
        
        
        N=int(input("Enter N number:"))  
        i=2 
        lst=[] 
        while(1):  
            if(Prime(i)):  
                lst.append(i) 
                if(len(lst)==N): 
                    break 
            i+=1 
        print(*lst) 
    elif choice == 2:
        lst1, lst2 = [], []

        lst1 = sorted([int(item) for item in input("Enter the list of number, separated by comma : ").split(",")]) 
        lst2 = sorted([item for item in input("Enter the list of char, separated by comma : ").split(",")])
        new_dict = dict(zip_longest(lst1, lst2, fillvalue="NULL"))
        dict_list(new_dict)
        
    else:
        print("Wrong input")