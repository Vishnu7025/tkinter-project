import tkinter
import tkinter.messagebox
t=tkinter.Tk()
t.title ('Profile')
t.geometry('500x500')
a=tkinter.Label(text="profile creation",bg="indigo",fg="white",font=('bradley hand itc',35,'bold')).place(x=90,y=0)
b=tkinter.Label(text="First name",bg="red",fg="white",font=('bradley hand itc',25,'bold')).place(x=50,y=100)
c=tkinter.Entry(width=30)
c.place(x=275,y=120)


d=tkinter.Label(text="Location",bg="red",fg="white",font=('bradley hand itc',25,'bold')).place(x=50,y=170)
e=tkinter.Entry(width=30).place(x=275,y=190)

def  abcd():
    name=c.get()
    place=e.get()
    import pymysql
    x=pymysql.connect(host='localhost',user='root',password='7025448550',db='vishnu')
    cur=x.cursor()
    cur.execute("insert into profile values('"+name+"','"+place+"')")
    x.commit()
    x.close()

    
    tkinter.messagebox.showinfo("Thank you",'Thanks for visiting')
    t.destroy()


f=tkinter.Button(text="submit",bg="blue",fg="white",font=('bradley hand itc',25,'bold'),command=abcd)
f.place(x=225,y=250)




t.mainloop()
