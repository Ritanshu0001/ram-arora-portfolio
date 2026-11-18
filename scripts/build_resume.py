"""Build Ram Arora's one-page resume. Requires reportlab; accepts an output PDF path."""
from pathlib import Path
import sys
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.utils import ImageReader
from reportlab import rl_config

rl_config.useA85 = 0

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'dist' if (ROOT / 'dist').is_dir() else ROOT
OUTPUT = Path(sys.argv[1]) if len(sys.argv) > 1 else SITE / 'documents/Ram_Arora_Resume.pdf'
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
W, H = A4
LEFT, RIGHT = 34, W - 34
WIDTH = RIGHT - LEFT
INK = colors.HexColor('#1D2738')
ACCENT = colors.HexColor('#283D6A')
MUTED = colors.HexColor('#526071')
RULE = colors.HexColor('#B9C3D0')
c = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1)
c.setTitle('Ram Arora Resume - Finance, Operations and Supply Chain')
c.setAuthor('Ram Arora')
c.setSubject('Education, academic projects, research and certifications')
y = H - 31
BODY = 9.1
LEADING = 11
style = ParagraphStyle('body', fontName='Helvetica', fontSize=BODY, leading=LEADING, textColor=INK)

def para(text, x=LEFT, width=WIDTH, size=BODY, leading=LEADING, gap=0, color=INK):
    global y
    s = ParagraphStyle('line', parent=style, fontSize=size, leading=leading, textColor=color)
    p = Paragraph(text, s)
    _, height = p.wrap(width, H)
    y -= height
    p.drawOn(c, x, y)
    y -= gap

def section(title):
    global y
    y -= 7
    c.setFillColor(ACCENT)
    c.setFont('Helvetica-Bold', 10)
    c.drawString(LEFT, y - 9, title.upper())
    y -= 13
    c.setStrokeColor(RULE)
    c.setLineWidth(.45)
    c.line(LEFT, y, RIGHT, y)
    y -= 5

def bullet(text):
    global y
    c.setFont('Helvetica', BODY)
    c.setFillColor(INK)
    c.drawString(LEFT + 2, y - BODY, '\u2022')
    para(text, x=LEFT + 12, width=WIDTH - 12)

def entry(title, date='', subtitle=''):
    global y
    date_width = c.stringWidth(date, 'Helvetica', 8.2) + 15 if date else 0
    top = y
    para(f'<b>{title}</b>', width=WIDTH - date_width, color=ACCENT)
    if date:
        c.setFont('Helvetica', 8.2)
        c.setFillColor(MUTED)
        c.drawRightString(RIGHT, top - BODY, date)
    if subtitle:
        para(subtitle, size=8.1, leading=10, color=MUTED)

c.setFillColor(ACCENT)
c.setFont('Helvetica-Bold', 24)
c.drawString(LEFT, y - 23, 'Ram Arora')
y -= 31
para('FINANCE  |  OPERATIONS  |  SUPPLY CHAIN', size=9, leading=12, color=ACCENT)
para('<link href="https://ramarora09.com" color="#283D6A">ramarora09.com</link>  |  <link href="mailto:ramarora0132@gmail.com" color="#283D6A">ramarora0132@gmail.com</link>', size=8.5, leading=11)
para('<link href="https://www.linkedin.com/in/ram-arora-7a7316354/" color="#283D6A">linkedin.com/in/ram-arora-7a7316354/</link>  |  +91 6395929182', size=8.5, leading=11)

photo_size = 65
photo_x, photo_y = RIGHT - photo_size, H - 96
c.saveState()
clip = c.beginPath()
clip.roundRect(photo_x, photo_y, photo_size, photo_size, 7)
c.clipPath(clip, stroke=0)
c.drawImage(ImageReader(str(SITE / 'assets/ram-arora-portrait.jpg')), photo_x, photo_y, photo_size, photo_size, preserveAspectRatio=True, mask='auto')
c.restoreState()
y = min(y, H - 99)

section('Professional summary')
para('Economics (Honors) graduate pursuing an MBA at Lovely Professional University, with academic work in corporate finance, statistical research and product marketing. Seeking opportunities in finance, operations and supply chain management. Brings Excel-based analysis and Six Sigma Foundations coursework in business operations and process improvement.')

