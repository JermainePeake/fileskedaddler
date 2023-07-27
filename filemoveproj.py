'''
#a program that moves files automatically
#this will depend on the criteria in which the files will be moved
#will it be moved by file type or file contents?
import shutil
#shutil.move(source,destination)
f = file
if f== .txt:
    shutil(.txt, folder)
elif f == .png:
    shutile(.png,fold)
elif f == .jpg:
    shutil(.jpg, fold)

strng = 'chitty chitty bang bang'
news = ''
for i in range(len(strng)):
    if strng[i] == 't':
        news += strng[i]

print(news)
        
#as of now, I assume she wants an executable python program, that when opened
#and run, will take each file of a certain type (.txt,.png,.jpg, etc) and move
#it to a designated folder
#or she wants the files moved based on there contents in which case I'll have
#to read from the file find whatever criteria within its contents, and move it
#based on that.

#realization: right, when offloading test logs from pcdr, they look for specific
#asset tags like ones that start with bbn6l1.
#so if I could just make something that says 'for the first 6 characters in a
#list of strings, if the first 6 are equal to 'bbn6l1', then move them to
#testlog folder
strn='bbn6l127'
strn='hunws12k'
strn='wafdldrd'
strn='bbn6l106'
strn='bbn6l123'
strn='wafdlxrd'
strn='huntingt'
strn='wafedera'
strn='bbn6l1xe'
lis=['bbn6l127','hunws12k','wafdldrd','bbn6l106','bbn6l123','wafdlxrd','huntingt','wafedera','bbn6l1xe']
lis2=[]
assettag= lis[0][:6]
print(assettag)
for i in range(len(lis)):
    if lis[i][:6]==assettag:
        lis2 += lis[i]
print(lis2)#spent maybe 45min-1hr

#she wants test logs and system files to move to designated folders

import shutil ###started at a lil after 8 (unable to work on this yesterday bc of things)
###also i used chatgpt below because i never learned about the r###
src=r"C:\Users\afron\OneDrive\Desktop\source\dingus22.txt"
dest=r"C:\Users\afron\OneDrive\Desktop\destination"
shutil.move(src,dest)
#this will move file 'dingus22.txt' to folder 'destination'
#we want the test logs from 'pcdr' to folder 'testlogs'
#now I will try moving multiple files


#this is what I gave to chatgpt
#in my defence, the class I took didn't bother to teach me alot about files
import shutil
for i in r"C:\Users\afron\OneDrive\Desktop\source"
    shutil.move(i,r"C:\Users\afron\OneDrive\Desktop\destination")
######################################################################
'''
import os#1
import shutil#2
#3
src_dir = r"C:\Users\afron\OneDrive\Desktop\source"#4
dest_dir = r"C:\Users\afron\OneDrive\Desktop\destination"#5
#6
for filename in os.listdir(src_dir):#7
    src = os.path.join(src_dir, filename)#8
    dest = os.path.join(dest_dir, filename)#9
    shutil.move(src, dest)#10
#os.listdir is a list of file names in a given directory (or folder) (src_dir is the given directory)
#line 8 is combining the path to the folder(line4) and the join method which is the item in the for loop
#line 9 does the same thing but with destination.
#for some reason this doesnt work here so I made another thingy and it did it
    
#now I think I have to account for if the source and destination are unknown
#I'm gonna put this inna function
#also if it had a way of verifying that the files have been successfully moved
#that would be lit
    
import os
import shutil

def filemove(src_,dest_):
    for filename in os.listdir(src_):
        src = os.path.join(src_, filename)
        dest = os.path.join(dest_, filename)
        shutil.move(src, dest)
filemove(r"C:\Users\afron\OneDrive\Desktop\source",r"C:\Users\afron\OneDrive\Desktop\destination")

##tried to run this in the command line and it didnt work but, when I run the first one in the command line
#it does work???
#chatgpt just explained it to me, python through the command line can only run one line at a time, so I need
#to write the code to a notepad and save it as a python file.
#It works! and I can open the file as notepad and edit it that way.
#I have to remember tho that for this to work, python needs to be installed on the computer, so at work, they have to let me do that I think?
#so some things about it, its basically an executable now, so when you run it, it works immediatelye
#when you edit the code, you have to save it and it stays that way until you edit it again.

#also to make this work they would have to copy and past over the new folders, which I think is mostly fine but
#there should be a way to optimize this.#now I think I have to account for if the source and destination are unknown

#also if it had a way of verifying that the files have been successfully moved
#that would be lit
