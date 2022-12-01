import streamlit as st
from PIL import Image
import requests



st.set_page_config(layout = 'wide', page_title="My Project",page_icon='tra.jpg')

# def load_lottieurl(url: str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# lottie_shops = load_lottieurl('https://assets6.lottiefiles.com/packages/lf20_0ilhlmpl.json')
# st_lottie(lottie_shops, height=250)

col1, col2, col3, = st.columns([0.5, 1, 0.5])
col2.header('Interview with Projecting Success')
st.write('---')
# col2.header('Akinsida Anthony Stephen')

col1, col2 = st.columns(2)
          
with col1:
        st.header('A Statement of Intent')

        hold, tab1, tab2, tab3, tab4 = st.tabs(['Hold','About me','My Initiative(s)', "Hosted Lesson Note", "My Plans"])
        with tab1:
            st.write('''I dont like sterotypes, I applied for this job because
            there is a degree of freedom and initiative on the side of tutors required for an
            apprenticeship programme to become a success, and I strongly believe that I have a lot to offer
            the program in terms of my experience and initiatives.   
            [Click here to read my general profile:](https://anthonyakinsida.streamlit.app/)''') 
            


        with tab2:
            st.write('''My ability to create hands-on resources for my students set me apart. I dont
            believe students should be made to memorize or cram codes, I do not expect them to be able to
            repeat the codes immediately after the class, I expect them to get used to the code-formats and
            consequently they can produce their own codes and develop their own learning styles.
            
- I provide hosted lesson notes in form of applications for my students. Whether it is one student or a thousand students there is at least one hosted lesson note for the class and for the topic or topics
- I believe it is a watse of time to teach or learn one data science langauage at a time, I strongly believe that the best way to become verstile is to learn the the two most popular data science languages(R and Python) simultenously.
To this end, I developed successful tutorials with hoted lesson notes that help students to learn both languages together. The benefit of this
initiative is huge of the student and for the society at large. It is better to produce apprentices who can fit and work anywhere
[Click here to see some big companies using R:](https://careerkarma.com/blog/who-uses-r/)  
[Click here to see some big companies using Python:](https://realpython.com/world-class-companies-using-python/)
''')             
        
        with tab3:
            st.write('''I use streamlit a lot because it is easy on python code and very easy to deploy  
            [Click here to see a sample of a hosted lesson note:](https://sample.streamlit.app/) 
            ''')
        with tab4:
            st.write('''The following are required:  
- SQL (MySQL)
- Excel
- Power BI
- Statistics
- Machine Learning
- Data Analytics
However, I believe that we can add the following to enrich the students' journey
- R Programming Language and 
- Streamlit (a python library that enables you to create apps and dashboards in very few line of codes and deploy them quickly. Recently Snowflakes acquired Streamlit, the future is bright.)
''')


with col2:
        st.header('For Future use.....If I am invited again')

        hold, tabA, tab1, tab3, tab4, tab5= st.tabs(['Hold','One', "Two","Three","Four","Conclusions"])

#         with tabA:
#             st.write('2006, University of Lagos Nigeria')
#             st.caption('Msc Economics')
#             st.write('2004, University of Lagos Nigeria')
#             st.caption('Post Graduate Diploma Manpower, Economics and Planning')
#             st.write('2002, University of Ado Ekiti Nigeria')
#             st.caption('Bachelor of Arts Degree in Philosophy')
        
#         with tab1:
#             struc = st.radio(label = 'Select to Consider an Experience', options = ['Data/Research Analyst Related Jobs',
#                                                             'Teaching and Mentorship',
#                                                             "Support Worker's Role",
#                                                             ])
#             st.write('---')
            
#             if struc == 'Data/Research Analyst Related Jobs':
#                 st.write('''  
# March 2018 - Current  
# Data Analyst   
# Alliance and Frontier Limited Lagos Nigeria 

# April 2014 - August 2018  
# Research Analyst  
# Dominion Research Solutions Lagos Nigeria

