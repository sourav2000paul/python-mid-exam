from collections import defaultdict
class Star_Cinema:
    __hall_list=[]

    def entry_hall(item):
        Star_Cinema.__hall_list.append(item)

class Hall(Star_Cinema):
    def __init__(self,row,cols,hall_no) -> None:
        self.seats={}
        self.show_list=[]
        self.row=row
        self.cols=cols
        self.hall_no=hall_no
        Star_Cinema.entry_hall(self)
        print(f'This is {self.hall_no} with seats:{row}/{cols}')


    def entry_show(self,id,movie_name,time):
        self.seats.update(defaultdict(int,{id:[[0 for i in range(self.cols)] for j in range(self.row)]}))
        self.show_list.append((id,movie_name,time))
        print(f'{movie_name} is added successfully!')


    def book_seat(self,id,row,col):
        if row>=len(self.seats[id]) or col>=len(self.seats[id][1]):
           print('Invalid index')
           return
        else:
            if self.seats[id][row-1][col-1]==0:
                self.seats[id][row-1][col-1]=1
                print(f'Congratulations ! {row},{col}seat is booked successfully with {id}')
                return
            else:
                print("Seat is booked by someone")
                return


    def view_show_list(self):
        for item in self.show_list:
            print(f'MOVIE NAME:{item[1]} SHOW ID:{item[0]} TIME : {item[2]}')
      
           
    def view_available_seats(self,id):
                  
        if id not in self.seats:
            print(f'This {id} show is not available ')
        else:
            for item in self.seats[id]:
                print(item)





hal=Hall(6,5,'abc')
hal.entry_show(111,'Javan','20/10/2024 10:00 PM')
hal.entry_show(333,'kabir singh','22/10/2024 5:00 PM')
print(hal.show_list)
run=True
current_hall=hal
while run:
    print('1 : VIEW ALL SHOW TODAY')
    print('2 : VIEW AVAILABLE SEATS ')
    print('3 : BOOK TICKET')
    print('4 : EXIT')

    ch=int(input("ENTER OPTION: "))

    if ch==1:
        hal.view_show_list()
    elif ch==2:
        id=int(input('ENTER SHOW ID: '))
        hal.view_available_seats(id)
    elif ch==3:
        id=int(input('SHOW ID: '))
        if id not in hal.seats:
           
            print(f'This {id} show is not available!!')
            
        else:
            tkt_num=int(input('NUMBER OF TICKET: '))
            for i in range(tkt_num):
                row=int(input('ENTER SEAT ROW: '))
                col=int(input('ENTER SEAT COLOMN: '))
                hal.book_seat(id,row,col)
                flag=True
           
        
        
    elif ch==4:
        break