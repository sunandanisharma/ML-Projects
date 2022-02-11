#!/usr/bin/env python
# coding: utf-8

# Alarm Clock-Python Mini

# In[12]:


from tkinter import *
import datetime , time , winsound


# In[13]:


def AClock(set_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("Enter your lucky date: ",date)
        print(now)
        if now == set_timer:
            print("wake up buddy")
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break

def actual_time():
    set_timer = f"{hour.get()}:{minu.get()}:{sec.get()}"
    AClock(set_timer)


# In[14]:


clock =Tk()
clock.title("Fairy Clock ")
clock.geometry("400x200")
time = format = Label(clock , text = "Enter hour is 24 hour format!" , fg = "black" , bg = "red" ,font = "Arial").place(x = 60 , y =120)
addTime = Label(clock , text = "Hour Min  Sec" , font = 80).place(x = 110)

setalarm = Label(clock , text = "Time to wake up!" , fg ="pink" , relief = "solid" , font = ("Arial " , 10 , "bold")).place(x=0 , y=29)

hour = StringVar()
minu = StringVar()
sec = StringVar()


# In[15]:


hourtime = Entry(clock , textvariable = hour ,bg = "pink" ,width =15).place(x=110 , y=30)
mintime = Entry(clock , textvariable = minu ,bg = "pink" ,width =15).place(x=150 , y=30)
sectime = Entry(clock , textvariable = sec ,bg = "pink" ,width =15).place(x=200 , y=30)


# In[16]:


submitt = Button(clock , text = "Set Alarm"  ,fg = "pink" ,width =10 , command = actual_time).place(x=110 , y=70)


# In[17]:


clock.mainloop()


# In[ ]:




