from tkinter import *
import random


politics_questions=[".Who was the first woman governor of India?",
                    ".The idea of Fundamental Rights in Indian Constitution was adopted from-",
                    ".Who is considered as the chief architect of the Indian Constitution?",
                    ".Who was the Prime Minister of India when emergency was declared?",
                    ".Who proposed the Preamble before the Drafting Committee of the Constitution?",
                    ".Who was the first Indian woman president of the UN General Assembly?",
                    ".Who was the first Indain woman Ambassador?",
                    ".Who can remove the Vice-President from his office?",
                    ".What is the term of Vice-President?",
                    ".How many Judges deos The Supreme Court of India contain at present?",
                    ".Who appoints the Chief Justice of the Supreme Court?",
                    ".The impeachment of the President is carried by which one of the following?",
                    ".How many number of members are nominated by the President to the Rajya sabha?",
                    ".Elections in India for Parliament and State Legislatures are conducted by?",
                    ".Members of Election Commission are appointed by?",]
answers_politics=[["Vijaylakshmi","Sarojini Naidu","Padmaja Naidu","Indira Gandhi"],
                  ["England","France","Germany","America"],
                  ["Mahatma Gandhi","Jawaharlal Nehru","B.R.Ambedkar","Vallabhai Patel"],
                  ["Rajiv Gandhi","Indira Gandhi","Morarji Desai","Charan Singh"],
                  ["Jawaharlal Nehru","Mahatma Gandhi","B.R.Ambedkar","B.N.Rao"],
                  ["Vijaya Lakshmi Pandit","Indira Gandhi","Mother Theresa","Margret Thatcher"],
                  ["Chandrawati","Ram Dulari Sinha","Sharda Mukherjee","Chonira Belliappa Muttamma"],
                  ["President","Prime Minister","Parliament","Legislative Assembly"],
                  ["6yrs","4yrs","7yrs","5yrs"],
                  ["25","31","20","30"],
                  ["President","Prime Minister","Parliament","Legeslative Assembly"],
                  ["Attorney general","Members of the legislative","Parliament","Prime minister"],
                  ["20","18","15","12"],
                  ["President","State Election Commision","Governor","Election Commission of India"],
                  ["President","Prime Minister","Elected by people","Chief Justice of India"]]
correct_answers_politics=[1,3,2,1,0,0,3,2,3,1,0,2,3,3,0]

currentaffairs_questions=[".Who is the present RBI Governor?",
                          ".Who is the current President of India?",
                          ".Who is the world's richest man?",
                          ".Which is currently the most expensive stock in India?",
                          ".Who is the current Chief Minister of Karnataka?",
                          ".Who is the present richest person in India?",
                          ".Where did corona virus origniate?",
                          ".Who won the cricketer of the month February?",
                          ".The mutated Coronavirus is from which country?",
                          ".Which famous basketball personality died in 2020?",
                          ".Who is the present Chess Grandmaster in the world?",
                          ".Which is the covid vaccine made in India?",
                          ".Who is the present President of USA?",
                          ".Where is the headquarters of UNICEF?",
                          ".Who is the youngest billionare in the world?"]
                          
                          
answers_currentaffairs=[["Raghuram Rajan","Shaktikanta Das","Nirmala Sitaraman","Gita Gopinath"],
                        ["Pranab Mukherjee","M.Venkaiah Naidu","Ram Nath Kovind","Rajnath Singh"],
                        ["Mark Zuckerberg","Jeff Bezos","Bill Gates","Elon Musk"],
                        ["MRF","Honeywell Automation","Tata Consultancy Services","Bosch"],
                        ["Siddaramaiyah","D.K Shivakumar","B.S Yediyurappa","H.D Deve Gowda"],
                        ["Anil Ambani","Ratan Tata","Goutam Adani","Mukesh Ambani"],
                        ["India","USA","England","China"],
                        ["Rishab Pant","Ashwin","Virat Kohli","James Anderson"],
                        ["India","England","USA","Italy"],
                        ["Kobe Bryant","Stephan Curry","Micheal Jordan","James Harden"],
                        ["Magnus Carlsen","Vishwanath Anand","Hikaru Nakamura","Anish Giri"],
                        ["Janssen","Covaxin","Pfizer","Moderna"],
                        ["Barack Obama","Donald Trump","Hilary Clinton","Joe Biden"],
                        ["Washington","New Jersey","New York","Las Vegas"],
                        ["Kyllie Jenner","Elon Musk","Kendall Jenner","Warren Buffet"]]
                        
correct_answers_currentaffairs=[2,2,3,0,2,3,3,1,1,0,1,1,3,2,0]

