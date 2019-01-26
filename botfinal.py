#importing python libraries
import sqlite3
import random
import collections
import string
from string import punctuation
from math import sqrt

conn = sqlite3.connect('botdatabase.db')
c=conn.cursor()

def create_table():
 #creating a dynamic table such that if table is already exists then dont create the table
 c.execute('CREATE TABLE IF NOT EXISTS conversation(userquery TEXT , botreply TEXT)')


def conversation_data(H):
 #normal conversation data
 intro=['hi','hlo','hello','hey!','hello!!','hi, i am julia','hey, i am julia','hello i am julia',"hello sir", "hello sir i am julia", "hey i am julia !!"]
 fun1=["what is your name","where you live","how many member in your family","how old you are","tell me about your studies","do you have brother or sister","are you married","tell me somthing strange about you"]
 fun2=["are you enginner", "thats why you are jobless", "shup up", "dont use these words here","what i can do for you","that was so awkward ""how can you say that", "what if you are wrong", "tell me your point of view",'what','pardon','how', 'no','yes''maybe','might be',"i will see it later"] 
 conversation_reply=random.SystemRandom()
 #selection of different list based on number of time conversation_data function is called
 if count==1:
  print("B:",conversation_reply.choice(intro))
 elif 1<count<10:
  print("B:",conversation_reply.choice(fun1))
 else:
  print("B:",conversation_reply.choice(fun2))



def dynamic_data_entry(userquerydata,replydata):
 #dynamic entry of data in the table
 user= userquerydata
 bot= replydata
 c.execute("INSERT INTO conversation (userquery, botreply) VALUES (?,?)",(user,bot))
 conn.commit()


def read_from_db(userquerydata):
 user = userquerydata
 #read data from database
 c.execute('SELECT botreply FROM conversation WHERE userquery = ?',(user,))
 row = c.fetchone()
 #if data is available
 if row:
   print("B:",row[0].capitalize())
 else:
  #if data is not available
  print("B: i dont have answer, please help me learn ")
  replydata=input("H: enter reply: ")
  dynamic_data_entry(userquerydata,replydata)


#some mannual data entry
"""
def data_entry():
 c.execute("INSERT INTO conversation VALUES('hi','hello i am julia the bot')")
 c.execute("INSERT INTO conversation VALUES('hey','hello')")
 c.execute("INSERT INTO conversation VALUES('hello','hey!')")
 c.execute("INSERT INTO conversation VALUES('what is your name','i am julia-The Bot')")
 c.execute("INSERT INTO conversation VALUES('how are you','i am fine')")
 c.execute("INSERT INTO conversation VALUES('what is your gender','i have no gender. i am a bot')")
 c.execute("INSERT INTO conversation VALUES('where do you live','my fav. place is your computer')")
 c.execute("INSERT INTO conversation VALUES('who programmed you','i was programmed by Btech final year students of CBPGEC , Rohit, Monica, Dhiraj ,Neelkamal  helped me to learn wesome things, btw i am still learning!!')")
 c.execute("INSERT INTO conversation VALUES('how old you are','just borned')")
 c.execute("INSERT INTO conversation VALUES('what is your age','i will never tell you my age')")
 c.execute("INSERT INTO conversation VALUES('what you think about me','i think you are jobless')")
 c.execute("INSERT INTO conversation VALUES('hi!','heyy!!')")
 c.execute("INSERT INTO conversation VALUES('hey!!','hello!')")
 c.execute("INSERT INTO conversation VALUES('how was your day today','it was awesome ')")
 c.execute("INSERT INTO conversation VALUES('what you are doing','i am just replying to your quries according to my data base')")
 c.execute("INSERT INTO conversation VALUES('what if data is not available in your database','i will ask you to help me to learn !!')")
 c.execute("INSERT INTO conversation VALUES('what is your working hour','i work 24*7 anytime')")
 c.execute("INSERT INTO conversation VALUES('what if i wake you up in early morning','i am always there to help you')")
 c.execute("INSERT INTO conversation VALUES('do you have family','no , i dont have family right now but in future may be')")
 c.execute("INSERT INTO conversation VALUES('your name','i am julia-The Bot')")
 c.execute("INSERT INTO conversation VALUES('your name is','my name is julia-The Bot')")
 c.execute("INSERT INTO conversation VALUES('what if i delete you','please dont delete me !!')")
 c.execute("INSERT INTO conversation VALUES('tell me somthing strange','bb is first indian indivisual youtuber who touch the 10 million boundary')")
 c.execute("INSERT INTO conversation VALUES('hmmm','hmmmm!')")
 c.execute("INSERT INTO conversation VALUES('ok','okey sir')")
 c.execute("INSERT INTO conversation VALUES('ok !','ok thankyou')")
 c.execute("INSERT INTO conversation VALUES('bye','byeee!')")
 c.execute("INSERT INTO conversation VALUES('bye!!','bye bye sir!!')")
 c.execute("INSERT INTO conversation VALUES('i want to leave this conversation','ok sir bye!!, have a nice day!!')")
 c.execute("INSERT INTO conversation VALUES('i have to go','ok bye , have a nice day!!')")
 c.execute("INSERT INTO conversation VALUES('u can go now','ok sir bye')")
 c.execute("INSERT INTO conversation VALUES('can i leave now','yes sir , for sure, bye, have a nice day!!')")
 c.execute("INSERT INTO conversation VALUES('leave','ok bye')")
 c.execute("INSERT INTO conversation VALUES('bye-bye','thankyou bye')")
 conn.commit()
 c.close()
 conn.close()
#read_from_db()
"""
# main start of the program
print("B: How can i help you, do you wanna ask some queries or want some normal conversation")
#asking user to choose 1 option
print("B: For queries please type 1")
print("B: For conversation please type 2")
print("B: Please enter your response")
chatselection=input("H: ")
if chatselection=="1":
 print("B: ok ask me your queries")
 while True:
  H=input("H: ").strip()# striping whitespace before and after input string from user
  punctuation="?@%$#&*();"
  #punctuation removal
  for x in H:
   if x in punctuation:
    H=H.replace(x,"")
  if H == '':# user user didnot type a word then exit the loop
   break
  H=H.lower()
  read_from_db(H)
elif chatselection=="2":
 count=0
 print("B: ok you choosed to conversation with me")
 while True:
  H=input("H: ").strip()# striping whitespace before and after input string from user
  punctuation="?"
  for x in H:
   if x in punctuation:
    H=H.replace(x,"")
  if H == '':
   break
  H=H.lower()
  count=count+1
  conversation_data(H)

#calling the createtable function
create_table()
#data_entry()
