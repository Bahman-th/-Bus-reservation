from tkinter import *
import csv
f=open('customers list.txt','a')
# defining============================================================================
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
# main win - mainloop===================================================================
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

