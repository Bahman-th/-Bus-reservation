from tkinter import *
import csv
f=open('customers list.txt','a')
# log defining=========================================================================================
def admin():
    fname = fn_entry.get()
    lname = ln_entry.get()
    if fname == 'admin' and lname == 'admin':
        def add_trip():
            with open('/Users/hesam/Desktop/reservation/all-trips-main.txt','a') as (trip_list2):
                writer = (csv.writer(trip_list2))
                writer.writerow([start,end,time,sit_count])
        def remove_trip():
            lines=list()
            with open('/Users/hesam/Desktop/reservation/all-trips-main.txt','a') as (file):
                reader = csv.reader(file)
                for row in reader:
                    lines.append(row)
                    if row[0] == start and row[1] == end:
                        lines.remove(row)

        res.destroy()
        admin_win = Tk()
        admin_win.title("Admin Pannel")
        admin_win.minsize(550,300)
        admin_win.maxsize(550,300)
        admin_greet = Label(admin_win, text = "Wellcome dear admin\nlong-time no see ...!").pack()

        start = Entry(admin_win)
        start.pack()
        start = start.get()
        end = Entry(admin_win)
        end.pack()
        end = end.get()
        time = Entry(admin_win)
        time.pack()
        time = time.get()
        sit_count = Entry(admin_win)
        sit_count.pack()
        sit_count = sit_count.get()


        add_button = Button(admin_win, text = "Add trip", command = add_trip).pack()
        remove_trip = Button(admin_win, text = "Remove trip", command = remove_trip).pack()

        admin_win.mainloop()
def sign_up():
    fname = fn_entry.get()
    lname = ln_entry.get()
    with open ('/Users/hesam/Desktop/reservation/customers list.txt','a') as file:
        writer = csv.writer(file)
        writer.writerow([fname,lname,'n']+'\n')
    res.destroy()
def log_in():
    print('slhfgkdf')
    finame = fn_entry.get()
    laname = ln_entry.get()
    file = open('/Users/hesam/Desktop/reservation/customers list.txt')
    data = list(csv.reader(file))
    for raw in data:
        
        if raw[1] == laname and raw[0] == finame:
            res.destroy()
        else:
            print('zjshbdfhjkabsf')
    file.close()

# menu difining ===================================================================================

def show_res(fname,lname):
    A = 0
    file = open ('/Users/hesam/Desktop/reservation/customers list.txt','r')
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
            
# log loop ========================================================================================

res = Tk()

res.minsize(550,300)
res.maxsize(550,300)
res.title('Login Sign up')
name_label = Label(res, text = 'First Name:').pack()

fn_entry = Entry(res)
fn_entry.pack()
Lastname_label = Label(res, text = 'Last Name:').pack()
ln_entry = Entry(res)
ln_entry.pack()

frame = Frame(res)
frame.pack()

admin_button = Button(res, text = 'Log in as\nadmin', command = admin).pack()
si_button = Button(res, text = 'Log In', width = 7, command = log_in)
si_button.pack()
su_button = Button(res, text = 'Sign Up', width = 7, command = sign_up)
su_button.pack()
quit_button = Button(res, text = 'Quit', fg = 'red', command = quit).place(x=0,y=0)

na_account_label = Label(res, text = " We couldn't find your account\nPlease make one first!", fg = 'red')
greet_label = Label(res, text = '\n\nWellcome To My Bus-reservation service\nThis project \
has been developed to sooth The reserving service\nand take a good score too ...' ).pack()

#if flag == True:
 #   res.destroy()
res.mainloop()

# menu loop =======================================================================================

menu_win = Tk()
menu_win.title('Reservation')
menu_win.minsize(550,300)
fname='fn_entry.get()'
lname='ln_entry.get()'
show_res_button = Button(menu_win, text = 'show Reserves', command = show_res(fname,lname))

start_label = Label(menu_win, text = 'start location:\ntehran\nmashad\nrasht')
start_label.pack()
start_entry = Entry(menu_win, width = 10)
start_entry.pack()
stop_label = Label(menu_win, text = 'stop location:\nshiraz\nmashhad\nrasht\nalborz\nesfahan\nghazvin')
stop_label.pack()
start_entry.pack()
end_entry = Entry(menu_win, width = 10)
end_entry.pack()

start_button = Button(menu_win, text = 'Search',command = find_trip)
start_button.pack()

menu_win.mainloop()