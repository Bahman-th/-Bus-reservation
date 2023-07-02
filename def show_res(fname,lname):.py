def show_res(fname,lname):
    file = open (('/Users/hesam/Desktop/reservation/customers list.txt','r'))
    reader = list(csv.reader(file))
    for item in reader:
        if item[0] == fname and item[1] == lname:
            A = item[3]
    res_label = Label(menu_win, text = A).place(x = 0, y = 0)

def find_trip():
    start = start_entry.get()
    stop = end_entry.get()
    flag = False
    with open('/Users/hesam/Desktop/reservation/all-trips-main.txt','r') as (trip_list):
        reader = list(csv.reader(trip_list))
        for item in reader:
            if item[0] == start and item[1] == stop and item[3] != '0':
                trip_label = Label(menu_win, text = 'The ('+item[0]+' To '+item[1]+')trip, moves at '+item[2]+' and has '+item[3]+' sits available')
                trip_label.pack()
                submit_button = Button(menu_win, text = 'Reserve This Trip', command = reserve)
                submit_button.pack()
                flag = True
        if flag == False:
            error_label = Label(menu_win, text = 'No sits Available for '+item[0]+' to '+item[0]+' trip!')
        
def reserve():
    start = start_entry.get()
    stop = end_entry.get()
    trip_list1 = ('/Users/hesam/Desktop/reservation/all-trips-main.txt','r')
    reader = list(csv.reader(trip_list1))
    for item in reader:
        if item[0] == start and item[1] == stop:
            trip_list1.close()
            with open('/Users/hesam/Desktop/reservation/all-trips-main.txt','a') as (trip_list2):
                writer = list(csv.writer(trip_list2))
                item[3] = int(item[3])-1
                print(item[3])