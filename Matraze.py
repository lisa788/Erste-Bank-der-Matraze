#!/usr/bin/env python3
from collections import OrderedDict

print("Welcome to Erste Bank der Matratze")

menu = "Choose an option:\n 1) Balance Inquiry\n 2) Deposit\
\n 3) Transfer \n 4) Withdrawal \n 5) Flee the Country"
print(menu)

rand = 0        #for naming unnamed bags
spacing = 17    #used for formatting
bags = {"Bugout Bag":['0','0','0','0']}  #initialize Bugout bag
    
def Deposit(bag_name):
    global total
    global rand
    global s
    if bag_name == "":      #if no bag name entered, assign name
        bag_name = "Unnamed Bag #"+str(rand)
        rand+=1
        print("Un-named bag was named: "+bag_name)
    
    if len(s.split()) != 4:  #handle wrong number of coins input
        print("Error: Could not determine number of coins.\nBag Not Deposited.")
        return
    elif (change[0].isdigit()==False) or (change[1].isdigit()==False) or (change[2].isdigit()==False) or (change[3].isdigit()==False):
        print("Invalid number.")
        return
    elif (int(change[0]) <0) or (int(change[1]) <0) or (int(change[2]) <0) or (int(change[3]) <0):
        print("Enter positive #s only.")
    else:
        print("Bag deposited")
            
    if bag_name in bags:    #determine total amount deposited from list of coins
        bagchange = bags[bag_name]  #add to existing bag
        ch = [int(change[0])+int(bagchange[0]), int(change[1])+int(bagchange[1]), int(change[2])+int(bagchange[2]), int(change[3])+int(bagchange[3])]
        bags[bag_name]=ch
    else:
        bags[bag_name]=change   #create new bag and deposit coins

def niceprint(makenice):
    global qs, ds, ns, ps
    if int(wd[0])==0:
        qs = ""
    elif int(wd[0])==1:
        qs = str(wd[0])+" quarter"
    else:
        qs = str(wd[0])+" quarters"
    
    if int(wd[1])==0:
        ds = ""
    elif int(wd[1])==1:
        ds = str(wd[1])+" dime"
    else:
        ds = str(wd[1])+" dimes"
        
    if int(wd[2])==0:
        ns = ""
    elif int(wd[2])==1:
        ns = str(wd[2])+" nickel"
    else:
        ns = str(wd[2])+" nickels"
        
    if int(wd[3])==0:
        ps = ""
    elif int(wd[3])==1:
        ps = str(wd[3])+" penny"
    else:
        ps = str(wd[3])+" pennies"

def Withdraw(bag_name):
    global wd
    if bag_name not in bags.keys():
        print("Bag does not exist.")
        return
    wd = bags[bag_name] #get list of coins
    niceprint(wd)
    print(qs+", "+ds+", "+ns+", "+ps+" "+"withdrawn.")
    bags.pop(bag_name)  #delete bag

def Transfer(from_bag, to_bag):
    if (from_bag not in bags.keys()) or (to_bag not in bags.keys()):
        print("Bag does not exist.")
        return
    frombag = bags[from_bag] 
    tobag = bags[to_bag]
    txfr = [int(frombag[0])+int(tobag[0]), int(frombag[1])+int(tobag[1]), int(frombag[2])+int(tobag[2]), int(frombag[3])+int(tobag[3])]
    bags[to_bag]=txfr  
    bags.pop(from_bag)  #delete withdrawn bag
    transferred = float(frombag[0])*0.25+float(frombag[1])*0.10+float(frombag[2])*0.05+float(frombag[3])*0.01
    print("${:.2f} Transferred.".format(transferred))
    
def Flee():
    subtotal = 0.0
    for k,v in (bags.items()):  
        amount = float(v[0])*0.25+float(v[1])*0.10+float(v[2])*0.05+float(v[3])*0.01
        if k=="Bugout Bag":
            global wd
            wd = v
        else:
            subtotal+=amount   #sum of bags except Bugout
    print("You have fled the country, leaving ${:.2f} behind.".format(subtotal))
    niceprint(wd)  
    print("You took "+qs+", "+ds+", "+ns+", "+ps+" "+"with you.") #coins in Bugout bag

while True:
    opt = input("> ")    
    
    if opt=="1":        #Balance Inquiry
        total=0.00
        sortprint={}

        for k,v in (bags.items()):      #find total of coins
            amount = float(v[0])*0.25+float(v[1])*0.10+float(v[2])*0.05+float(v[3])*0.01
            sortprint[k]=amount
            total+=amount        
            if len(k) > spacing:  #find length of longest bag name
                spacing = len(k)    
            if k=="Bugout Bag":         #print Bugout Bag first
                print(((spacing-len(k))*" ")+"{}: ${:.2f}".format(k, amount))
        d_sorted_by_value = OrderedDict(sorted(sortprint.items(),key=lambda x: x[1]))
        for k,v in (d_sorted_by_value.items()):     #sort remaining bags for printing
            if len(k) > spacing:  #find length of longest bag name
                spacing = len(k)
            if k=="Bugout Bag":
                pass
            else:
                print(((spacing-len(k))*" ")+"{}: ${:.2f}".format(k, v))
        print("-"*(spacing+1)+"\n"+(" "*(spacing-5))+"Total: ${:.2f}".format(total))
        
    elif opt=="2":      #Deposit
        bag_name = input("Enter name of deposited bag: ")
        s = input("Enter number of quarters, dimes, nickels, and pennies: ")
        change = s.split()
        if len(bag_name) > spacing:  #find length of longest bag name
                spacing = len(bag_name)
        Deposit(bag_name)
                
    elif opt=="3":      #Transfer
        from_bag = input("Enter name of bag to transfer from: ")
        to_bag = input("Enter name of bag to transfer into: ")
        Transfer(from_bag, to_bag)
        
    elif opt=="4":      #Withdrawal
        bag_name = input("Enter name of bag to withdraw: ")
        Withdraw(bag_name)
    
    elif opt=="5":      #Flee the Country
        Flee()
        ex = input("Exit program? (Y or N) ")
        if ex =='y' or ex=='Y':
            exit(1)
        else:
            pass
    
    else: print(menu)