movie_questions=[".Which is the first Indian movie submitted for Oscar?",
                ".Which is the first Indian sound film?",
                ".Filmfare Awards was started in which year?",
                ".Who is the main actor in K.G.F?",
                ".Which of the following movie is based on science fiction?",
                ".Which series on NETFLIX was based on a game whose sales increased?",
                ".Which of the following movies is based on cricket?",
                ".Deepika Padukone acted in which of the hollywood movies?",
                ".Who is the first actress to be nominated for Rajya Sabha?",
                ".Who is known as 'The Show Man' of Indian cinema?",
                ".Who is called as 'Challenging Star' in sandlewood industry?",
                ".The movie named 'Half Girlfriend' was a book written by?",
                ".Who wrote the book Harry Potter?",
                ".Which of the following is a sitcom?",
                ".Cannes film festival is held every year in which country?"]

answers_movie=[["The Guide","Mother India","Madhumati","Amrapali"],
               ["Alam Ara","Raja Harishchandra","Kishan Kanya","Idiots"],
               ["1952","1964","1954","1960"],
               ["Yash","Puneeth","Sudeep","Hrithik"],
               ["Interstellar","Chak de India","Lagan","Super 30"],
               ["F1","Queen's Gambit","Big Bang Theory","Jada"],
               ["3Idiots","Tare Zameen Par","Lagaan","Krish"],
               ["Fast and Furious","Wonder woman","Madonna","XXX"],
               ["Meena Kumari","Nargis","Madhubala","Jaya Bachchan"],
               ["Dev Anand","Raj Kapoor","Dilip Kumar","Rajesh Khanna"],
               ["Yash","Puneeth","Sudeep","Darshan"],
               ["Chetan Bhagat","Vikas Swarup","Kashinath Singh","Anuja Chauhan"],
               ["JK Rowling","Christopher Nolen","Charles Bukowski","Bruce Wagner"],
               ["F.R.I.E.N.D.S","Riverdale","Money Heist","Tom and Jerry"],
               ["Italy","Egypt","France","USA"]]
correct_answers_movie=[1,0,2,0,0,1,2,3,1,1,3,0,0,0,2]               
        
travel_questions=[".On which mountain are 4 American President's head carved?",
                  ".Which of the 7 wonders of the world is located in Peru?",
                  ".Which city is reffered to as 'The pink city'?",
                  ".Where is the leaning tower located?",
                  ".Which is the tallest building in the world?",
                  ".Where is the famous Eiffel Tower situated?",
                  ".Where is 'Christ the Redeemer' statue situated?",
                  ".Where is the Taj Mahal located?",
                  ".Where in Egypt will you find the pyramids?",
                  ".The Giant Buddha is found in which country?",
                  ".What is the name of the mysterious rocks in England?",
                  ".Golden temple is situated in which place of India?",
                  ".Which is the largest waterfalls in the world?",
                  ".The world Famous Ajanta Caves is located in which state?",
                  ".Which city is called 'The White City ' of Rajasthan?"]
answers_travel=[["Mount Kilimanjaro","Mount Rashmore","Mauna Kea","Mount Logan"],
                ["Colosseum","Machu Picchu","Petra","Chiken Itza"],
                ["Shangai","New York","Jaipur","Chennai"],
                ["Rome","Venice","Milan","Pisa"],
                ["Shangai Tower","Abraj Al Bait","Taipei 101","Burj Khalifa"],
                ["Nice","Lisbon","Madrid","Paris"],
                ["Rio de Janeiro","Santiago","Buenos Aires","Salvador"],
                ["Delhi","Mumbai","Agra","Banglore"],
                ["Alexandria","Aswan","Giza","Luxor"],
                ["China","Bhutan","Nepal","Bangladesh"],
                ["Old Harry Rocks","Stonehenge","Balancing Rock","The Pillar Rock"],
                ["Dehli","Mumbai","Amritsar","Surat"],
                ["Niagara Falls","Iguazu Falls","Vicotria Falls","Gullfoss Falls"],
                ["Andhra Pradesh","Maharashtra","Orissa","Karnataka"],
                ["Udaipur","Jaipur","Jodhpur","Bilaspur"]]
correct_answers_travel=[1,1,2,3,3,3,0,2,2,0,1,2,0,1,0]

sports_questions=[".Which country will host the upcoming cricket world cup?",
                  ".Who was the first Grandmaster Chess Champion from India?",
                  ".Who is the considered as the most successful swimmer?",
                  ".What is Lewis Hamilton famous for?",
                  ".Where will the upcoming Olympics be hosted?",
                  ".World Test Championship final is going to held between which two teams?",
                  ".Who has won the most Wimbeldon singles title?",
                  ".Who is the captain of Indian Football team?",
                  ".Rugby is a National Game of which country?",
                  ".Who has scored most goals in La Liga history?",
                  ".Who won the Cricket World cup 2019",
                  ".Who won the FIFA 2018?",
                  ".Vijay Hazare Trophy belongs to which game?",
                  ".Dronacharya Award is given to?",
                  ".Which is the highest award given for sports in India?",]
                  
