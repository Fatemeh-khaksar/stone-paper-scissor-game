from select import select
from tkinter import *
from turtle import width
from random import randint

win =Tk()

select={
    1:'stone',
    2:'paper',
    3:'scissor'
}

def stone():
    comp=randint(1,3)
    lb['text']='computer selection:'+select[comp]

    if comp==2:
        lbResultComputr['text']=int(lbResultComputr['text'])+1
    elif comp ==3:
        lbResultUser['text']=int(lbResultUser['text'])+1

def paper():
    comp=randint(1,3)
    lb['text']='computer selection:'+select[comp]

    if comp==3:
        lbResultComputr['text']=int(lbResultComputr['text'])+1
    elif comp ==1:
        lbResultUser['text']=int(lbResultUser['text'])+1

def scissor():
    comp=randint(1,3)
    lb['text']='computer selection:'+select[comp]

    if comp==1:
        lbResultComputr['text']=int(lbResultComputr['text'])+1
    elif comp ==2:
        lbResultUser['text']=int(lbResultUser['text'])+1

def reset():
    lbResultComputr['text']=0
    lbResultUser['text']=0
    lb['text']='Select'


win.title('ston,paper,scissor')
win.minsize(300,400)

win.rowconfigure([0,1],weight=1)
win.columnconfigure(0,weight=1)

lb=Label(master=win,text='select',bg='#fff',height=2,font=('None', 18, 'bold'))
lb.grid(row=0,column=0,sticky='nwe')

frmbtn=Frame(master=win ,height=100, bg='red')

frmbtn.rowconfigure(0,weight=1)
frmbtn.columnconfigure([0,1,2],weight=1)

stonbtn=Button(master=frmbtn,text='stone',height=2,font=('None',18,'bold'),command=stone).grid(row=0,column=0,sticky='nwes',padx=2,pady=3)
paperbtn=Button(master=frmbtn,text='paper',height=2,font=('None',18,'bold'),command=paper).grid(row=0,column=1,sticky='nwes',padx=2,pady=3)
scissorbtn=Button(master=frmbtn,text='scissor',height=2,font=('None',18,'bold'),command=scissor).grid(row=0,column=2,sticky='nwes',padx=2,pady=3)

frmbtn.grid(row=1,column=0,sticky='wen')

frmresult=Frame(master=win,height=200)
frmresult.rowconfigure([0,1],weight=1)
frmresult.columnconfigure([0,1],weight=1)

lbresultNameusre=Label(master=frmresult,text='your point',relief='ridge')
lbresultNameusre.grid(row=0,column=0,sticky='news')
lbresultNamecomputer=Label(master=frmresult,text='computer point',relief='ridge')
lbresultNamecomputer.grid(row=0,column=1,sticky='news')

lbResultUser=Label(master=frmresult,text='0',bg='red',fg='#fff',font=('None',40,'bold'),height=3)
lbResultUser.grid(row=1,column=0,sticky='nwes')
lbResultComputr=Label(master=frmresult,text='0',bg='blue',fg='#fff',font=('None',40,'bold'),height=3)
lbResultComputr.grid(row=1,column=1,sticky='nwes')

frmresult.grid(row=2,column=0,sticky='news')

btnResult=Button(master=win,text='start again',font=('None',18,'bold'),relief='ridge',borderwidth=4,command=reset).grid(row=3,column=0,sticky='nswe')

win.mainloop()