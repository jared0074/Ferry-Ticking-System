import time,pickle
from datetime import date
today = date.today()

#Saving list in a data copy

def saving():
    global dataB,dataE
    try:
        dataB = pickle.load(open('datab.txt','rb'))
        dataE = pickle.load(open('datae.txt','rb'))
    except:
        seat_b = [[0 for seat in range(10)]for ferry in range (8)]
        pickle.dump(seat_b, open('datab.txt','wb'))
        seat_e = [[0 for seat in range(40)]for ferry in range (8)]
        pickle.dump(seat_e, open('datae.txt','wb'))
        dataB = pickle.load(open('datab.txt','rb'))
        dataE = pickle.load(open('datae.txt','rb'))
        
#The Interface of Main Menu
        
def main_menu ():
    print ('='*26+"\n| FERRY TICKETING SYSTEM |\n"+'='*26+'\n')
    print ('='*74+"\n"+"| DATE: "+str(today)+" "*55+"|"+"\n"+'-'*73+"|")
    print ("| TIMETABLE : PENANG to LANGKAWI    |   TIMETABLE : LANGKAWI to PENANG   |"+"\n"+'-'*73+"|")
    print ("|   FERRY ID         TIME           |   FERRY ID         TIME            |")
    print ("|     001           10 a.m.         |     002           11 a.m.          |")
    print ("|     003           12 p.m.         |     004            1 p.m.          |")
    print ("|     005            2 p.m.         |     006            3 p.m.          |")
    print ("|     007            4 p.m.         |     008            5 p.m.          |"+"\n"+"="*74,'\n')
    print ("Type P - TO PURCHASE TICKETS\n"+"Type V - TO VIEW SEAT ARRANGEMENTS\n"+"Type Q - TO QUIT THE SYSTEM")
    user_input = str(input("PLEASE ENTER AN OPTION\n"))
    if (user_input.upper() == 'P'):
        submenu ()
    elif (user_input.upper() == 'Q'):
        quit_m()
    elif (user_input.upper() == 'V'):
        view_seat()
    else:
        print ("PLEASE ENTER A VALID OPTION!")
        main_menu()
        
#The Interface of Submenu After user input P
        
def submenu ():
    print ('='*21+"\n| PURCHASING MODULE |\n"+'='*21+"\n\nType B - TO PURCHASE TICKET FOR BUSINESS CLASS")
    print ("TYPE E - TO PURCHASE TICKETS FOR ECONOMY CLASS")
    print ("TYPE M - TO RETURN TO MAIN MENU\n")
    user_input1 = str(input("PLEASE ENTER AN OPTION\n"))
    if (user_input1.upper() == 'B'):
        b_class()
        ticket_p ()
    elif (user_input1.upper() == 'E'):
        e_class()
        ticket_p ()
    elif (user_input1.upper() == 'M'):
        main_menu()
    else:
        print ("PLEASE ENTER A VALID OPTION!")
        submenu()
        
#Business Class Arrangement
        