answers_sports=[["England","Australia","South Africa","India"],
                ["Pentala Harikrishnan","Krishnan Sasikiran","Viswanathan Anand","Ramachandran Ramesh"],
                ["Grant Hackett","Virdhawal Khade","Micheal Phelps","Mark Spitz"],
                ["Car racing","Swimming","Cricket","Tennis"],
                ["Paris","Japan","India","England"],
                ["IND vs ENG", "IND vs AUS", "IND vs NZ", "NZ vs AUS"],
                ["Roger Federer","Rafeal Nadal","Novak Djokovic","Andy Murray"],
                ["Udanta","Sandesh Jhingan","Gurpreeth Singh Sandu","Sunil Chettri"],
                ["India","New Zealand","England","USA"],
                ["Messi","Ronaldo","Sergio Ramos","marcelo"],
                ["India","New Zealand","England","Australia"],
                ["France","Croatia","Belgium","England"],
                ["Football","Swimming","Cricket","Tennis"],
                ["Archers","Coaches","Swimmers","Managers"],
                ["Arjuna Awards","Dronacharya Award","Rajiv Gandhi Khel Ratna Award","Dhyan Chand Award"]]
correct_answers_sports=[3,2,2,0,1,2,0,3,1,0,2,0,2,1,2]


global user_answer_movie,user_answer_sports,user_answer_travel,user_answer_politics,user_answer_currentaffairs
user_answer_movie=[]
user_answer_sports=[]
user_answer_travel=[]
user_answer_politics=[]
user_answer_currentaffairs=[]


global indexes
indexes=[]
question_no=["1","2","3","4","5"]
def generatequestions():
    global indexes
    indexes=[]
    while(len(indexes)<5):#here 5 tells the number of questions to be diplayed, i.e 5 questions
        x=random.randint(0,14)
        if x in indexes:
            continue
        else:
            indexes.append(x)#here indexes list stores 5 random integers indicating question numbers to be displayed
global btn_retry
global q_no
global ques
def retry():
    lblresult.destroy()         
    lblscore.destroy()
    lbl_msg.destroy()
    btn_retry.destroy()    
    startispressed()

global lbl_msg
def showresult_movie(score_movie):
    lblq_no.destroy()
    lblquestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    nxtbtn.destroy()
    global lblresult
    lblresult=Label(
        root,
        text="Your Score",
        font=("Aerial",70),
        background="gold"
        )
    lblresult.pack(pady=(200,0))
    global lblscore
    lblscore=Label(
        root,
        text=score_movie,
        background="gold",
        justify="center",
        font=("Aerial",80),
        )
    lblscore.pack()
    global lbl_msg
    lbl_msg=Label(
        root,
        text="Thank you for taking the quiz",
        font=("Aerial",40),
        background="gold",
        justify="center",
        )
    lbl_msg.pack()
    
    global btn_retry
    btn_retry=Button(
       root,
       command=retry,
       text="RETRY",
       bg="black",
       fg="gold",
       font=("Aerial",20),
       )
    btn_retry.place(x=440,y=600)

        
def showresult_currentaffairs(score_currentaffairs):
    lblq_no.destroy()
    lblquestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    nxtbtn.destroy()
    global lblresult
    lblresult=Label(
        root,
        text="Your Score",
        font=("Aerial",70),
        background="gold"
        )
    lblresult.pack(pady=(200,0))
    global lblscore
    lblscore=Label(
        root,
        text=score_currentaffairs,
        background="gold",
        justify="center",
        font=("Aerial",80),
        )
    lblscore.pack()
    global lbl_msg
    lbl_msg=Label(
        root,
        text="Thank you for taking the quiz",
        font=("Aerial",40),
        background="gold",
        justify="center",
        )
    lbl_msg.pack()
    global btn_retry
    btn_retry=Button(
       root,
       command=retry,
       text="RETRY",
       bg="black",
       fg="gold",
       font=("Aerial",20),
       )
    btn_retry.place(x=440,y=600)

def showresult_travel(score_travel):
    lblq_no.destroy()
    lblquestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    nxtbtn.destroy()
    global lblresult
    lblresult=Label(
        root,
        text="Your Score",
        font=("Aerial",70),
        background="gold"
        )
    lblresult.pack(pady=(200,0))
    global lblscore
    lblscore=Label(
        root,
        text=score_travel,
        background="gold",
        justify="center",
        font=("Aerial",80),
        )
    lblscore.pack()
    global lbl_msg
    lbl_msg=Label(
        root,
        text="Thank you for taking the quiz",
        font=("Aerial",40),
        background="gold",
        justify="center",
        )
    lbl_msg.pack()
    global btn_retry
    btn_retry=Button(
       root,
       command=retry,
       text="RETRY",
       bg="black",
       fg="gold",
       font=("Aerial",20),
       )
    btn_retry.place(x=440,y=600)