section('Skills and interests')
para('<b>Finance:</b> Financial Statement &amp; Ratio Analysis, Capital Structure Analysis, Peer Benchmarking, Accounting Basics, Investment Research, Portfolio Tracking')
para('<b>Operations foundations:</b> Business Operations, Process Improvement, Six Sigma Foundations')
para('<b>Supply chain interests:</b> Supply Chain Management, Inventory Planning, Procurement, Logistics')
para('<b>Tools:</b> MS Excel, MS Office, PowerPoint, Google Sheets')
para('<b>Strengths:</b> Negotiation, Adaptability, Business Analysis, Communication, Analytical Thinking')
para('<b>Languages:</b> English, Hindi, Punjabi')

section('Research and publications')
entry('An Analysis of Sources of Finance and Financing Strategy of Exide Industries Limited', 'Sep 2026', 'Co-author | Corporate Finance I | Selected for publication')
bullet('Analyzed financing sources, capital structure and financial performance over FY2021-22 to FY2025-26.')
bullet('Benchmarked Exide against Amara Raja and HBL Engineering using financial ratios and annual reports.')
y -= 3
entry('Disease Burden and Life Expectancy Trends')
para('Academic project on implications for the pharmaceutical and health insurance sectors.', color=MUTED)

section('Academic projects')
entry('Rooh-e-Attar | Marketing &amp; Sales', 'Group project')
bullet('Co-developed an affordable attar brand; the team reported <b>INR 51,650 in sales revenue</b>.')
bullet('Applied STP, brand identity and packaging; promoted products through Instagram posts, reels and stories.')
y -= 3
entry('Comparative Health &amp; Socio-Economic Study', 'Oct 2026')
bullet('Analyzed 12 World Bank indicators across India, China and the US (2019-2023; 15 observations).')
bullet('Used Python, pandas, SciPy and Matplotlib for descriptive statistics, correlation, regression and forecasting.')
y -= 3
entry('Project CONNECT | Reliance Industries Limited Case Study', 'Oct 2026', 'MBA group project | Organizational Behaviour | MGNM581')
bullet('Proposed six initiatives to improve communication and engagement among contract workers.')
bullet('Proposed a "You Spoke, We Acted" feedback process to record suggestions, assign responsibility and track follow-up.')

section('Certifications and learning')
certificates = [
 ('Six Sigma Foundations | LinkedIn Learning', 'Nov 18, 2026'),
 ('Understanding Capital Markets | LinkedIn Learning', 'Nov 17, 2026'),
 ('Managing Your Personal Investments | LinkedIn Learning', 'Oct 2026'),
 ('Asset Classes and Financial Market Fundamentals | LinkedIn Learning', 'Oct 2026'),
 ('Corporate Finance Foundations | LinkedIn Learning', 'Oct 2026'),
 ('Artificial Intelligence and Business Strategy | LinkedIn Learning', 'Sep 2026'),
 ('NISM Series XII - Securities Market Foundation', ''),
 ('Financial Markets Management (NSQF Level 4) | CBSE / NSE Academy', 'May 2023'),
 ('NISM Series V-A - Mutual Fund Distributor Certification', 'Pursuing'),
 ('AI Literacy Essentials Program | EY', ''),
 ('Excel Modelling and Stock Trading', ''),
]
for text, date in certificates:
    top = y
    para(text, width=WIDTH - 80)
    if date:
        c.setFillColor(MUTED)
        c.setFont('Helvetica', 8.2)
        c.drawRightString(RIGHT, top - BODY, date)

section('Campus activities')
bullet('Organized and led personal finance and investment workshops for the Economics Society at PU.')
bullet('Member of the Commerce and Management Society at PU.')

section('Education')
entry('Lovely Professional University | Phagwara, Punjab', '2026 - 2028')
para('Master of Business Administration - Pursuing')
y -= 2
entry('Panjab University | Chandigarh', '2023 - 2026')
para('Bachelor of Arts (Hons.) Economics | Percentage: 61%')
y -= 2
entry('Rainbow School | Saharanpur, Uttar Pradesh', '2022 - 2023')
para('Intermediate | Percentage: 86%')

if y < 28:
    raise RuntimeError(f'Resume overflow: bottom of content is {y:.1f} pt')
c.showPage()
c.save()
print(f'Created {OUTPUT}; bottom margin {y:.1f} pt')