def b_class():
    global ferry_selection,seat_selection,seat,seat_class,time,des
    seat = 'BUSINESS CLASS'
    seat_class = 'B'
    saving()
    while True:
        ferry_selection = int(input("PLEASE CHOOSE A FERRY (1-8)\n"))
        if (ferry_selection%2) == 0:
            des = "LANGKAWI TO PENANG"
        else:
            des = "PENANG TO LANGKAWI"
        time = str(ferry_selection + 9)+':00'
        if (ferry_selection>0 and ferry_selection<9):
            if not 0 in dataB[ferry_selection - 1]:
                print ("BUSINESS CLASS IS FULL, PLEASE CHOOSE ANOTHER FERRY.")
                while True:
                    user_input2 = str(input("DO YOU WISH TO PICK ANOTHER FERRY? (Y/N)\n"))
                    if user_input2.upper() == 'Y':
                        return b_class()
                        break
                    elif user_input2.upper() == 'N':
                        quit_m()
                        break
                    else:
                        print("PLEASE ENTER A VALID OPTION!")
            else:
                B = 0
                print ('='*20+"\n|  "+seat+"  |\n"+'='*20+"\n")
                print ("="*61+"\n| FERRY: "+str(ferry_selection).zfill(3)+" "*16+"DESTINATION: "+des+" |\n"+"-"*61)
                print ("| DATE: "+str(today)+" "*20+"DEPARTURE TIME: "+time+" |\n"+"-"*61)
                for i in range (1,3):
                    print ("|"+" "*59,end="|\n|    ")
                    for i in range (1,6):
                        B = B + 1
                        print ("B"+str(B).zfill(2),end = " "*3)
                        print (str(dataB[ferry_selection - 1][B-1]),end = " "*4)
                    print("|")
                print ("|"+" "*59+"|\n"+"-"*61+"\n| AVAILABLE = 0"+" "*32+"OCUPPIED = 1 |\n"+"="*61)
                break
        else:
            print("PLEASE RECHOOSE YOUR FERRY!")
            continue       
    while True:
        seat_selection = int(input("\nPLEASE CHOOSE YOUR SEAT (1-10)\n"))
        if (seat_selection>0 and seat_selection<11):
            if (dataB[ferry_selection - 1][seat_selection-1] == 0):
                dataB[ferry_selection - 1][seat_selection-1] = 1
                break
            elif (dataB[ferry_selection - 1][seat_selection-1] == 1):
                print ("SORRY THIS SEAT HAS BEEN CHOSEN, PLEASE PICK ANOTHER ONE!")
                continue
        else:
            print ("PLEASE ENTER A VALID OPTION")
            continue
    pickle.dump(dataB, open('datab.txt','wb'))
    
#Economic Class Arrangement
    
def e_class():
    global ferry_selection,seat_selection,seat,seat_class,time,des
    seat = 'ECONOMIC CLASS'
    seat_class = 'E'
    saving()
    while True:
        ferry_selection = int(input("PLEASE CHOOSE A FERRY (1-8)\n"))
        if (ferry_selection%2) == 0:
            des = "LANGKAWI TO PENANG"
        else:
            des = "PENANG TO LANGKAWI"
        time = str(ferry_selection + 9)+':00'
        if (ferry_selection>0 and ferry_selection<9):
            if not 0 in dataE[ferry_selection - 1][0:40]:
                print ("ECONOMIC CLASS IS FULL, PLEASE CHOOSE ANOTHER FERRY.")
                while True:
                    user_input2 = str(input("DO YOU WISH TO PICK ANOTHER FERRY? (Y/N)"))
                    if user_input2.upper() == 'Y':
                        break
                    elif user_input2.upper() == 'N':
                        quit_m()
                        break
                    else:
                        print("PLEASE ENTER A VALID OPTION!")
            else:
                E = 0
                print ('='*20+"\n|  "+seat+"  |\n"+'='*20+"\n")
                print ("="*61+"\n| FERRY: "+str(ferry_selection).zfill(3)+" "*16+"DESTINATION: "+des+" |\n"+"-"*61)
                print ("| DATE: "+str(today)+" "*20+"DEPARTURE TIME: "+time+" |\n"+"-"*61)
                for i in range (1,9):
                    print ("|"+" "*59,end="|\n|    ")
                    for i in range (1,6):
                        E = E + 1
                        print ("E"+str(E).zfill(2),end = " "*3)
                        print (str(dataE[ferry_selection - 1][E-1]),end = " "*4)
                    print("|")
                print ("|"+" "*59+"|\n"+"-"*61+"\n| AVAILABLE = 0"+" "*32+"OCUPPIED = 1 |\n"+"="*61)
                break
        else:
            print("PLEASE RECHOOSE YOUR FERRY!")
            continue
    while True:
        seat_selection = int(input("\nPLEASE CHOOSE YOUR SEAT (1-40)\n"))
        if (seat_selection>0 and seat_selection<41):
            if (dataE[ferry_selection - 1][seat_selection-1] == 0):
                dataE[ferry_selection - 1][seat_selection-1] = 1
                break
            elif (dataE[ferry_selection - 1][seat_selection-1] == 1):
                print ("SORRY THIS SEAT HAS BEEN CHOSEN, PLEASE PICK ANOTHER ONE!")
                continue
        else:
            print ("PLEASE ENTER A VALID OPTION!")
            continue
    pickle.dump(dataE, open('datae.txt','wb'))
    
#Printing Ticket for the user
    