def showresult_politics(score_politics):
    lblq_no.destroy()
    lblquestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    nxtbtn.destroy()
    global lblresult
    lblresult=Label(
        root,
        text="Your Score",
        font=("Aerial",70),
        background="gold"
        )
    lblresult.pack(pady=(200,0))
    global lblscore
    lblscore=Label(
        root,
        text=score_politics,
        background="gold",
        justify="center",
        font=("Aerial",80),
        )
    lblscore.pack()
    global lbl_msg
    lbl_msg=Label(
        root,
        text="Thank you for taking the quiz",
        font=("Aerial",40),
        background="gold",
        justify="center",
        )
    lbl_msg.pack()
    global btn_retry
    btn_retry=Button(
       root,
       command=retry,
       text="RETRY",
       bg="black",
       fg="gold",
       font=("Aerial",20),
       )
    btn_retry.place(x=440,y=600)
    
   
def showresult_sports(score_sports):
    lblq_no.destroy()
    lblquestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    nxtbtn.destroy()
    global lblresult
    lblresult=Label(
        root,
        text="Your Score",
        font=("Aerial",70),
        background="gold"
        )
    lblresult.pack(pady=(200,0))
    global lblscore
    lblscore=Label(
        root,
        text=score_sports,
        background="gold",
        justify="center",
        font=("Aerial",80),
        )
    lblscore.pack()
    global lbl_msg
    lbl_msg=Label(
        root,
        text="Thank you for taking the quiz",
        font=("Aerial",40),
        background="gold",
        justify="center",
        )
    lbl_msg.pack()
    global btn_retry
    btn_retry=Button(
       root,
       command=retry,
       text="RETRY",
       bg="black",
       fg="gold",
       font=("Aerial",20),
       )
    btn_retry.place(x=440,y=600)
   
    
def calcscore_movie():
    x=0
    global score_movie
    score_movie=0
    for i in indexes:
        if user_answer_movie[x]==correct_answers_movie[i]:
            score_movie+=1
        x+=1
    showresult_movie(score_movie)


def calcscore_sports():
    x=0
    global score_sports
    score_sports=0
    for i in indexes:
        if user_answer_sports[x]==correct_answers_sports[i]:
            score_sports+=1
        x+=1
    showresult_sports(score_sports)

def calcscore_politics():   
    x=0
    global score_politics
    score_politics=0
    for i in indexes:
        if user_answer_politics[x]==correct_answers_politics[i]:
            score_politics+=1
        x+=1
    showresult_politics(score_politics)

def calcscore_travel():   
    x=0
    global score_travel
    score_travel=0
    for i in indexes:
        if user_answer_travel[x]==correct_answers_travel[i]:
            score_travel+=1
        x+=1
    showresult_travel(score_travel)

    
def calcscore_currentaffairs():
    global x
    x=0
    global score_currentaffairs
    score_currentaffairs=0
    for i in indexes:
        if user_answer_currentaffairs[x]==correct_answers_currentaffairs[i]:
                score_currentaffairs+=1
        x+=1
    showresult_currentaffairs(score_currentaffairs)

    
ques=1

qno=1
def next_clicked_movie():
    global radiovar,user_answer_movie
    global lblquestion,r1,r2,r3,r4,display
    global ques,qno
    m=radiovar.get()
    user_answer_movie.append(m)
    radiovar.set(-1)
    
    if ques<4:
        lblq_no.config(text=question_no[qno])
        lblquestion.config(text=movie_questions[indexes[ques]])
        r1['text']=answers_movie[indexes[ques]][0]
        r2['text']=answers_movie[indexes[ques]][1]
        r3['text']=answers_movie[indexes[ques]][2]
        r4['text']=answers_movie[indexes[ques]][3]
        nxtbtn.config(text="NEXT")
        qno+=1
        ques+=1
       
    elif ques==4:
        lblq_no.config(text=question_no[qno])
        lblquestion.config(text=movie_questions[indexes[ques]])
        r1['text']=answers_movie[indexes[ques]][0]
        r2['text']=answers_movie[indexes[ques]][1]
        r3['text']=answers_movie[indexes[ques]][2]
        r4['text']=answers_movie[indexes[ques]][3]
        nxtbtn.config(text="SUBMIT")
        ques+=1

    else:
        calcscore_movie()
        ques=1
        qno=1
        user_answer_movie=[]

           
         
