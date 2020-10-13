from tkinter import*
from tkinter.messagebox import*
import math as m

# creating a window
window=Tk()
window.title('My Calculator')
window.geometry('380x400')

#text label
headinglabel=Label(window , text='CALCULATOR' , font=('Courier New ' , 25 , 'bold'))
headinglabel.pack(side=TOP)

#Text field
textfield=Entry(window,font=('Courier new' , 16 , 'bold') , justify=CENTER)
textfield.pack(side=TOP , pady=10,padx=10 , fill=X)

#frame 
frame=Frame(window)
frame.pack(side=TOP)

#function
def click(event):
    b=event.widget
    text=b['text']
   

    if(text=='='):
        try:
            ex=textfield.get()
            answer=eval(ex)
            textfield.delete(0,END)
            textfield.insert(0,answer)
            
        except Exception as e:
            print('error',e)
            showerror('error',e)
        return
            
    textfield.insert(END , text)

def all_clr():
    textfield.delete(0,END)
    
def clr():
    ex=textfield.get()
    ex=ex[0:len(ex)-1]
    textfield.delete(0,END)
    textfield.insert(0,ex)

                         


#button
temp=1
for i in range(0,3):
    for j in range(0,3):
        btn=Button(frame , text=str(temp) , font=('Courier New', 16 , 'bold') ,width=5 ,bd=4)
        btn.grid(row=i , column=j , padx=5 , pady=5)
        temp+=1
        btn.bind('<Button-1>' ,click)

zerobtn = Button(frame , text='0' , font=('Courier New', 16 , 'bold') ,width=5 ,bd=4)
zerobtn.grid(row=3 , column=0 , padx=5 , pady=5)

dotbtn = Button(frame , text='.' , font=('Courier New', 16 , 'bold') ,width=5 ,bd=4)
dotbtn.grid(row=3 , column=1 , padx=5 , pady=5)

eqlbtn = Button(frame , text='=' , font=('Courier New', 16 , 'bold') ,width=5 ,bd=4)
eqlbtn.grid(row=3 , column=2 , padx=5 , pady=5)

addbtn = Button(frame , text='+' , font=('Courier New', 16 , 'bold') ,width=5 ,bd=4)
addbtn.grid(row=0 , column=3 , padx=5 , pady=5)

subbtn=Button(frame , text='-' , font=('Courier New', 16 , 'bold') ,width=5 ,bd=4)
subbtn.grid(row=1 , column=3 , padx=5 , pady=5)

mulbtn=Button(frame , text='*' , font=('Courier New', 16 , 'bold') ,width=5 ,bd=4)
mulbtn.grid(row=2 , column=3 , padx=5 , pady=5)

divbtn=Button(frame , text='/' , font=('Courier New', 16 , 'bold') ,width=5 ,bd=4)
divbtn.grid(row=3 , column=3 , padx=5 , pady=5)

clrbtn=Button(frame , text='<--' , font=('Courier New', 16 , 'bold') ,width=12 ,bd=4 , command =clr)
clrbtn.grid(row=4 , column=0  , pady=5 , columnspan=2)


allclrbtn=Button(frame , text='AC' , font=('Courier New', 16 , 'bold') ,width=5 ,bd=4 , command=all_clr)
allclrbtn.grid(row=4 , column=2 , padx=5 , pady=5)



#binding all button

addbtn.bind('<Button-1>' ,click)
subbtn.bind('<Button-1>' ,click)
mulbtn.bind('<Button-1>' ,click)
divbtn.bind('<Button-1>' ,click)
dotbtn.bind('<Button-1>' ,click)
eqlbtn.bind('<Button-1>' ,click)
zerobtn.bind('<Button-1>' ,click)


def enterClick(event):
    print('hi')
    e = Event()
    e.widget = equalBtn
    click(e)


textfield.bind('<Return>', enterClick)
#################################################################################


#function of scientific
scframe=Frame(window)

sqrtbtn=Button(scframe , text='√' , font=('Courier New', 16 , 'bold') ,width=5 ,bd=4 )
sqrtbtn.grid(row=0, column=0 )


powbtn=Button(scframe , text='^' , font=('Courier New', 16 , 'bold') ,width=5 ,bd=4)
powbtn.grid(row=0 , column=1 )

factbtn=Button(scframe , text='x!' , font=('Courier New', 16 , 'bold') ,width=5 ,bd=4 )
factbtn.grid(row=0 , column=2 )


radbtn=Button(scframe , text='rad' , font=('Courier New', 16 , 'bold') ,width=5 ,bd=4 )
radbtn.grid(row=0 , column=3 )


degbtn=Button(scframe , text='deg' , font=('Courier New', 16 , 'bold') ,width=5 ,bd=4 )
degbtn.grid(row=1 , column=0 )

sinbtn=Button(scframe , text='sinΘ' , font=('Courier New', 16 , 'bold') ,width=5 ,bd=4 )
sinbtn.grid(row=1 , column=1 )

cosbtn=Button(scframe , text='cosΘ' , font=('Courier New', 16 , 'bold') ,width=5 ,bd=4 )
cosbtn.grid(row=1 , column=2 )

tanbtn=Button(scframe , text='tanΘ' , font=('Courier New', 16 , 'bold') ,width=5 ,bd=4 )
tanbtn.grid(row=1 , column=3 )

normalcalc = True

def calculate_sc(event):
    print('btn..')
    btn = event.widget
    text=btn['text']
    print(text)
    ex=textfield.get()
    answer = ''

    if text == 'deg':
        answer=str(m.degrees(float(ex)))
    elif text == 'rad':
        answer=str(m.radians(float(ex)))
    elif text == 'x!':
        answer= str(m.factorial(int(ex)))
    elif text == 'sinΘ':
        answer = str(m.sin(m.radians(int(ex))))
    elif text == 'cosΘ':
        answer = str(m.cos(m.radians(int(ex))))
    elif text == 'tanΘ':
        answer= str(m.tan(m.radians(int(ex))))
    elif text == '√':
        answer= m.sqrt(int(ex))
    elif text == '^':
        print('pow')
        base,pow=ex.split('.')
        print(base)
        print(pow)
        answer=m.pow(int(base),int(pow))
   
               
    textfield.delete(0, END)
    textfield.insert(0, answer)
    

def sc_click():
    global normalcalc
    if normalcalc:
        frame.pack_forget()
        
        scframe.pack(side=TOP)
        
        frame.pack(side=TOP)
        window.geometry('380x500')
        print('scientific')
        normalcalc=False
    else:
        print('normal')
        scframe.pack_forget()
        window.geometry('380x400')
        normalcalc=True

    
    
#binding sc button
sqrtbtn.bind("<Button-1>", calculate_sc)
powbtn.bind("<Button-1>", calculate_sc)
radbtn.bind("<Button-1>", calculate_sc)
factbtn.bind("<Button-1>", calculate_sc)
degbtn.bind("<Button-1>", calculate_sc)
sinbtn.bind("<Button-1>", calculate_sc)
cosbtn.bind("<Button-1>", calculate_sc)
tanbtn.bind("<Button-1>", calculate_sc)

menubar=Menu(window)
mode=Menu(menubar , font=('',10) , tearoff=0)
mode.add_checkbutton(label='Scientific Calculator' , command=sc_click)
menubar.add_cascade(label='Mode' , menu=mode)
window.config(menu=menubar)


window.mainloop()