# January 2009 - February 2014  
# Research Manager  
# Primewaterview Limited Lagos
# ''')
#                 st.write('''- Analysed operational improvements against KPIs to measure progress.  
# - Analysed and tracked data to prepare forecasts and identify trends.    
# - Conducted data modelling and statistical analysis to note trends and draw conclusions.    
# - Collaborated cross-functionally with diverse teams in cleaning, assessing and interpreting data.
# - Evaluated performance data and established benchmarks for future tracking.  
# - Contributed to data capture, storage and forecast for analysis projects.  
# - Evaluated complex data sets to identify business opportunities and threats.
# ---
# - Aided company strategy through large-scale data consolidation, analysis and evidence presentation.
# - Developed charts and graphs on research findings to assess trends, presenting findings to management.
# - Assessed research to evaluate and determine trends and anomalies for further investigation.
# - Used data collected from research projects to make smart decisions when moving forward with business activities.
# - Conducted targeted research based on policy and process improvement goals, supporting company growth.
# - Informed and influenced policymakers through strategic research, reporting and analysis.
# - Designed and coordinated diverse qualitative and quantitative research, aiding business improvement strategies.
# - Improved project processes and operations through detailed advice from quantitative data findings.
# - Analysed data to determine opportunities for growth and greater efficiency.
# - Used various approaches to gathering and assessing data, including trend analysis, consumer research and best practice reviews.
# - Used data collected to form strategies to successfully grow business by 20%.
# - Developed competitive insight through strategic data capture, enhancing overall market intelligence.
# - Applied mathematical and programmatic methods to perform data extraction, cleansing and manipulation.
# ''')

#             if struc == 'Teaching and Mentorship':
#                 st.write('''
# September 2005 - Current  
# Teacher/Mentor  
# Self-Employed 

# April 2005 - March 2006 
# Teaching Assitant
# University of Lagos 
# - Sourced and developed a wide range of creative materials required for lessons, including workbooks, quizzes, games and presentations.
# - Monitored and documented student grades, behaviour and participation.
# - Monitored student development by marking coursework, monitoring classroom activities and assessing student behaviour.
# - Taught a wide range of subjects to students aged 9 - 30 in subjects, including Maths, Economics Data Science.
# - Planned educational events, trips, outings, clubs and activities to support Data Science curriculum.
# - Enhanced student outcomes by providing extra tutoring, mentoring and training support to underachieving students.
# - Created software application as lesson notes to help students to aid developments
# - Maintained excellent student relationships by providing a safe, positive learning environment for students.
# - Motivated students to achieve maximum potential through ongoing encouragement and providing extra support where needed.
# - Maintained strong student relationships by providing safe, positive learning environments for students.
# ''')

#             if struc == "Support Worker's Role":
#                 st.write('''
# 2021 - Current
# Support Worker: Part-time(Night Shifts)
# - Lending helping hands to medical staff in mental heatlh homes and hospitals
# - I am a certified Prevention Management of Violence and Aggression support staff
# '''
# )
#                 logo = Image.open('PMVA.png')
#                 st.image(logo,width= 100,caption = 'PMVA Certificate')
#                 if st.button('Enlarge Certificate'):
#                     st.image(logo,width=500,caption= 'PMVA Certificate')
#                     st.button('Close')




#         with tab3:
#             pas = Image.open('pass1.png')
#             st.image(pas,width= 250,caption = '')
#             # logo = Image.open('mo1.jpg')
#             # st.image(logo,width= 250,caption = 'My Daughter')
#             st.write('''My personal lifestyle revolves around: My Family, My Students, My Laptops and 
#             Arsenal Footbal Club. Meaning you can guess my location at any particular time of the day when I am not at work.
#             ''')
            
#             logo = Image.open('mo2.jpg')
#             st.image(logo,width= 250,caption = 'My daughter')

#             st.write('''Dont blame me if I troll Tottenham fans about their empty trophy cabinet, I
#             get trolled by Manchester United and Liverpool fans too. Annoyingly, Chelsea fans troll
#             me about my lack of trophies in Europe. I am always very happy to get one over Tottenham because
#             they are my next-door neigbours.''')
#             # st_player('https://www.youtube.com/watch?v=l3z_gICq-CQ',height=290)

#             st.video('https://www.youtube.com/watch?v=l3z_gICq-CQ', 'rb')
#             st.write('''Arsenal Women also did same against Tottenham Woman in the North London Derby that 
#             created a record for the most attended FA Women's Super League football game with 47,367 spectators
#             at the Emirate Stadium on the 24th of September 2022.''')
#             if st.button('Watch Highlight Here'):
#                 st.video('https://www.youtube.com/watch?v=o1y1fAeHgM8')
#                 st.button('Close')
            
            