def next_clicked_currentaffairs():
    global radiovar,user_answer_currentaffairs
    global lblquestion,r1,r2,r3,r4,display
    global ques,qno
    m=radiovar.get()
    user_answer_currentaffairs.append(m)
    radiovar.set(-1)
    
    if ques<4:
        lblq_no.config(text=question_no[qno])
        lblquestion.config(text=currentaffairs_questions[indexes[ques]])
        r1['text']=answers_currentaffairs[indexes[ques]][0]
        r2['text']=answers_currentaffairs[indexes[ques]][1]
        r3['text']=answers_currentaffairs[indexes[ques]][2]
        r4['text']=answers_currentaffairs[indexes[ques]][3]
        nxtbtn.config(text="NEXT")
        qno+=1
        ques+=1
       
    elif ques==4:
        lblq_no.config(text=question_no[qno])
        lblquestion.config(text=currentaffairs_questions[indexes[ques]])
        r1['text']=answers_currentaffairs[indexes[ques]][0]
        r2['text']=answers_currentaffairs[indexes[ques]][1]
        r3['text']=answers_currentaffairs[indexes[ques]][2]
        r4['text']=answers_currentaffairs[indexes[ques]][3]
        nxtbtn.config(text="SUBMIT")
        ques+=1

    else:
        calcscore_currentaffairs()
        ques=1
        qno=1
        user_answer_currentaffairs=[]

           
        
def next_clicked_travel():
    global radiovar,user_answer_travel
    global lblquestion,r1,r2,r3,r4,display
    global ques,qno
    m=radiovar.get()
    user_answer_travel.append(m)
    radiovar.set(-1)
    
    if ques<4:
        lblq_no.config(text=question_no[qno])
        lblquestion.config(text=travel_questions[indexes[ques]])
        r1['text']=answers_travel[indexes[ques]][0]
        r2['text']=answers_travel[indexes[ques]][1]
        r3['text']=answers_travel[indexes[ques]][2]
        r4['text']=answers_travel[indexes[ques]][3]
        nxtbtn.config(text="NEXT")
        qno+=1
        ques+=1
       
    elif ques==4:
        lblq_no.config(text=question_no[qno])
        lblquestion.config(text=travel_questions[indexes[ques]])
        r1['text']=answers_travel[indexes[ques]][0]
        r2['text']=answers_travel[indexes[ques]][1]
        r3['text']=answers_travel[indexes[ques]][2]
        r4['text']=answers_travel[indexes[ques]][3]
        nxtbtn.config(text="SUBMIT")
        ques+=1

    else:
        calcscore_travel()
        ques=1
        qno=1
        user_answer_travel=[]

         
def next_clicked_politics():
    global radiovar,user_answer_politics
    global lblquestion,r1,r2,r3,r4,display
    global ques,qno
    m=radiovar.get()
    user_answer_politics.append(m)
    radiovar.set(-1)
    
    if ques<4:
        lblq_no.config(text=question_no[qno])
        lblquestion.config(text=politics_questions[indexes[ques]])
        r1['text']=answers_politics[indexes[ques]][0]
        r2['text']=answers_politics[indexes[ques]][1]
        r3['text']=answers_politics[indexes[ques]][2]
        r4['text']=answers_politics[indexes[ques]][3]
        nxtbtn.config(text="NEXT")
        qno+=1
        ques+=1
       
    elif ques==4:
        lblq_no.config(text=question_no[qno])
        lblquestion.config(text=politics_questions[indexes[ques]])
        r1['text']=answers_politics[indexes[ques]][0]
        r2['text']=answers_politics[indexes[ques]][1]
        r3['text']=answers_politics[indexes[ques]][2]
        r4['text']=answers_politics[indexes[ques]][3]
        nxtbtn.config(text="SUBMIT")
        ques+=1

    else:
        calcscore_politics()
        ques=1
        qno=1
        user_answer_politics=[]
           
        
            
def next_clicked_sports():
    global radiovar,user_answer_sports
    global lblquestion,r1,r2,r3,r4,display
    global ques,qno
    s=radiovar.get()
    user_answer_sports.append(s)
    radiovar.set(-1)
    
    if ques<4:
        lblq_no.config(text=question_no[qno])
        lblquestion.config(text=sports_questions[indexes[ques]])
        r1['text']=answers_sports[indexes[ques]][0]
        r2['text']=answers_sports[indexes[ques]][1]
        r3['text']=answers_sports[indexes[ques]][2]
        r4['text']=answers_sports[indexes[ques]][3]
        nxtbtn.config(text="NEXT")
        qno+=1
        ques+=1
       
    elif ques==4:
        lblq_no.config(text=question_no[qno])
        lblquestion.config(text=sports_questions[indexes[ques]])
        r1['text']=answers_sports[indexes[ques]][0]
        r2['text']=answers_sports[indexes[ques]][1]
        r3['text']=answers_sports[indexes[ques]][2]
        r4['text']=answers_sports[indexes[ques]][3]
        nxtbtn.config(text="SUBMIT")
        ques+=1

    else:
         calcscore_sports()
         ques=1
         qno=1
         user_answer_sports=[]
         
