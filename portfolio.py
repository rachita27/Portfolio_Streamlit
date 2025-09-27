import streamlit as st
from PIL import Image
import os

BASE_DIR = os.path.dirname(__file__)  
# MODEL_PATH = os.path.join(BASE_DIR, "models", "nova_logo.png")

# ---------------- CONFIG ----------------
st.set_page_config(page_title="My Portfolio", page_icon=":bar_chart:", layout="centered")

# ---------------- CUSTOM CSS ----------------
st.markdown(
    """
    <style>
    .stApp {
    background: linear-gradient(to right, #f8f9fa, #e9ecef); -- GREY
   --- background: linear-gradient(120deg, #e0c3fc, #f9f9f9); 
    --background: linear-gradient(120deg, #dde1e7, #f7f8fa);
   --background: linear-gradient(to right, #d0f0e4, #ffffff); --gREEN
    --background: linear-gradient(120deg, #e0f7fa, #f1f3f6);--WHITE
    --background: linear-gradient(to right, #f8f9fa, #e9ecef); -- GREY
    

    }
    </style>
    """,
    unsafe_allow_html=True
)
##
st.markdown(
    """
    <style>
    body {
        font-family: 'Segoe UI', sans-serif;
    }
    .hero-title {
        font-size: 60px;
        font-weight: bold;
        color: #222;
    }
    .hero-subtitle {
        font-size: 28px;
        color: #888;
    }
    .section-title {
        font-size: 34px;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 15px;
    }
    .project-card {
        border: 1px solid #eee;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 25px;
        background-color: white;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- HERO ----------------
col1, col2 = st.columns([2,1])
with col1:
    st.markdown('<p class="hero-title"><h1>Hi, I\'m Rachita 👋 </h1></p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle"> <h3> Senior Consultant | Senior Analyst | Data Scientist </h3> </p>', unsafe_allow_html=True)
    st.write("Analytics lead with 5+ years of experience delivering BI dashboards, ML solutions, and consulting insights which drives efficiency, improving customer experience, and enabling data-driven decisions.")
    # st.write("I turn data into actionable insights and build ML-driven solutions.")
    st.markdown("""
    <a href="https://drive.google.com/file/d/1j7pTlNxrvCtIhVpo0y_M2o8l7fR94eBJ/view?usp=drive_link" target="_blank"><button style='margin:5px'>📄 Download Resume</button></a>
    <a href="mailto:rachita.harjai97@gmail.com"><button style='margin:5px'>✉️ Contact Me</button></a>
    """, unsafe_allow_html=True)
with col2:
    os.path.join(BASE_DIR, "Rachita_Img.jpg")
    st.image(os.path.join(BASE_DIR, "Rachita_Img.jpg"), width=200)
    # st.image("https://avatars.githubusercontent.com/u/9919?s=280&v=4", width=200)

st.write("---")

# ---------------- ABOUT ----------------
# st.markdown('<p class="section-title">👨‍💻 About Me</p>', unsafe_allow_html=True)
with st.expander("**👨‍💻 About Me**"):
       st.write("""I’m a Data Science and Analytics professional with 5+ years of experience delivering data-driven solutions across consulting, utilities, and customer experience domains. My journey includes onshore consulting with British Gas UK and leadership experience managing analyst teams while driving measurable business impact.

My toolkit blends SQL, Python, R, Power BI, Tableau, Power Apps, Power Automate, and applied ML. I’ve built 30+ BI dashboards, predictive models, and automation solutions that have improved operational efficiency, optimized customer experience, and unlocked millions in business value.

Recently, I’ve showcased my ML and visualization expertise through projects such as:

📊 DataDNA challenge: Advanced exploratory analysis and visualization, uncovering hidden data patterns.

⚖️ Credit Risk Modeling: Built a Streamlit-powered ML app to predict loan default probabilities, combining model interpretability with an intuitive UI for decision-makers.

Some of my notable professional initiatives include:

         
🔹 Solver Buddy → AI-lite Power Apps–based recommendation engine for real-time issue diagnosis.


🔹 Guru Reporting → Automated ticketing & performance dashboards (Planner + SFTP + BI) improving productivity by 15%.


🔹 VOC Analytics → Text mining, clustering, and sentiment models that boosted NPS by 10 points.

I bring a consulting mindset + technical expertise, enabling me to translate ambiguous business problems into structured analytical solutions. Now, I’m looking to take on impactful roles as a Data Scientist, Senior Analyst, or Analytics Consultant, where I can combine business context, advanced analytics, and communication skills to deliver scalable value.""")

# st.write("""
# I am a passionate Data Scientist with strong experience in Machine Learning, Deep Learning, and Analytics.
# I love solving business problems with data, building models that scale, and creating dashboards that tell powerful stories.
# """)

# ---------------- EXPERIENCE ----------------
st.markdown('<p class="section-title"><h3>📌 Experience </h3> </p>', unsafe_allow_html=True)
# st.markdown('<div class="section-title"><span>💼</span> Experience</div>', unsafe_allow_html=True)
st.timeline = [
    {"year": "💼 2023 - 2025", "role": "Senior Analyst/Consultant", "org": "EXL Service (UK)", "desc": """As a Senior Analyst onshore with British Gas UK, I partnered with cross-functional teams to deliver customer care analytics, automation, and BI solutions that improved efficiency, reduced complaints, and enabled data-driven decision-making.

🔹Solver Buddy (Smart Rule Based Diagnostic Tool): 

Designed and led the development of a rule-based engine (R, SQL, Power Apps) to diagnose root causes of customer complaints and guide agents with resolution steps. Automated complaint-level diagnostics, integrated usage tracking with Dataverse, and visualized adoption in Power BI.

    📉 30% reduction in open complaints

    ⚡ 15% improvement in Average Handling Time (AHT)

    ✅ Standardized diagnostic workflows across teams, later adopted beyond Customer Care.

🔹Lead Generation Reporting: 

Built the first dedicated performance dashboard for Customer Ops & Partners, redefining metrics to capture lead quality, warm transfers, and conversion rates instead of just raw volumes. Automated logic validation and created new reporting structures in Power BI.

    🎯 Enabled targeted frontline coaching based on lead quality

    🔍 Improved visibility into poor-quality leads, driving corrective actions

    📈 Shifted focus from “quantity of leads” to “quality & conversion impact”
     
🔹Stakeholder Engagement & Leadership: 

Partnered directly with UK stakeholders, acted as the SME for CX analytics, and presented insights to senior leadership. Mentored junior analysts, coordinated Agile sprints, and ensured delivery of BI solutions aligned with business KPIs and customer experience goals.

"""},
    {"year": "💼 2022 - 2023", "role": "Senior Analyst/Consultant", "org": "EXL Service (India)", "desc": """
🔹Complaint Analytics & VOC/NPS Dashboards: 
     
Implemented Power BI dashboards with Power Automate integrations to track complaint categories, root causes, and closure timelines.

    📊 Delivered actionable insights that reduced issue backlog by 20% in 6 months

    🗣️ Supported NPS improvement of +10 points by highlighting VOC pain points

🔹Sentiment Analysis

    ⚡ Designed a cost-effective sentiment analysis solution that replaced voice profiling with text mining and keyword categorization, achieving 80–85% model accuracy in identifying promoter, detractor, and passive behaviors.

    🔍 Developed a custom sentiment dictionary using Neural Networks and K-Means clustering, improving classification accuracy by capturing contextual word relationships and handling negations missed by traditional dictionaries.

    📊 Built an interactive Power BI dashboard to visualize sentiment model performance and generate word clouds, enabling stakeholders to pinpoint customer pain points and driving a 10% increase in customer satisfaction scores.

🔹Debt Strategy Reporting: 

    📊 Built dynamic, customizable reporting tools for the Debt Strategy Team to monitor KPIs in real-time. The enhanced visibility supported strategy refinements and contributed to a £15M annual increase in debt collections.

    🔍 Enhanced reporting with dynamic filtering by agent, date, and debt type, allowing 200+ business users to drill down into KPIs such as Promise-to-Pay (PTP), Right Person Contact (RPC), and Payment Plan Setups to identify performance gaps.

🔹Process Automation & Reporting: 

Built automated pipelines (R + RS Connect + Power Automate) for recurring complaint and performance reporting, eliminating manual interventions and improving data availability to 99.9% uptime.


"""},
    {"year": "💼 2021 - 2022", "role": "Assistant Manger", "org": "EXL Service (India)", "desc": """

🔹 Model Migration & Optimization: 

Led the migration of a bespoke model into RShiny, improving usability, boosting performance by 3x, and driving adoption across teams for faster decision support.

🔹Automation & Pipelines: 
     
Developed Python functions to extract billing details from .mht files, reducing manual processing time by 80% and improving accuracy in financial reporting. Designed an end-to-end pipeline in R to process .lse files into Hadoop, ensuring 99.9% data availability with zero manual   

🔹 Commodity Pricing Data Model (CDM):
     
Redesigned the client’s energy pricing model by replicating an Alteryx workflow in R and Python after migrating data to AWS. Developed a margin calculation system that allocated cost curves by customer meter type and consumption. The solution improved margin accuracy by 15%, streamlined market trading decisions, and enhanced scalability of pricing operations.
        
"""}
]


for item in st.timeline:
    with st.expander(f"**{item['year']} : {item['role']} at {item['org']}**"):
        st.write(item["desc"])
# for item in st.timeline:
#     st.markdown(f"<div class='timeline-item'><h4>{item['year']} — {item['role']} at <i>{item['org']}</i></h4><p>{item['desc']}</p></div>", unsafe_allow_html=True)
# for item in st.timeline:
#     st.markdown(f"**{item['year']}** — {item['role']} at *{item['org']}*  ")
#     st.write(item['desc'])

# ---------------- SKILLS ----------------
st.markdown('<p class="section-title"> <br> </br> ⚡ Skills</p>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.progress(90)
    st.write("Python, SQL, R")
with col2:
    st.progress(85)
    st.write("Scikit-learn")
    # st.write("TensorFlow, PyTorch, Scikit-learn")
with col3:
    st.progress(80)
    st.write("Power BI, Streamlit")
    # st.write("Tableau, Plotly, Streamlit")

# ---------------- PROJECTS ----------------
st.markdown('<p class="section-title">🚀 Projects</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="project-card">
        <h4>📊 Nova Bank Credit Risk Analytics Challenge</h4>
        <p>Built a model which Predicts Probability of Default.</p>
        <a href="https://www.linkedin.com/posts/rachita-ai-enthusiast_datadna-datadna-datadna-activity-7376656769118531585-VpkU?utm_source=share&utm_medium=member_desktop&rcm=ACoAACq54EUBoF_nzCPWo1lI6wATBE_l_Kydrdc">🔗 LinkedIn Post with Repo Links</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="project-card">
        <h4> 🧠 Credit Risk Evaluation App</h4>
        <p>Streamlit App I built around the same problem, with What-If-Analysis feature.</p>
        <a href="https://www.linkedin.com/posts/rachita-ai-enthusiast_machinelearning-creditrisk-streamlit-activity-7377341081912287232-TP1P?utm_source=share&utm_medium=member_desktop&rcm=ACoAACq54EUBoF_nzCPWo1lI6wATBE_l_Kydrdc">🔗 LinkedIn Post & Repo Link</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="project-card">
        <h4>📈 Fitness Membership Growth Potential </h4>
        <p> Created Retention, Resource Utilization & Revenue Optimization Strategy.</p>
        <a href="https://www.linkedin.com/posts/rachita-ai-enthusiast_powerbi-datadna-analytics-activity-7365479353457025024-YJbr?utm_source=share&utm_medium=member_desktop&rcm=ACoAACq54EUBoF_nzCPWo1lI6wATBE_l_Kydrdc">🔗 LinkedIn Post with Repo Links</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="project-card">
        <h4> 🔍 Managing Employee Expenses</h4>
        <p>Power Apps real-time add, updates, attachments, and exports.</p>
        <a href="https://www.linkedin.com/posts/rachita-ai-enthusiast_powerapps-microsoftpowerplatform-expensetracker-activity-7334092560358944768-E2C4?utm_source=share&utm_medium=member_desktop&rcm=ACoAACq54EUBoF_nzCPWo1lI6wATBE_l_Kydrdc">🔗 LinkedIn Post</a>
    </div>
    """, unsafe_allow_html=True)

# ---------------- CONTACT ----------------

st.markdown('<p class="section-title"><br> </br>📬 Get in Touch</p>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""[LinkedIn](https://www.linkedin.com/in/rachita-ai-enthusiast/)
    """)
with col2:
    st.markdown("[GitHub](https://github.com/rachita27)")
with col3:
    st.markdown("[Email](mailto:rachita.harjai97@gmail.com)")
# with col2:
#     st.markdown("[GitHub](https://github.com/yourusername)")
# with col3:

#     st.markdown("[Email](mailto:your.email@example.com)")



