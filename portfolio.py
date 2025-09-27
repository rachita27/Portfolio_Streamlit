import streamlit as st
from PIL import Image
import os

BASE_DIR = os.path.dirname(__file__)  
# MODEL_PATH = os.path.join(BASE_DIR, "models", "nova_logo.png")

# ---------------- CONFIG ----------------
st.set_page_config(page_title="My Portfolio", page_icon=":bar_chart:", layout="wide")

# ---------------- CUSTOM CSS ----------------
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
    st.write("I turn data into actionable insights and build ML-driven solutions.")
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
st.markdown('<p class="section-title">👨‍💻 About Me</p>', unsafe_allow_html=True)
st.write("""I'm a Lead BI & CX Analytics professional with 5+ years of experience building data-driven solutions for global enterprises, including 2 years onshore with British Gas UK, delivering strategic insights and automation through EXL Consulting.

I specialize in Power BI, R, SQL, Python, Power Apps & Automate, Tableau, ML and have led 30+ BI dashboards, AI-lite solutions, and VOC/NPS reporting systems across customer care and commercial operations. My projects have enabled measurable improvements like:
• 30% drop in complaints via diagnostic logic
• 15% boost in agent efficiency (RPH)
• 10-point lift in Net Promoter Score

Notable initiatives include:
🔹 Solver Buddy – a Power Apps-based recommendation engine for real-time issue diagnosis
🔹 Guru Reporting – automated ticket + performance dashboards (Planner + SFTP + BI)
🔹 VOC root cause analysis using text mining, clustering, and sentiment models

I've directly partnered with UK stakeholders, managed analyst teams, and delivered BI strategies aligned to both business KPIs and customer insights. I'm now looking to drive larger impact in roles like:
Lead BI Analyst | Analytics Consultant | VOC/CX Analytics Lead | Senior Business Analyst | Data Science Specialist (Applied)

Let’s connect if you're building the next-gen analytics function — I bring the toolkit, mindset, and track record to lead it.""")

# st.write("""
# I am a passionate Data Scientist with strong experience in Machine Learning, Deep Learning, and Analytics.
# I love solving business problems with data, building models that scale, and creating dashboards that tell powerful stories.
# """)

# ---------------- EXPERIENCE ----------------
st.markdown('<p class="section-title"><h3>📌 Experience </h3> </p>', unsafe_allow_html=True)
# st.markdown('<div class="section-title"><span>💼</span> Experience</div>', unsafe_allow_html=True)
st.timeline = [
    {"year": "💼 2023 - 2025", "role": "Senior Analyst/Consultant", "org": "EXL Service (UK)", "desc": """Lead a dynamic customer care team focused on delivering exceptional client experiences and solutions. Act as the primary liaison between clients and internal teams to manage expectations, gather requirements, and deliver tailored end products.

I’ve also led multiple cross-functional teams and projects, with a particular focus on AI-driven solutions. One notable project involved developing an AI model to assist customer service agents by identifying issues and recommending actions to improve resolution times and outcomes. In this project, I collaborated with SMEs to build and integrate the solution into a Power Apps platform, which helps to identify the issue & take necessary action. It contains features of response collection required for tracking usage and enabling ongoing agent coaching.

I worked on a project aimed at identifying the root causes of customer complaints and analyzing associated details. This solution empowered the client to pinpoint key issues and implement improvements to enhance the customer experience. The process involved understanding client needs, formulating a detailed plan, creating templates, and developing a Power BI dashboard to provide actionable insights.

Develop and oversee Power BI reports to provide actionable insights and data-driven solutions for clients and stakeholders. Design and implement Power Apps in combination with Microsoft Power Automate (Flows) to streamline processes, enhance efficiency, and solve complex business challenges.

Foster collaboration within the team to ensure high-quality deliverables while maintaining a customer-first approach."""},
    {"year": "💼 2022 - 2023", "role": "Senior Analyst/Consultant", "org": "EXL Service (India)", "desc": """Managed & Led the Customer Care Team's workload, focusing on the creation of new Management Information (MI) reports and the maintenance of existing ones.

Developed and deployed Power BI dashboards and R scripts to provide actionable insights and data-driven visualizations.

Designed and implemented Net Promoter Score (NPS) reporting to monitor agent performance and track customer experience trends over time.

Conducted text mining on customer feedback to identify recurring themes, linking them to underlying factors influencing detractor or promoter behaviors.

Built a sentiment analysis framework using a basic Neural Net Model and k-Nearest Neighbors (kNN) to score sentiment. Created a custom data dictionary based on customer feedback to address limitations in existing dictionaries, such as the inability to handle negations of positive sentiments.

Provided deep insights that enabled stakeholders to enhance customer satisfaction and refine business strategies."""},
    {"year": "💼 2021 - 2022", "role": "Assistant Manger", "org": "EXL Service (India)", "desc": """Designed, reported, and maintained the Customer Care Dashboard by utilizing R for scripting and Power BI for data visualization.

Conducted sentiment analysis on customer feedback to derive true sentiments, addressing nuances such as negations, and used text mining techniques to uncover themes, visualized through Wordclouds in Power BI, to identify drivers impacting NPS scores.

Developed a Python function to automate the extraction of billing-related details from .mht files.

Built an end-to-end data pipeline in R to process .lse files and deliver final outputs to Hadoop, enhancing efficiency and scalability.

Created a Pricing Pipeline for a UK utilities firm by developing logic in R and Python, enabling computation of future costs and revenue projections for newly acquired customers.

Contributed to the migration and optimization of a bespoke model by converting it into an RShiny tool for improved usability and performance."""}
]