def sports():
    global lblquestion,r1,r2,r3,r4,lblq_no,nxtbtn,display,btn_sports,btn_movie,btn_current_affairs,btn_politics,btn_travel,btn_retry
    btn_sports.destroy()
    btn_movie.destroy()
    btn_current_affairs.destroy()
    btn_politics.destroy()
    btn_travel.destroy()
    lbl_category.destroy()
    
    lblq_no=Label(
        root,
        text=question_no[0],
        background="gold",
        foreground="black",
        font=("Aerial",20),
        anchor=W,
        )
    lblq_no.place(x=0,y=50)
    lblquestion=Label(
        root,
        text=sports_questions[indexes[0]],
        font=("Aerial",20),
        width=500,
        anchor=W,
        justify=LEFT,
        background="gold",
        foreground="black",
        wraplength=1000,

        )
    lblquestion.place(x=20,y=50)

    global radiovar
    radiovar=IntVar()
    radiovar.set(-1)

    r1=Radiobutton(
        root,
        text=answers_sports[indexes[0]][0],
        font=("Aerial",20),
        value=0,
        variable=radiovar,
        background="gold",
        foreground="black",
        anchor=W,
        )
    r1.place(x=0,y=100)
    r2=Radiobutton(
        root,
        text=answers_sports[indexes[0]][1],
        font=("Aerial",20),
        value=1,
        variable=radiovar,
        background="gold",
        foreground="black",
        anchor=W,
        )
    r2.place(x=0,y=150)
    r3=Radiobutton(
        root,
        text=answers_sports[indexes[0]][2],
        font=("Aerial",20),
        value=2,
        variable=radiovar,
        anchor=W,
        background="gold",
        foreground="black",
        )
    r3.place(x=0,y=200)
    r4=Radiobutton(
        root,
        text=answers_sports[indexes[0]][3],
        font=("Aerial",20),
        value=3,
        variable=radiovar,
        anchor=W,
        background="gold",
        foreground="black",
        )
    r4.place(x=0,y=250)
    global nxtbtn
    nxtbtn=Button(
        root,
        text="NEXT",
        command=next_clicked_sports,
        bg="black",
        fg="gold",
        font=("Aerial",20)
        )
    nxtbtn.place(x=400,y=400)

def movie():
    global lblquestion,r1,r2,r3,r4,lblq_no,nxtbtn,display,btn_sports,btn_movie,btn_current_affairs,btn_politics,btn_travel,btn_retry
    btn_sports.destroy()
    btn_movie.destroy()
    btn_current_affairs.destroy()
    btn_politics.destroy()
    btn_travel.destroy()
    lbl_category.destroy()
    
    lblq_no=Label(
        root,
        text=question_no[0],
        background="gold",
        foreground="black",
        font=("Aerial",20),
        anchor=W,
        )
    lblq_no.place(x=0,y=50)
    lblquestion=Label(
        root,
        text=movie_questions[indexes[0]],
        font=("Aerial",20),
        width=500,
        anchor=W,
        background="gold",
        foreground="black",
        wraplength=1000,

        )
    lblquestion.place(x=20,y=50)

    global radiovar
    radiovar=IntVar()
    radiovar.set(-1)

    r1=Radiobutton(
        root,
        text=answers_movie[indexes[0]][0],
        font=("Aerial",20),
        value=0,
        variable=radiovar,
        background="gold",
        foreground="black",
        anchor=W,
        )
    r1.place(x=0,y=100)
    r2=Radiobutton(
        root,
        text=answers_movie[indexes[0]][1],
        font=("Aerial",20),
        value=1,
        variable=radiovar,
        background="gold",
        foreground="black",
        anchor=W,
        )
    r2.place(x=0,y=150)
    r3=Radiobutton(
        root,
        text=answers_movie[indexes[0]][2],
        font=("Aerial",20),
        value=2,
        variable=radiovar,
        anchor=W,
        background="gold",
        foreground="black",
        )
    r3.place(x=0,y=200)
    r4=Radiobutton(
        root,
        text=answers_movie[indexes[0]][3],
        font=("Aerial",20),
        value=3,
        variable=radiovar,
        anchor=W,
        background="gold",
        foreground="black",
        )
    r4.place(x=0,y=250)
    global nxtbtn
    nxtbtn=Button(
        root,
        text="NEXT",
        command=next_clicked_movie,
        bg="black",
        fg="gold",
        font=("Aerial",20)
        )
    nxtbtn.place(x=400,y=400)

