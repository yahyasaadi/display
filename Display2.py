import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
import plotly.express as px
import pyrebase
import time,os
import random
from datetime import datetime
from datetime import date


today = date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

st.set_page_config(page_title='Garissa Township Consituency By-Election',page_icon='fm.png', layout = "wide")
selected2 = option_menu(None, ["Agents",'Chief Agents', "Official","Image"], 
  icons=['house', 'cloud-upload', "list-task",'download'], 
  menu_icon="cast", default_index=0, orientation="horizontal")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")


st.title("Garissa Township MP Seat Race")
firebaseConfig = {
  "apiKey": "AIzaSyCqMdmrITPM8x4PdMqP5T9Hcmmj5IJPH6M",
  "authDomain": "demoapp-607db.firebaseapp.com",
  "databaseURL": "https://demoapp-607db-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "demoapp-607db",
  "storageBucket": "demoapp-607db.appspot.com",
  "messagingSenderId": "641799333572",
  "appId": "1:641799333572:web:fd402ab5271f9fa4d6cb91",
  "measurementId": "G-KPVXQKZ7KK",
  "serviceAccount":"demoapp-607db-firebase-adminsdk-zsj0n-ed52918681.json"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
storage = firebase.storage()


placeholder = st.empty()

# while True:
if selected2 == "Agents":
  all_votes = db.child('votes').order_by_key().get()
  info = []
  for vote in all_votes:
    values = vote.val()
    print(values)
    info.append(values)
    
  # st.write(info)
  df = pd.DataFrame(info,columns=['time','ward','pollingStation','registerdVoters','rejected','rejectedObj','disputed','valid','dekow','jofle','osman','malow','feisal','muhiadin'])
  # st.write(df)
  df['time'] = pd.to_datetime(df['time'])
  df = df.sort_values(by='time',ascending=False)
  reg = 53765
  with placeholder.container():
    r1,r2= st.columns(2)
    r1.write(f"<h4 style ='margin-top:50px;'>Total Number of Registered Voters in Garissa Township are : {reg}<h4>",unsafe_allow_html=True)
    turnout = df[['rejected','disputed','valid','rejectedObj']]
    turnout = turnout.astype({"rejected":"int","disputed":"int","valid":"int","rejectedObj":"int"})
    # st.write(turnout['valid'].sum())
    # total_valid = turnout['valid'].sum()
    re_turnout = turnout[['rejected','disputed','valid','rejectedObj']].sum()
    final_turnout = re_turnout.sum()
    # st.write(re_turnout)
    r2.write("<h4 style ='margin-top:50px;'>The percentage Turnout Voters in Garissa Township is : {:.2f}%<h4>".format((final_turnout/reg)*100),unsafe_allow_html=True)
    c1,c2,c3,c4,c5 = st.columns(5)
    c1.write(f'<strong >Total Turnout: {final_turnout}</strong>',unsafe_allow_html=True)
    c5.write(f'<strong >Total Votes Rejection Objected: {re_turnout[3]}</strong>',unsafe_allow_html=True)
    c4.write(f'<strong >Total Votes Valid: {re_turnout[2]}</strong>',unsafe_allow_html=True)
    c3.write(f'<strong >Total Votes Disputed: {re_turnout[1]}</strong>',unsafe_allow_html=True)
    c2.write(f'<strong >Total Votes Rejected: {re_turnout[0]}</strong>',unsafe_allow_html=True)

    # osman,major,jofle = st.columns(3)
    # osman_data,major_data,jofle_data = st.columns(3)
    # osman_per,major_per,jofle_per = st.columns(3)
    # osman_data.write('<h3 style="margin-top:20px">Hon. ABDIKARIM</h3>',unsafe_allow_html=True)
    # major_data.write('<h3 style="margin-top:25px">Hon. DEKOW</h3>',unsafe_allow_html=True)
    # jofle_data.write('<h3 style="margin-top:20px">Hon. NASSIR</h3>',unsafe_allow_html=True)
    
    # THE CHANGE
    
    jofle, osman,major = st.columns(3)
    jofle_data, osman_data,major_data = st.columns(3)
    jofle_per, osman_per,major_per = st.columns(3)
    osman_data.write('<h3 style="margin-top:20px">Hon. ABDIKARIM</h3>',unsafe_allow_html=True)
    major_data.write('<h3 style="margin-top:25px">Hon. DEKOW</h3>',unsafe_allow_html=True)
    jofle_data.write('<h3 style="margin-top:20px">Hon. NASSIR</h3>',unsafe_allow_html=True)
    
    # THE END

    malow,feisal,muhiadin = st.columns(3)
    malow_data,feisal_data,muhiadin_data = st.columns(3)
    malow_per,feisal_per,muhiadin_per = st.columns(3)
    malow_data.write('<h3>Hon. MALOW</h3>',unsafe_allow_html=True)
    feisal_data.write('<h3 style="margin-top:30px">Hon. FEISAL</h3>',unsafe_allow_html=True)
    muhiadin_data.write('<h3 style="margin-top:30px">Hon. MUHIADIN</h3>',unsafe_allow_html=True)

    major.image('major.png')
    osman.image('osman.jpg')
    jofle.image('jofle.jpg')

    malow.image('malow.jpg')
    feisal.image('feisal1.jpg')
    muhiadin.image('muhiadin1.png')

    candidates_votes = df[['dekow','jofle','osman','malow','feisal','muhiadin']]
    candidates_votes = candidates_votes.astype({"dekow":"int","jofle":"int","osman":"int",'malow':'int','feisal':'int','muhiadin':'int'})
    votes4dekow=candidates_votes['dekow'].sum()
    votes4jofle=candidates_votes['jofle'].sum()
    votes4osman=candidates_votes['osman'].sum()
    votes4malow=candidates_votes['malow'].sum()
    votes4feisal=candidates_votes['feisal'].sum()
    votes4muhiadin=candidates_votes['muhiadin'].sum()

    major_data.write(f"Total Votes: {votes4dekow}")
    jofle_data.write(f"Total Votes: {votes4jofle}")
    osman_data.write(f"Total Votes: {votes4osman}")
    malow_data.write(f"Total Votes: {votes4malow}")
    feisal_data.write(f"Total Votes: {votes4feisal}")
    muhiadin_data.write(f"Total Votes: {votes4muhiadin}")

    def calculate(vote4each):
      percentage_f = (vote4each/re_turnout[2]) * 100
      return percentage_f
    major_per.write('Total Percentage: {:.2f}%'.format(calculate(votes4dekow)))
    jofle_per.write('Total Percentage: {:.2f}%'.format(calculate(votes4jofle)))
    osman_per.write('Total Percentage: {:.2f}%'.format(calculate(votes4osman)))
    malow_per.write('Total Percentage: {:.2f}%'.format(calculate(votes4malow)))
    feisal_per.write('Total Percentage: {:.2f}%'.format(calculate(votes4feisal)))
    muhiadin_per.write('Total Percentage: {:.2f}%'.format(calculate(votes4muhiadin)))
    # total = calculate(votes4osman)+calculate(votes4jofle)+calculate(votes4dekow)
    # st.write(total)
    graph1,graph2=st.columns(2)
    data = [['MAJOR',votes4dekow],['JOFLE',votes4jofle],['OSMAN',votes4osman],['MALOW',votes4malow],['FEISAL',votes4feisal],['MUHIADIN',votes4muhiadin]]
    jabir = pd.DataFrame(data,columns=['Candidate','Votes'] )
    jabir= jabir.sort_values(by='Votes', ascending=False)
    bar_chart = px.bar(jabir,
                        x='Candidate',
                        y='Votes',
                        text='Votes',
                        orientation='v',
                        color_discrete_sequence = ['#62B6B7'],
                        template='plotly_white')
    graph1.plotly_chart(bar_chart)
    #bar chart
    checkvotes = [votes4dekow,votes4jofle,votes4osman,votes4malow,votes4feisal,votes4muhiadin]
    pie_chart = px.pie(jabir, title = f'Votes for Each Candidate - {today}, {current_time}', values=checkvotes,names=['Dekow','Nassir','Abdikarim','Malow','Feisal','Muhiadin'])
    graph2.plotly_chart(pie_chart)
    st.dataframe(df,width=int(1900))

    ##checking who is leading
    hv=np.max(checkvotes)
    hv5=np.min(checkvotes)
    ("---")
    if hv == votes4dekow:
      checkvote1 = [votes4jofle,votes4osman,votes4malow,votes4feisal,votes4muhiadin]
      hv1=np.max(checkvote1)
      major_per.write(f"<strong style='color:#99004d;'>You are ahead by : {votes4dekow-hv1} votes</strong>",unsafe_allow_html=True)
    elif hv == votes4jofle:
      checkvote1 = [votes4dekow,votes4osman,votes4malow,votes4feisal,votes4muhiadin]
      hv1=np.max(checkvote1)
      jofle_per.write(f"<strong style='color:#99004d;'>You are ahead by : {votes4jofle-hv1} votes</strong>",unsafe_allow_html=True)
    elif hv == votes4osman:
      checkvote1 = [votes4dekow,votes4jofle,votes4malow,votes4feisal,votes4muhiadin]
      hv1=np.max(checkvote1)
      osman_per.write(f"<strong style='color:#99004d;'>You are ahead by : {votes4osman-hv1} votes</strong>",unsafe_allow_html=True)
    elif hv == votes4malow:
      checkvote1 = [votes4dekow,votes4osman,votes4jofle,votes4feisal,votes4muhiadin]
      hv1=np.max(checkvote1)
      malow_per.write(f"<strong style='color:#99004d;'>You are ahead by : {votes4malow-hv1} votes</strong>",unsafe_allow_html=True)
    elif hv == votes4feisal:
      checkvote1 = [votes4dekow,votes4osman,votes4jofle,votes4malow,votes4muhiadin]
      hv1=np.max(checkvote1)
      feisal_per.write(f"<strong style='color:#99004d;'>You are ahead by : {votes4feisal-hv1} votes</strong>",unsafe_allow_html=True)
    else:
      checkvote1 = [votes4dekow,votes4osman,votes4jofle,votes4malow,votes4feisal]
      hv1=np.max(checkvote1)
      muhiadin_per.write(f"<strong style='color:#99004d;'>You are ahead by : {votes4muhiadin-hv1} votes</strong>",unsafe_allow_html=True)
elif selected2 == "Chief Agents":
  all_votes = db.child('chiefAgents').order_by_key().get()
  info = []
  for vote in all_votes:
    values = vote.val()
    # print(values)
    info.append(values)
  # st.write(info)
  df = pd.DataFrame(info,columns=['time','ward','pollingStation','registerdVoters','rejected','rejectedObj','disputed','valid','dekow','jofle','osman','malow','feisal','muhiadin'])
  # st.write(df)
  df['time'] = pd.to_datetime(df['time'])
  df = df.sort_values(by='time',ascending=False)
  reg = 53765
  with placeholder.container():
    r1,r2= st.columns(2)
    r1.write(f"<h4 style ='margin-top:50px;'>Total Number of Registered Voters in Garissa Township are : {reg}<h4>",unsafe_allow_html=True)
    turnout = df[['rejected','disputed','valid','rejectedObj']]
    turnout = turnout.astype({"rejected":"int","disputed":"int","valid":"int","rejectedObj":"int"})
    # st.write(turnout['valid'].sum())
    # total_valid = turnout['valid'].sum()
    re_turnout = turnout[['rejected','disputed','valid','rejectedObj']].sum()
    final_turnout = re_turnout.sum()
    # st.write(re_turnout)
    r2.write("<h4 style ='margin-top:50px;'>The percentage Turnout Voters in Garissa Township is : {:.2f}%<h4>".format((final_turnout/reg)*100),unsafe_allow_html=True)
    c1,c2,c3,c4,c5 = st.columns(5)
    c1.write(f'<strong >Total Turnout: {final_turnout}</strong>',unsafe_allow_html=True)
    c5.write(f'<strong >Total Votes Rejection Objected: {re_turnout[3]}</strong>',unsafe_allow_html=True)
    c4.write(f'<strong >Total Votes Valid: {re_turnout[2]}</strong>',unsafe_allow_html=True)
    c3.write(f'<strong >Total Votes Disputed: {re_turnout[1]}</strong>',unsafe_allow_html=True)
    c2.write(f'<strong >Total Votes Rejected: {re_turnout[0]}</strong>',unsafe_allow_html=True)

    # osman,major,jofle = st.columns(3)
    # osman_data,major_data,jofle_data = st.columns(3)
    # osman_per,major_per,jofle_per = st.columns(3)
    
    # THE CHANGE
    jofle, osman,major = st.columns(3)
    jofle_data, osman_data,major_data = st.columns(3)
    jofle_per, osman_per,major_per = st.columns(3)
    
    # THE END

    malow,feisal,muhiadin = st.columns(3)
    malow_data,feisal_data,muhiadin_data = st.columns(3)
    malow_per,feisal_per,muhiadin_per = st.columns(3)

    major.image('major.png')
    osman.image('osman.jpg')
    jofle.image('jofle.jpg')

    malow.image('malow.jpg')
    feisal.image('feisal1.jpg')
    muhiadin.image('muhiadin1.png')

    candidates_votes = df[['dekow','jofle','osman','malow','feisal','muhiadin']]
    candidates_votes = candidates_votes.astype({"dekow":"int","jofle":"int","osman":"int",'malow':'int','feisal':'int','muhiadin':'int'})
    votes4dekow=candidates_votes['dekow'].sum()
    votes4jofle=candidates_votes['jofle'].sum()
    votes4osman=candidates_votes['osman'].sum()
    votes4malow=candidates_votes['malow'].sum()
    votes4feisal=candidates_votes['feisal'].sum()
    votes4muhiadin=candidates_votes['muhiadin'].sum()

    major_data.write(f"Total Votes: {votes4dekow}")
    jofle_data.write(f"Total Votes: {votes4jofle}")
    osman_data.write(f"Total Votes: {votes4osman}")
    malow_data.write(f"Total Votes: {votes4malow}")
    feisal_data.write(f"Total Votes: {votes4feisal}")
    muhiadin_data.write(f"Total Votes: {votes4muhiadin}")

    def calculate(vote4each):
      percentage_f = (vote4each/re_turnout[2]) * 100
      return percentage_f
    major_per.write('Total Percentage: {:.2f}%'.format(calculate(votes4dekow)))
    jofle_per.write('Total Percentage: {:.2f}%'.format(calculate(votes4jofle)))
    osman_per.write('Total Percentage: {:.2f}%'.format(calculate(votes4osman)))
    malow_per.write('Total Percentage: {:.2f}%'.format(calculate(votes4malow)))
    feisal_per.write('Total Percentage: {:.2f}%'.format(calculate(votes4feisal)))
    muhiadin_per.write('Total Percentage: {:.2f}%'.format(calculate(votes4muhiadin)))
    # total = calculate(votes4osman)+calculate(votes4jofle)+calculate(votes4dekow)
    # st.write(total)
    graph1,graph2=st.columns(2)
    data = [['MAJOR',votes4dekow],['JOFLE',votes4jofle],['OSMAN',votes4osman],['MALOW',votes4malow],['FEISAL',votes4feisal],['MUHIADIN',votes4muhiadin]]
    jabir = pd.DataFrame(data,columns=['Candidate','Votes'] )
    jabir= jabir.sort_values(by='Votes', ascending=False)
    bar_chart = px.bar(jabir,
                        x='Candidate',
                        y='Votes',
                        text='Votes',
                        orientation='v',
                        color_discrete_sequence = ['#62B6B7'],
                        template='plotly_white')
    graph1.plotly_chart(bar_chart)
    #bar chart
    checkvotes = [votes4dekow,votes4jofle,votes4osman,votes4malow,votes4feisal,votes4muhiadin]
    pie_chart = px.pie(jabir, title = f'Votes for Each Candidate - {today}, {current_time}', values=checkvotes,names=['Dekow','Nassir','Abdikarim','Malow','Feisal','Muhiadin'])
    graph2.plotly_chart(pie_chart)
    st.dataframe(df,width=int(1900))

    ##checking who is leading
    hv=np.max(checkvotes)
    hv5=np.min(checkvotes)
    ("---")
    if hv == votes4dekow:
      checkvote1 = [votes4jofle,votes4osman,votes4malow,votes4feisal,votes4muhiadin]
      hv1=np.max(checkvote1)
      major_per.write(f"<strong style='color:#99004d;'>You are ahead by : {votes4dekow-hv1} votes</strong>",unsafe_allow_html=True)
    elif hv == votes4jofle:
      checkvote1 = [votes4dekow,votes4osman,votes4malow,votes4feisal,votes4muhiadin]
      hv1=np.max(checkvote1)
      jofle_per.write(f"<strong style='color:#99004d;'>You are ahead by : {votes4jofle-hv1} votes</strong>",unsafe_allow_html=True)
    elif hv == votes4osman:
      checkvote1 = [votes4dekow,votes4jofle,votes4malow,votes4feisal,votes4muhiadin]
      hv1=np.max(checkvote1)
      osman_per.write(f"<strong style='color:#99004d;'>You are ahead by : {votes4osman-hv1} votes</strong>",unsafe_allow_html=True)
    elif hv == votes4malow:
      checkvote1 = [votes4dekow,votes4osman,votes4jofle,votes4feisal,votes4muhiadin]
      hv1=np.max(checkvote1)
      malow_per.write(f"<strong style='color:#99004d;'>You are ahead by : {votes4malow-hv1} votes</strong>",unsafe_allow_html=True)
    elif hv == votes4feisal:
      checkvote1 = [votes4dekow,votes4osman,votes4jofle,votes4malow,votes4muhiadin]
      hv1=np.max(checkvote1)
      feisal_per.write(f"<strong style='color:#99004d;'>You are ahead by : {votes4feisal-hv1} votes</strong>",unsafe_allow_html=True)
    else:
      checkvote1 = [votes4dekow,votes4osman,votes4jofle,votes4malow,votes4feisal]
      hv1=np.max(checkvote1)
      muhiadin_per.write(f"<strong style='color:#99004d;'>You are ahead by : {votes4muhiadin-hv1} votes</strong>",unsafe_allow_html=True)
elif selected2 == "Official":
  all_votes = db.child('Official').order_by_key().get()
  info = []
  for vote in all_votes:
    values = vote.val()
    # print(values)
    info.append(values)
  # st.write(info)
  df = pd.DataFrame(info,columns=['time','ward','pollingStation','registerdVoters','rejected','rejectedObj','disputed','valid','dekow','jofle','osman','malow','feisal','muhiadin'])
  # st.write(df)
  df['time'] = pd.to_datetime(df['time'])
  df = df.sort_values(by='time',ascending=False)
  reg = 53765
  with placeholder.container():
    r1,r2= st.columns(2)
    r1.write(f"<h4 style ='margin-top:50px;'>Total Number of Registered Voters in Garissa Township are : {reg}<h4>",unsafe_allow_html=True)
    turnout = df[['rejected','disputed','valid','rejectedObj']]
    turnout = turnout.astype({"rejected":"int","disputed":"int","valid":"int","rejectedObj":"int"})
    # st.write(turnout['valid'].sum())
    # total_valid = turnout['valid'].sum()
    re_turnout = turnout[['rejected','disputed','valid','rejectedObj']].sum()
    final_turnout = re_turnout.sum()
    # st.write(re_turnout)
    r2.write("<h4 style ='margin-top:50px;'>The percentage Turnout Voters in Garissa Township is : {:.2f}%<h4>".format((final_turnout/reg)*100),unsafe_allow_html=True)
    c1,c2,c3,c4,c5 = st.columns(5)
    c1.write(f'<strong >Total Turnout: {final_turnout}</strong>',unsafe_allow_html=True)
    c5.write(f'<strong >Total Votes Rejection Objected: {re_turnout[3]}</strong>',unsafe_allow_html=True)
    c4.write(f'<strong >Total Votes Valid: {re_turnout[2]}</strong>',unsafe_allow_html=True)
    c3.write(f'<strong >Total Votes Disputed: {re_turnout[1]}</strong>',unsafe_allow_html=True)
    c2.write(f'<strong >Total Votes Rejected: {re_turnout[0]}</strong>',unsafe_allow_html=True)

    # osman,major,jofle = st.columns(3)
    # osman_data,major_data,jofle_data = st.columns(3)
    # osman_per,major_per,jofle_per = st.columns(3)
    
    # THE CHANGE
    jofle, osman,major = st.columns(3)
    jofle_data, osman_data,major_data = st.columns(3)
    jofle_per, osman_per,major_per = st.columns(3)
    
    # THE END

    malow,feisal,muhiadin = st.columns(3)
    malow_data,feisal_data,muhiadin_data = st.columns(3)
    malow_per,feisal_per,muhiadin_per = st.columns(3)

    major.image('major.png')
    osman.image('osman.jpg')
    jofle.image('jofle.jpg')

    malow.image('malow.jpg')
    feisal.image('feisal1.jpg')
    muhiadin.image('muhiadin1.png')

    candidates_votes = df[['dekow','jofle','osman','malow','feisal','muhiadin']]
    candidates_votes = candidates_votes.astype({"dekow":"int","jofle":"int","osman":"int",'malow':'int','feisal':'int','muhiadin':'int'})
    votes4dekow=candidates_votes['dekow'].sum()
    votes4jofle=candidates_votes['jofle'].sum()
    votes4osman=candidates_votes['osman'].sum()
    votes4malow=candidates_votes['malow'].sum()
    votes4feisal=candidates_votes['feisal'].sum()
    votes4muhiadin=candidates_votes['muhiadin'].sum()

    major_data.write(f"Total Votes: {votes4dekow}")
    jofle_data.write(f"Total Votes: {votes4jofle}")
    osman_data.write(f"Total Votes: {votes4osman}")
    malow_data.write(f"Total Votes: {votes4malow}")
    feisal_data.write(f"Total Votes: {votes4feisal}")
    muhiadin_data.write(f"Total Votes: {votes4muhiadin}")

    def calculate(vote4each):
      percentage_f = (vote4each/re_turnout[2]) * 100
      return percentage_f
    major_per.write('Total Percentage: {:.2f}%'.format(calculate(votes4dekow)))
    jofle_per.write('Total Percentage: {:.2f}%'.format(calculate(votes4jofle)))
    osman_per.write('Total Percentage: {:.2f}%'.format(calculate(votes4osman)))
    malow_per.write('Total Percentage: {:.2f}%'.format(calculate(votes4malow)))
    feisal_per.write('Total Percentage: {:.2f}%'.format(calculate(votes4feisal)))
    muhiadin_per.write('Total Percentage: {:.2f}%'.format(calculate(votes4muhiadin)))
    # total = calculate(votes4osman)+calculate(votes4jofle)+calculate(votes4dekow)
    # st.write(total)
    graph1,graph2=st.columns(2)
    data = [['MAJOR',votes4dekow],['JOFLE',votes4jofle],['OSMAN',votes4osman],['MALOW',votes4malow],['FEISAL',votes4feisal],['MUHIADIN',votes4muhiadin]]
    jabir = pd.DataFrame(data,columns=['Candidate','Votes'] )
    jabir= jabir.sort_values(by='Votes', ascending=False)
    bar_chart = px.bar(jabir,
                        x='Candidate',
                        y='Votes',
                        text='Votes',
                        orientation='v',
                        color_discrete_sequence = ['#62B6B7'],
                        template='plotly_white')
    graph1.plotly_chart(bar_chart)
    #bar chart
    checkvotes = [votes4dekow,votes4jofle,votes4osman,votes4malow,votes4feisal,votes4muhiadin]
    pie_chart = px.pie(jabir, title = f'Votes for Each Candidate - {today}, {current_time}', values=checkvotes,names=['Dekow','Nassir','Abdikarim','Malow','Feisal','Muhiadin'])
    graph2.plotly_chart(pie_chart)
    st.dataframe(df,width=int(1900))

    ##checking who is leading
    hv=np.max(checkvotes)
    hv5=np.min(checkvotes)
    ("---")
    if hv == votes4dekow:
      checkvote1 = [votes4jofle,votes4osman,votes4malow,votes4feisal,votes4muhiadin]
      hv1=np.max(checkvote1)
      major_per.write(f"<strong style='color:#99004d;'>You are ahead by : {votes4dekow-hv1} votes</strong>",unsafe_allow_html=True)
    elif hv == votes4jofle:
      checkvote1 = [votes4dekow,votes4osman,votes4malow,votes4feisal,votes4muhiadin]
      hv1=np.max(checkvote1)
      jofle_per.write(f"<strong style='color:#99004d;'>You are ahead by : {votes4jofle-hv1} votes</strong>",unsafe_allow_html=True)
    elif hv == votes4osman:
      checkvote1 = [votes4dekow,votes4jofle,votes4malow,votes4feisal,votes4muhiadin]
      hv1=np.max(checkvote1)
      osman_per.write(f"<strong style='color:#99004d;'>You are ahead by : {votes4osman-hv1} votes</strong>",unsafe_allow_html=True)
    elif hv == votes4malow:
      checkvote1 = [votes4dekow,votes4osman,votes4jofle,votes4feisal,votes4muhiadin]
      hv1=np.max(checkvote1)
      malow_per.write(f"<strong style='color:#99004d;'>You are ahead by : {votes4malow-hv1} votes</strong>",unsafe_allow_html=True)
    elif hv == votes4feisal:
      checkvote1 = [votes4dekow,votes4osman,votes4jofle,votes4malow,votes4muhiadin]
      hv1=np.max(checkvote1)
      feisal_per.write(f"<strong style='color:#99004d;'>You are ahead by : {votes4feisal-hv1} votes</strong>",unsafe_allow_html=True)
    else:
      checkvote1 = [votes4dekow,votes4osman,votes4jofle,votes4malow,votes4feisal]
      hv1=np.max(checkvote1)
      muhiadin_per.write(f"<strong style='color:#99004d;'>You are ahead by : {votes4muhiadin-hv1} votes</strong>",unsafe_allow_html=True)
elif selected2 == 'Image':
  storage = firebase.storage()
  datadir = '/home/yahya/Desktop/j_display/images/'
  all_files = storage.child("images").list_files()
  for file in all_files:
      try:
          file.download_to_filename(datadir + file.name)
      except:
          print('Download Failed')
  with placeholder.container():
    image_col,image_desp = st.columns(2)
    for file in os.listdir(datadir):
      f = os.path.join(datadir,file)
      print(f)
      st.image("images/"+file,width=220,caption=file) #CHANGED image2 to images
      st.write(f'Form 35A for {file.split(".")[0]}')


else:
  with placeholder.container():
    pass

  # time.sleep(1)














style = '''
<style>
.e16nr0p30{
	margin-top:-100px;
}
footer{
  visibility:hidden;
}
header{
visibility: hidden;
}
</style>
'''
st.markdown(style,unsafe_allow_html=True)
