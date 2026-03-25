import pandas as pd
import os            # Lib installation for shutdown command
import easygui
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
# Program Startup for user
df1=pd.DataFrame()
m1=easygui.msgbox('Welcome to Trans-City Railway Online Platform (TCROP)')
msg = "Before Proceding, Please Login. \n Do you have a login id?"
choices=['Yes','Get Registered','Forgotten User ID','Cancel']
title = "Login TCROP"
check = easygui.buttonbox(msg, choices=choices)
if check=='Forgotten User ID':
    if easygui.ccbox("Sorry You have to register again for new id.\nDo you want to register now"):
        pass
        text='Please enter a username and password(minimum 8 characters)'
        title='Login'
        input_list=['Username :','Password:','Confirm Password :']
        m1=easygui.multenterbox(text,title,input_list)
        while m1[0] in df1 or m1[1] != m1[2]:
            if m1[0] in df1:
                text='Username already exist.\nPlease enter a re-enter username and password'
                title='Login'
                input_list=['Username :','Password :','Confirm Password :']
                m1=easygui.multenterbox(text,title,input_list)
            elif m1[1] != m1[2]:
                text='Password does not matched.\nPlease enter a re-enter username and password'
                title='Login'
                input_list=['Username :','Password :','Confirm Password :']
                m1=easygui.multenterbox(text,title,input_list)
        while (m1[0]=='' and m1[0] not in df1) or ((m1[1] == m1[2] and m1[1]=='' and m1[2]=='') or (m1[1] == m1[2] and len(m1[1])<8)):
            if m1[0]=='':
                text='Username can not be blank.\nPlease enter a re-enter username and password'
                title='Login'
                input_list=['Username :','Password :','Confirm Password :']
                m1=easygui.multenterbox(text,title,input_list)
            elif m1[1] == m1[2] and m1[1]==''and m1[1]=='':
                text='Password can not be blank.\nPlease enter a re-enter username and password'
                title='Login'
                input_list=['Username :','Password :','Confirm Password :']
                m1=easygui.multenterbox(text,title,input_list)
            elif m1[1] == m1[2] and len(m1[1])<8:
                text='Password should be less than 8 characters.\nPlease enter a re-enter username and password'
                title='Login'
                input_list=['Username :','Password :','Confirm Password :']
                m1=easygui.multenterbox(text,title,input_list)
        
        else:
            m2=easygui.msgbox('Thank You For Registering. You have been Registered')
    else:
        m0=easygui.msgbox('Thank You for visiting TCROP')
        exit()
        
    
elif check=="Get Registered":
    text='Please enter a username and password(minimum 8 characters)'
    title='Login'
    input_list=['Username :','Password:','Confirm Password :']
    m1=easygui.multenterbox(text,title,input_list)
    while m1[0] in df1 or m1[1] != m1[2]:
        if m1[0] in df1:
            text='Username already exist.\nPlease enter a re-enter username and password'
            title='Login'
            input_list=['Username :','Password :','Confirm Password :']
            m1=easygui.multenterbox(text,title,input_list)
        elif m1[1] != m1[2]:
            text='Password does not matched.\nPlease enter a re-enter username and password'
            title='Login'
            input_list=['Username :','Password :','Confirm Password :']
            m1=easygui.multenterbox(text,title,input_list)
    while (m1[0]=='' and m1[0] not in df1) or ((m1[1] == m1[2] and m1[1]=='' and m1[2]=='') or (m1[1] == m1[2] and len(m1[1])<8)):
        if m1[0]=='':
            text='Username can not be blank.\nPlease enter a re-enter username and password'
            title='Login'
            input_list=['Username :','Password :','Confirm Password :']
            m1=easygui.multenterbox(text,title,input_list)
        elif m1[1] == m1[2] and m1[1]==''and m1[1]=='':
            text='Password can not be blank.\nPlease enter a re-enter username and password'
            title='Login'
            input_list=['Username :','Password :','Confirm Password :']
            m1=easygui.multenterbox(text,title,input_list)
        elif m1[1] == m1[2] and len(m1[1])<8:
            text='Password should be less than 8 characters.\nPlease enter a re-enter username and password'
            title='Login'
            input_list=['Username :','Password :','Confirm Password :']
            m1=easygui.multenterbox(text,title,input_list)
        
    else:
        m2=easygui.msgbox('Thank You For Registering. You have been Registered')
   
elif check=='Cancel':
    m6=easygui.msgbox('Thanks For Visiting TCROP.\nPlease visit us again')
    exit()
