#!/bin/python

import os
import pyfiglet
######
os.system("pip install pyfiglet")
os.system("clear")
#####
ascii_banner = pyfiglet.figlet_format("ENCRYPTER")
print(ascii_banner)
####
print("-----------[ @Irfan_kpm ]------------\n\n")
def Encode():
   print("\n------ERROR---------")
   print("[#] USE CAPITEL LETTER")
   print("[#] DON'T USE NUMBER")
###
   A="m1n"
   B="mf5"
   C="ch3"
   D="5fd"
   E="cm3"
   F="2fg"
   G="km9"
   H="mf2"
   I="cd5"
   J="bc8"
   K="4km"
   L="kpm"
   M="ls7"
   N="cdh"
   O="xy4"
   P="qw7"
   Q="kk0"
   R="aa3"
   S="qw6"
   T="8m8"
   U="7mm"
   V="zz4"
   W="wn7"
   X="87s"
   Y="8sh"
   Z="fr1"
   output=""
   new="A"
   name=input("\nEnter word: ")
   list=["0","2","1","3","4","5",'6',"7","8","9","@","#","$","%","&","*","-","=","!","+","~",]
   if name.isupper()==True:   
      for i in name:
            if i in list:
            	new=name+"abc"
            if i =="A":
               output+=A
            if i == "B":
         	   output+=B
            if i =="C":
      	      output+=C
            if i == "D":
      	       output+=D
            if i =="E":
      	       output+=E
            if i == "F":
      	       output+=F
            if i =="G":
      	       output+=G
            if i == "H":
      	       output+=H
            if i =="I":
         	   output+=I
            if i == "J":
   	         output+=J
            if i =="K":
      	      output+=K
            if i == "L":
   	         output+=L
            if i =="M":
   	         output+=M
            if i == "N":
      	      output+=N
            if i =="O":
   	         output+=O
            if i == "P":
         	   output+=P
            if i =="Q":
         	   output+=Q
            if i == "R":
         	   output+=R
            if i =="S":
         	   output+=S
            if i == "T":
         	   output+=T
            if i =="U":
         	   output+=U
            if i == "V":
      	      output+=V
            if i =="W":
         	   output+=W
            if i == "X":
         	   output+=X
            if i =="Y":
         	   output+=Y
            if i == "Z":
      	      output+=Z
      
      
   	  
   else:
	   	print("[#]---ERROR DETECTED---")

   if name.isupper()==True:
     if new.isupper()==False:
     	print("---Wrong input--")
     else:
     	print("\n [#] Encrypted word : "+output)
  

   else:
   	print("---Wrong input---")
   	
   	
def Decode():
   print("\n------ERROR---------")
   print("[#] DON'T USE CAPITEL LETTER")
   print("[#] DON'T USE NUMBER")
###
   inp=input("\nEnter crypted word: ")
   output=""
   new="ba"
   
  
   m=len(inp)
   k=len(inp)//3
   
  
  
   for i in range(0,m,3):
       ans=inp[i:i+3]      
       
           
       list=["@","#","$","%","&","*","-","=","!","+","~",]
       if inp.isupper()==False:           
            if ans in list:
            	new=name+"AB"
            if ans=="m1n":
            	output=output+"A"            
            if ans== "mf5":
         	   output=output+"B"
            if ans=="ch3":
      	      output+="C"
            if ans == "5fd":
       	     output+="D"
            if ans =="cm3":
      	       output+="E"
            if ans== "2fg":
      	       output+="F"
            if ans=="km9":
      	       output+="G"
            if ans== "mf2":
      	       output+="H"
            if ans =="cd5":
         	   output+="I"
            if ans== "bc8":
   	         output+="J"
            if ans=="4km":
      	      output+="K"
            if ans == "kpm":
   	         output+="L"
            if ans=="ls7":
   	         output+="M"
            if ans== "cdh":
      	      output+="N"
            if ans=="xy4":
   	         output+="O"
            if ans == "qw7":
         	   output+="P"
            if ans=="kk0":
         	   output+="Q"
            if ans == "aa3":
         	   output+="R"
            if ans=="qw6":
         	   output+="S"
            if ans == "8m8":
         	   output+="T"
            if ans=="7mm":
         	   output+="U"
            if ans == "zz4":
      	      output+="V"
            if ans=="wn7":
         	   output+="W"
            if ans== "87s":
         	   output+="X"
            if ans=="8sh":
         	   output+="Y"
            if ans== "fr1":  
     	       output+="Z"
   n=len(output)
   if str(k)==str(n):
      print("\n\n[#] Decrypted word : "+output)


print(25*"-")	
print(" [00] EXIT")
print(" [1] ENCODE")
print(" [2] DECODE")
print(25*"-")
while True:
   ab=input("\n\nEnter your choice : ")   
   if ab=="00":
       print("----Exited---")
       break
   if ab=="1":
   	Encode()
   if ab=="2":
   	Decode()
   if int(ab)>=3:
	   print("\n\n-------Wrong input----")