for item in st.timeline:
    st.markdown(f"<div class='timeline-item'><h4>{item['year']} — {item['role']} at <i>{item['org']}</i></h4><p>{item['desc']}</p></div>", unsafe_allow_html=True)
# for item in st.timeline:
#     st.markdown(f"**{item['year']}** — {item['role']} at *{item['org']}*  ")
#     st.write(item['desc'])

# ---------------- SKILLS ----------------
st.markdown('<p class="section-title">⚡ Skills</p>', unsafe_allow_html=True)
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
# st.markdown('<p class="section-title">🚀 Projects</p>', unsafe_allow_html=True)

# col1, col2 = st.columns(2)
# with col1:
#     st.markdown("""
#     <div class="project-card">
#         <h4>📊 Sales Forecasting</h4>
#         <p>Built a forecasting model with Prophet to predict sales trends.</p>
#         <a href="https://github.com/yourusername/sales-forecasting">🔗 View Project</a>
#     </div>
#     """, unsafe_allow_html=True)
#     st.markdown("""
#     <div class="project-card">
#         <h4>📈 Interactive Dashboard</h4>
#         <p>Developed a financial dashboard with Plotly & Streamlit.</p>
#         <a href="https://github.com/yourusername/financial-dashboard">🔗 View Project</a>
#     </div>
#     """, unsafe_allow_html=True)

# with col2:
#     st.markdown("""
#     <div class="project-card">
#         <h4>🤖 Sentiment Analysis</h4>
#         <p>Created an NLP model to classify customer reviews in real time.</p>
#         <a href="https://github.com/yourusername/sentiment-analysis">🔗 View Project</a>
#     </div>
#     """, unsafe_allow_html=True)
#     st.markdown("""
#     <div class="project-card">
#         <h4>🧠 Image Classifier</h4>
#         <p>Trained a CNN model to classify product images with TensorFlow.</p>
#         <a href="https://github.com/yourusername/image-classifier">🔗 View Project</a>
#     </div>
#     """, unsafe_allow_html=True)

# ---------------- CONTACT ----------------

st.markdown('<p class="section-title"><br> </br>📬 Get in Touch</p>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("[LinkedIn](https://www.linkedin.com/in/rachita-ai-enthusiast/)")
    st.markdown("[GitHub](https://github.com/rachita27)")
    st.markdown("[Email](mailto:rachita.harjai97@gmail.com)")
# with col2:
#     st.markdown("[GitHub](https://github.com/yourusername)")
# with col3:

#     st.markdown("[Email](mailto:your.email@example.com)")