else:
    text='Please enter the credentials'
    title='Login TCROP'
    input_list=['Username :','Password :']
    m3=easygui.multenterbox(text,title,input_list)
    if m3[0] in df1 and m3[1] in df1:
        m4=easygui.msgbox('Welcome ', m3[0])
    while m3[0] not in df1 or m3[1]  not in df1 :
        msg='Entered credentials was not found'
        choices=['Retry','Forgotten User ID','Get Registered','Cancel']
        title = "Login TCROP"
        check = easygui.buttonbox(msg, choices=choices)
        if check=='Retry':
            text='Please enter the credentials'
            title='Login TCROP'
            input_list=['Username :','Password :']
            m3=easygui.multenterbox(text,title,input_list)
            
        if check=='Forgotten User ID':
            if easygui.ccbox("Sorry You have to register again for new id.\nDo you want to register now"):
                pass
                text='Please enter a username and password(minimum 8 characters)'
                title='Login'
                input_list=['Username :','Password:','Confirm Password :']
                m1=easygui.multenterbox(text,title,input_list)
                while m1[0] in df1 or m1[1] != m1[2]:
                    if m1[0] in df1:
                        text='Username already exist.\nPlease enter a re-enter username and password'
                        title='Login'
                        input_list=['Username :','Password :','Confirm Password :']
                        m1=easygui.multenterbox(text,title,input_list)
                    elif m1[1] != m1[2]:
                        text='Password does not matched.\nPlease enter a re-enter username and password'
                        title='Login'
                        input_list=['Username :','Password :','Confirm Password :']
                        m1=easygui.multenterbox(text,title,input_list)
                while (m1[0]=='' and m1[0] not in df1) or ((m1[1] == m1[2] and m1[1]=='' and m1[2]=='') or (m1[1] == m1[2] and len(m1[1])<8)):
                    if m1[0]=='':
                        text='Username can not be blank.\nPlease enter a re-enter username and password'
                        title='Login'
                        inputt_list=['Username :','Password :','Confirm Password :']
                        m1=easygui.multenterbox(text,title,input_list)
                    elif m1[1] == m1[2] and m1[1]==''and m1[1]=='':
                        text='Password can not be blank.\nPlease enter a re-enter username and password'
                        title='Login'
                        input_list=['Username :','Password :','Confirm Password :']
                        m1=easygui.multenterbox(text,title,input_list)
                    elif m1[1] == m1[2] and len(m1[1])<8:
                        text='Password should be less than 8 characters.\nPlease enter a re-enter username and password'
                        title='Login'
                        input_list=['Username :','Password :','Confirm Password :']
                        m1=easygui.multenterbox(text,title,input_list)
                
                else:
                    m2=easygui.msgbox('Thank You For Registering. You have been Registered')
            else:
                m0=easygui.msgbox('Thank You for visiting TCROP')
                exit()
            
        
        elif check=="Get Registered":
            text='Please enter a username and password(minimum 8 characters)'
            title='Login'
            input_list=['Username :','Password:','Confirm Password :']
            m1=easygui.multenterbox(text,title,input_list)
            while m1[0] in df1 or m1[1] != m1[2]:
                if m1[0] in df1:
                    text='Username already exist.\nPlease enter a re-enter username and password'
                    title='Login'
                    input_list=['Username :','Password :','Confirm Password :']
                    m1=easygui.multenterbox(text,title,input_list)
                elif m1[1] != m1[2]:
                    text='Password does not matched.\nPlease enter a re-enter username and password'
                    title='Login'
                    input_list=['Username :','Password :','Confirm Password :']
                    m1=easygui.multenterbox(text,title,input_list)
            while (m1[0]=='' and m1[0] not in df1) or ((m1[1] == m1[2] and m1[1]=='' and m1[2]=='') or (m1[1] == m1[2] and len(m1[1])<8)):
                if m1[0]=='':
                    text='Username can not be blank.\nPlease enter a re-enter username and password'
                    title='Login'
                    input_list=['Username :','Password :','Confirm Password :']
                    m1=easygui.multenterbox(text,title,input_list)
                elif m1[1] == m1[2] and m1[1]==''and m1[1]=='':
                    text='Password can not be blank.\nPlease enter a re-enter username and password'
                    title='Login'
                    input_list=['Username :','Password :','Confirm Password :']
                    m1=easygui.multenterbox(text,title,input_list)
                elif m1[1] == m1[2] and len(m1[1])<8:
                    text='Password should be less than 8 characters.\nPlease enter a re-enter username and password'
                    title='Login'
                    input_list=['Username :','Password :','Confirm Password :']
                    m1=easygui.multenterbox(text,title,input_list)
                
            else:
                m2=easygui.msgbox('Thank You For Registering. You have been Registered')
        elif check=='Cancel':
            m5=easygui.msgbox('Thank You for visiting TCROP')
            exit()
#Registration Completes            