def politics():
    global lblquestion,r1,r2,r3,r4,lblq_no,nxtbtn,display,btn_sports,btn_movie,btn_current_affairs,btn_politics,btn_travel,btn_retry
    btn_sports.destroy()
    btn_movie.destroy()
    btn_current_affairs.destroy()
    btn_politics.destroy()
    btn_travel.destroy()
    lbl_category.destroy()
    
    lblq_no=Label(
        root,
        text=question_no[0],
        background="gold",
        foreground="black",
        font=("Aerial",20),
        anchor=W,
        )
    lblq_no.place(x=0,y=50)
    lblquestion=Label(
        root,
        text=politics_questions[indexes[0]],
        font=("Aerial",20),
        width=500,
        anchor=W,
        background="gold",
        foreground="black",
        wraplength=1000,

        )
    lblquestion.place(x=20,y=50)

    global radiovar
    radiovar=IntVar()
    radiovar.set(-1)

    r1=Radiobutton(
        root,
        text=answers_politics[indexes[0]][0],
        font=("Aerial",20),
        value=0,
        variable=radiovar,
        background="gold",
        foreground="black",
        anchor=W,
        )
    r1.place(x=0,y=100)
    r2=Radiobutton(
        root,
        text=answers_politics[indexes[0]][1],
        font=("Aerial",20),
        value=1,
        variable=radiovar,
        background="gold",
        foreground="black",
        anchor=W,
        )
    r2.place(x=0,y=150)
    r3=Radiobutton(
        root,
        text=answers_politics[indexes[0]][2],
        font=("Aerial",20),
        value=2,
        variable=radiovar,
        anchor=W,
        background="gold",
        foreground="black",
        )
    r3.place(x=0,y=200)
    r4=Radiobutton(
        root,
        text=answers_politics[indexes[0]][3],
        font=("Aerial",20),
        value=3,
        variable=radiovar,
        anchor=W,
        background="gold",
        foreground="black",
        )
    r4.place(x=0,y=250)
    global nxtbtn
    nxtbtn=Button(
        root,
        text="NEXT",
        command=next_clicked_politics,
        bg="black",
        fg="gold",
        font=("Aerial",20)
        )
    nxtbtn.place(x=400,y=400)
    

def travel():
    global lblquestion,r1,r2,r3,r4,lblq_no,nxtbtn,display,btn_sports,btn_movie,btn_current_affairs,btn_politics,btn_travel,btn_retry
    btn_sports.destroy()
    btn_movie.destroy()
    btn_current_affairs.destroy()
    btn_politics.destroy()
    btn_travel.destroy()
    lbl_category.destroy()
    
    lblq_no=Label(
        root,
        text=question_no[0],
        background="gold",
        foreground="black",
        font=("Aerial",20),
        anchor=W,
        )
    lblq_no.place(x=0,y=50)
    lblquestion=Label(
        root,
        text=travel_questions[indexes[0]],
        font=("Aerial",20),
        width=500,
        anchor=W,
        background="gold",
        foreground="black",
        wraplength=1000,

        )
    lblquestion.place(x=20,y=50)

    global radiovar
    radiovar=IntVar()
    radiovar.set(-1)

    r1=Radiobutton(
        root,
        text=answers_travel[indexes[0]][0],
        font=("Aerial",20),
        value=0,
        variable=radiovar,
        background="gold",
        foreground="black",
        anchor=W,
        )
    r1.place(x=0,y=100)
    r2=Radiobutton(
        root,
        text=answers_travel[indexes[0]][1],
        font=("Aerial",20),
        value=1,
        variable=radiovar,
        background="gold",
        foreground="black",
        anchor=W,
        )
    r2.place(x=0,y=150)
    r3=Radiobutton(
        root,
        text=answers_travel[indexes[0]][2],
        font=("Aerial",20),
        value=2,
        variable=radiovar,
        anchor=W,
        background="gold",
        foreground="black",
        )
    r3.place(x=0,y=200)
    r4=Radiobutton(
        root,
        text=answers_travel[indexes[0]][3],
        font=("Aerial",20),
        value=3,
        variable=radiovar,
        anchor=W,
        background="gold",
        foreground="black",
        )
    r4.place(x=0,y=250)
    global nxtbtn
    nxtbtn=Button(
        root,
        text="NEXT",
        command=next_clicked_travel,
        bg="black",
        fg="gold",
        font=("Aerial",20)
        )
    nxtbtn.place(x=400,y=400)
