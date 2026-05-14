from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
    Table, TableStyle
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

# ── Colour palette ──────────────────────────────────────────────
NAVY   = colors.HexColor("#1B2A4A")
TEAL   = colors.HexColor("#2E86AB")
LIGHT  = colors.HexColor("#F0F4F8")
GRAY   = colors.HexColor("#555555")
LGRAY  = colors.HexColor("#888888")
WHITE  = colors.white
BLACK  = colors.black

PAGE_W, PAGE_H = A4
LM = RM = 1.8 * cm
TM = BM = 1.5 * cm

doc = SimpleDocTemplate("Pratigya_Singh_Resume.pdf",
    pagesize=A4,
    leftMargin=LM, rightMargin=RM,
    topMargin=TM, bottomMargin=BM,
)

# ── Styles ───────────────────────────────────────────────────────
def S(name, **kw):
    return ParagraphStyle(name, **kw)

name_style   = S("Name",   fontName="Helvetica-Bold",   fontSize=22, textColor=NAVY,  spaceAfter=2)
tagline_style= S("Tag",    fontName="Helvetica",         fontSize=10, textColor=TEAL,  spaceAfter=2)
contact_style= S("Cont",   fontName="Helvetica",         fontSize=8.5,textColor=GRAY,  spaceAfter=0)
sec_style    = S("Sec",    fontName="Helvetica-Bold",    fontSize=10, textColor=WHITE, spaceAfter=0, spaceBefore=0, leading=14)
body_style   = S("Body",   fontName="Helvetica",         fontSize=8.8,textColor=BLACK, spaceAfter=2, leading=13)
bullet_style = S("Bul",    fontName="Helvetica",         fontSize=8.8,textColor=BLACK, spaceAfter=2, leading=13,
                            leftIndent=10, firstLineIndent=-10, bulletIndent=0)
bold_body    = S("BBod",   fontName="Helvetica-Bold",    fontSize=8.8,textColor=NAVY,  spaceAfter=1)
sub_style    = S("Sub",    fontName="Helvetica",         fontSize=8.2,textColor=LGRAY, spaceAfter=3)
skill_label  = S("SLbl",   fontName="Helvetica-Bold",    fontSize=8.8,textColor=NAVY)
skill_val    = S("SVal",   fontName="Helvetica",         fontSize=8.8,textColor=BLACK)

def section_header(title):
    """Dark navy bar with white text."""
    tbl = Table([[Paragraph(title, sec_style)]], colWidths=[PAGE_W - LM - RM])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",  (0,0), (-1,-1), NAVY),
        ("TOPPADDING",  (0,0), (-1,-1), 4),
        ("BOTTOMPADDING",(0,0),(-1,-1), 4),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
    ]))
    return tbl

def bullet(text):
    return Paragraph(f"• &nbsp;{text}", bullet_style)

def sp(h=3):
    return Spacer(1, h)

# ── Build story ───────────────────────────────────────────────────
story = []

# ── HEADER ────────────────────────────────────────────────────────
story.append(Paragraph("PRATIGYA SINGH", name_style))
story.append(Paragraph("Data Analyst &amp; Python Developer", tagline_style))
story.append(Paragraph(
    "pratigyasingh085@gmail.com &nbsp;|&nbsp; +91 83192 91980 &nbsp;|&nbsp; "
    "github.com/pratigya0 &nbsp;|&nbsp; linkedin.com/in/pratigya-singh-rajput-8713801ba",
    contact_style))
story.append(sp(6))
story.append(HRFlowable(width="100%", thickness=1.5, color=TEAL))
story.append(sp(6))

# ── PROFESSIONAL SUMMARY ──────────────────────────────────────────
story.append(section_header("PROFESSIONAL SUMMARY"))
story.append(sp(5))
story.append(Paragraph(
    "Detail-oriented <b>Data Analyst and Python Developer</b> with hands-on experience in "
    "end-to-end AI application development, data pipeline design, and real-time computer vision "
    "systems. Skilled in Python, SQL, and ML frameworks with exposure to CRM analytics platforms "
    "(Google Analytics, Looker Studio, Salesforce Marketing Cloud). Adept at translating complex "
    "data into actionable insights to support data-driven decision-making.",
    body_style))