def ticket_p():
    ticket = open('ticketprinting.txt','w')
    customer_name = str(input("PLEASE ENTER YOUR NAME\n"))
    print("\nTHANK YOU FOR YOUR PURCHASE, HOPE TO SEE YOU SOON!\n\n"+"HERE IS THE TICKET\n")
    ticket.write(' '.ljust(3)+'_'*54+' '*4+'\n'+' ./'+' '*54+'\.'+'\n'+' | '+'='*18+' BOARDING  TICKET '+'='*18+' |\n')
    ticket.write(' |'+' DATE: '+str(today)+'  '.ljust(17)+"DEPARTURE TIME: "+time+' |'+'\n |'+' '*56+'|\n')
    ticket.write(' |'+" DESTINATION: "+des+' '*24+'|\n'+' |'+' '*56+'|\n'+' |'+' NAME :'+customer_name.upper().ljust(49)+'|')
    ticket.write('\n |'+' CLASS:'+seat.upper().ljust(49)+'|\n'+' |'+' SEAT :'+seat_class+str(seat_selection).ljust(37))
    ticket.write(' FERRY:'+str(ferry_selection).zfill(3)+' |\n'+' .\_'+'_'*53+'/.\n')
    ticket.close()
    ticket = open('ticketprinting.txt','r')
    for i in ticket:
        print (i,end = "")
    while True:
        re_purchase = str(input("\nDO YOU WANT TO PURCHASE ANOTHER TICKET? (Y/N)\n"))
        if (re_purchase.upper() == 'Y'):
            return main_menu()
            break
        elif (re_purchase.upper() == 'N'):
            return quit_m()
            break
        else:
            print("PLEASE ENTER A VALID OPTION")
            continue
        
#Viewing Seats after user enter V
        
def view_seat():
    saving()
    ferry_selection = int(input("PLEASE CHOOSE A FERRY TO VIEW (1-8)\n"))
    if (ferry_selection%2) == 0:
        des = "LANGKAWI TO PENANG"
    else:
        des = "PENANG TO LANGKAWI"
    time = str(ferry_selection + 9)+':00'
    B = 0
    print ('='*61+"\n|  "+"BUSINESS CLASS"+"  |"+" "*40+"|\n"+'='*20+" "*40+"|"+"\n"+"|"+" "*59+"|")
    print ("="*61+"\n| FERRY: "+str(ferry_selection).zfill(3)+" "*16+"DESTINATION: "+des+" |\n"+"-"*61)
    print ("| DATE: "+str(today)+" "*20+"DEPARTURE TIME: "+time+" |\n"+"-"*61)
    for i in range (1,3):
        print ("|"+" "*59,end="|\n|    ")
        for i in range (1,6):
            B = B + 1
            print ("B"+str(B).zfill(2),end = " "*3)
            print (str(dataB[ferry_selection - 1][B-1]),end = " "*4)
        print("|")
    print ("|"+" "*59+"|")
    E = 0
    print ('='*61+"\n|  "+"ECONOMIC CLASS"+"  |"+" "*40+"|"+"\n"+'='*20+" "*40+"|")
    print ("|"+" "*59+"|\n"+"="*61)
    for i in range (1,9):
        print ("|"+" "*59,end="|\n|    ")
        for i in range (1,6):
            E = E + 1
            print ("E"+str(E).zfill(2),end = " "*3)
            print (str(dataE[ferry_selection - 1][E-1]),end = " "*4)
        print("|")
    print ("|"+" "*59+"|\n"+"-"*61+"\n| AVAILABLE = 0"+" "*32+"OCUPPIED = 1 |\n"+"="*61)
    while True:
        continue_p = str(input("\nWOULD YOU LIKE TO CONTINUE PURCHASING TICKETS? (Y/N)\n"))
        if continue_p.upper() == 'Y':
            main_menu()
            break
        elif continue_p.upper() == 'N':
            quit_m()
            break
        else:
            print ("PLEASE ENTER A VALID OPTION!")
            continue
        
#quit module
        
def quit_m ():
    q = str(input("ARE YOU SURE YOU WANT TO QUIT (Y/N)\n"))
    if q.upper() == 'Y':
        print("PLEASE REVISIT SOON!")
        exit()
    elif q.upper() == 'N':
        return main_menu()
    else:
        print ("PLEASE ENTER A VALID OPTION!")
        return quit_m()

main_menu()

                          