def currentaffairs():
    global lblquestion,r1,r2,r3,r4,lblq_no,nxtbtn,display,btn_sports,btn_movie,btn_current_affairs,btn_politics,btn_travel,btn_retry
    btn_sports.destroy()
    btn_movie.destroy()
    btn_current_affairs.destroy()
    btn_politics.destroy()
    btn_travel.destroy()
    lbl_category.destroy()
    
    lblq_no=Label(
        root,
        text=question_no[0],
        background="gold",
        foreground="black",
        font=("Aerial",20),
        anchor=W,
        )
    lblq_no.place(x=0,y=50)
    lblquestion=Label(
        root,
        text=currentaffairs_questions[indexes[0]],
        font=("Aerial",20),
        width=500,
        anchor=W,
        background="gold",
        foreground="black",
        wraplength=1000,

        )
    lblquestion.place(x=20,y=50)

    global radiovar
    radiovar=IntVar()
    radiovar.set(-1)

    r1=Radiobutton(
        root,
        text=answers_currentaffairs[indexes[0]][0],
        font=("Aerial",20),
        value=0,
        variable=radiovar,
        background="gold",
        foreground="black",
        anchor=W,
        )
    r1.place(x=0,y=100)
    r2=Radiobutton(
        root,
        text=answers_currentaffairs[indexes[0]][1],
        font=("Aerial",20),
        value=1,
        variable=radiovar,
        background="gold",
        foreground="black",
        anchor=W,
        )
    r2.place(x=0,y=150)
    r3=Radiobutton(
        root,
        text=answers_currentaffairs[indexes[0]][2],
        font=("Aerial",20),
        value=2,
        variable=radiovar,
        anchor=W,
        background="gold",
        foreground="black",
        )
    r3.place(x=0,y=200)
    r4=Radiobutton(
        root,
        text=answers_currentaffairs[indexes[0]][3],
        font=("Aerial",20),
        value=3,
        variable=radiovar,
        anchor=W,
        background="gold",
        foreground="black",
        )
    r4.place(x=0,y=250)
    global nxtbtn
    nxtbtn=Button(
        root,
        text="NEXT",
        command=next_clicked_currentaffairs,
        bg="black",
        fg="gold",
        font=("Aerial",20)
        )
    nxtbtn.place(x=400,y=400)

def startquiz():
    global lblquestion,r1,r2,r3,r4,lblq_no,nxtbtn,display,btn_sports,btn_movie,btn_current_affairs,btn_politics,btn_travel,btn_msg,btn_retry,lbl_category
    lbl_category=Label(
        root,
        text="SELECT ANY 1 CATEGORY",
        font=("Aerial",50),
        background="gold",
        )
    lbl_category.place(x=50,y=10)
    btn_sports=Button(
        root,
        text="Sports",
        bg="Black",
        fg="Gold",
        command=sports,
        font=("Aerial",40),
        )
    btn_sports.place(x=125,y=150)
    btn_travel=Button(
        root,
        text="Travel",
        bg="Black",
        fg="Gold",
        command=travel,
        font=("Aerial",40),
        )
    btn_travel.place(x=550,y=150)

    btn_current_affairs=Button(
        root,
        text="Current Affairs",
        bg="Black",
        fg="Gold",
        command=currentaffairs,
        font=("Aerial",40),
        )
    btn_current_affairs.place(x=250,y=350)
    
    btn_politics=Button(
        root,
        text="Politics",
        bg="Black",
        fg="Gold",
        command=politics, 
        font=("Aerial",40),
        )
    btn_politics.place(x=125,y=550)

    btn_movie=Button(
        root,
        text="Movie",
        bg="Black",
        fg="Gold",
        command=movie,
        font=("Aerial",40),
        )
    btn_movie.place(x=550,y=550)

def startispressed():
    label1.destroy()
    lblinstruction.destroy()
    lblrules.destroy()
    btnstart.destroy()
    generatequestions()
    startquiz()



root=Tk()
root.geometry('1000x700')
root.title("General MCQ Quiz")
root.config(background="gold")
root.resizable(0,0)



label1=Label(
    root,
    text="WELCOME TO GENERAL MCQ QUIZ",
    background="gold",
    foreground="black",
    font=("Algerian",40)
    )
label1.pack(pady=(100,50))

btnstart=Button(
    root,    
    command = startispressed,
    border=0,
    text="START",
    fg="gold",
    font=("Algerian",30),
    bg="black")
btnstart.pack()


lblinstruction=Label(
    root,
    text="Read the rules\nClick start once you are ready",
    font=("Aerial",20),
    justify="center",
    background="gold")
lblinstruction.pack(pady=(10,70))
lblrules=Label(
    root,
    text="""RULES\n
->This quiz has several categories\n
->First click start and then choose the category that you want\n
->Each category will have five questions each carrying 1 mark\n
->Once next button is clicked you cannot go back to the previous question\n
->Click on submit once you have finished answering all the questions
""",
    background="gold",
    foreground="black",
    width=100,
    anchor=W,
    font=("Times",15),
    justify="left",
    )
lblrules.pack()
root.mainloop()