story.append(sp(8))

# ── TECHNICAL SKILLS ──────────────────────────────────────────────
story.append(section_header("TECHNICAL SKILLS"))
story.append(sp(5))

skills = [
    ("Languages",          "Python, SQL"),
    ("Data & Analytics",   "Pandas, NumPy, Matplotlib, Looker Studio, Google Analytics, Google Tag Manager"),
    ("ML / AI Frameworks", "TensorFlow, Scikit-learn, YOLO, OpenCV (LangChain – learning)"),
    ("AI Concepts",        "Machine Learning, NLP, Neural Networks, CNNs, Representation Learning, QCNNs"),
    ("CRM & Marketing",    "Salesforce Marketing Cloud (SFMC), MoEngage"),
    ("Other Tools",        "Git, Jupyter Notebook, VS Code"),
]

for label, val in skills:
    row = Table(
        [[Paragraph(f"{label}:", skill_label), Paragraph(val, skill_val)]],
        colWidths=[4.2*cm, PAGE_W - LM - RM - 4.2*cm],
    )
    row.setStyle(TableStyle([
        ("VALIGN",         (0,0),(-1,-1),"TOP"),
        ("TOPPADDING",     (0,0),(-1,-1), 2),
        ("BOTTOMPADDING",  (0,0),(-1,-1), 2),
        ("LEFTPADDING",    (0,0),(-1,-1), 0),
        ("RIGHTPADDING",   (0,0),(-1,-1), 0),
    ]))
    story.append(row)

story.append(sp(8))

# ── EXPERIENCE ───────────────────────────────────────────────────
story.append(section_header("PROFESSIONAL EXPERIENCE"))
story.append(sp(5))

story.append(Table(
    [[Paragraph("Data Analyst Intern – Publicis Groupe", bold_body),
      Paragraph("Jul 2025 – Sep 2025", sub_style)]],
    colWidths=[(PAGE_W-LM-RM)*0.72, (PAGE_W-LM-RM)*0.28],
    style=[("ALIGN",(1,0),(1,0),"RIGHT"), ("TOPPADDING",(0,0),(-1,-1),0),
           ("BOTTOMPADDING",(0,0),(-1,-1),0), ("LEFTPADDING",(0,0),(-1,-1),0),
           ("RIGHTPADDING",(0,0),(-1,-1),0)],
))
story.append(Paragraph("On-site | Bhopal, India", sub_style))
story.append(sp(3))

exp_bullets = [
    "Built and maintained analytics dashboards in <b>Looker Studio</b> integrating data from multiple marketing sources, enabling data-driven campaign decisions.",
    "Configured and managed <b>Google Analytics</b> and <b>Google Tag Manager</b> tracking setups for production web properties.",
    "Worked with <b>Salesforce Marketing Cloud (SFMC)</b> and <b>MoEngage</b> CRM platforms to analyse customer journeys and segment performance.",
    "Automated analytical workflows that reduced manual reporting effort, improving team productivity.",
    "Collaborated with cross-functional teams to translate business requirements into analytical solutions using real production data systems.",
]
for b in exp_bullets:
    story.append(bullet(b))

story.append(sp(8))

# ── PROJECTS ─────────────────────────────────────────────────────
story.append(section_header("PROJECTS"))
story.append(sp(5))

# Project 1
story.append(Table(
    [[Paragraph("Derma Quantum – AI-Powered Skin Disease Diagnosis", bold_body),
      Paragraph("Python | TensorFlow | ResNet50 | QCNN", sub_style)]],
    colWidths=[(PAGE_W-LM-RM)*0.6, (PAGE_W-LM-RM)*0.4],
    style=[("ALIGN",(1,0),(1,0),"RIGHT"), ("TOPPADDING",(0,0),(-1,-1),0),
           ("BOTTOMPADDING",(0,0),(-1,-1),0), ("LEFTPADDING",(0,0),(-1,-1),0),
           ("RIGHTPADDING",(0,0),(-1,-1),0)],
))
story.append(sp(3))
proj1_bullets = [
    "Developed a web-based diagnostic framework combining <b>ResNet50</b> and <b>Quantum Convolutional Neural Networks (QCNNs)</b> for accurate skin disease classification.",
    "Designed and trained a multi-class model on <b>25,000+ images across 16 disease classes</b>, achieving a <b>19% improvement</b> in classification accuracy over baseline.",
    "Improved system interpretability by 30% and code modularity by 80%, resulting in a scalable and production-ready diagnostic pipeline.",
]
for b in proj1_bullets:
    story.append(bullet(b))

story.append(sp(6))

# Project 2
story.append(Table(
    [[Paragraph("Real-Time Vehicle Counting System", bold_body),
      Paragraph("Python | OpenCV | YOLO", sub_style)]],
    colWidths=[(PAGE_W-LM-RM)*0.6, (PAGE_W-LM-RM)*0.4],
    style=[("ALIGN",(1,0),(1,0),"RIGHT"), ("TOPPADDING",(0,0),(-1,-1),0),
           ("BOTTOMPADDING",(0,0),(-1,-1),0), ("LEFTPADDING",(0,0),(-1,-1),0),
           ("RIGHTPADDING",(0,0),(-1,-1),0)],
))
story.append(sp(3))
proj2_bullets = [
    "Built a real-time vehicle detection and counting pipeline using <b>YOLO</b>, <b>background subtraction</b>, and <b>contour detection</b>, achieving <b>95% accuracy</b> across diverse video datasets.",
    "Optimised processing pipeline to handle video streams at <b>30 FPS</b>, ensuring low-latency, scalable performance for traffic monitoring use cases.",
    "Designed modular components allowing easy integration with external traffic management systems.",
]
for b in proj2_bullets:
    story.append(bullet(b))

story.append(sp(8))

# ── EDUCATION ────────────────────────────────────────────────────
story.append(section_header("EDUCATION"))
story.append(sp(5))

edu = [
    ("B.Tech – Computer Science (AI & ML Specialization)",
     "Lakshmi Narain College of Technology, Bhopal",
     "CGPA: 7.21", "2022 – 2025"),
    ("Diploma – Computer Science & Engineering",
     "Government Women's Polytechnic College, Bhopal",
     "CGPA: 7.75", "2019 – 2022"),
]
for deg, inst, cgpa, yr in edu:
    story.append(Table(
        [[Paragraph(deg, bold_body), Paragraph(yr, sub_style)]],
        colWidths=[(PAGE_W-LM-RM)*0.78, (PAGE_W-LM-RM)*0.22],
        style=[("ALIGN",(1,0),(1,0),"RIGHT"), ("TOPPADDING",(0,0),(-1,-1),0),
               ("BOTTOMPADDING",(0,0),(-1,-1),0), ("LEFTPADDING",(0,0),(-1,-1),0),
               ("RIGHTPADDING",(0,0),(-1,-1),0)],
    ))
    story.append(Paragraph(f"{inst} &nbsp;|&nbsp; {cgpa}", sub_style))
    story.append(sp(5))

story.append(sp(4))

# ── CERTIFICATIONS & ACHIEVEMENTS ────────────────────────────────
story.append(section_header("CERTIFICATIONS & ACHIEVEMENTS"))
story.append(sp(5))

certs = [
    "<b>Google Analytics Certified</b> – Google (2025)",
    "<b>Amazon ML Summer School</b> – Selected for cohort focused on Applied Machine Learning",
    "Built end-to-end BI dashboards integrating multiple data sources, enabling data-driven decision-making for marketing teams.",
]
for c in certs:
    story.append(bullet(c))

story.append(sp(6))

# ── Build ─────────────────────────────────────────────────────────
doc.build(story)
print("✅ Resume generated successfully!")