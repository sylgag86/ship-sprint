from pathlib import Path
from fpdf import FPDF

base = Path('/home/Syl/.openclaw/workspace/ship-sprint-container/product')
source = base / 'guide-master-v1.md'
out = base / '24-hour-ship-sprint-v1.pdf'

lines = source.read_text(encoding='utf-8').splitlines()
subs = {'•':'-','—':'-','–':'-','“':'"','”':'"','’':"'",'…':'...'}

def clean(s:str)->str:
    for a,b in subs.items(): s=s.replace(a,b)
    return s.encode('latin-1','ignore').decode('latin-1')

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Cover
pdf.add_page()
pdf.set_fill_color(12,18,45); pdf.rect(0,0,210,297,style='F')
pdf.set_text_color(110,231,255); pdf.set_font('Helvetica','B',16)
pdf.cell(0,20,clean('OPENCLAW EDITION'),align='C'); pdf.ln(18)
pdf.set_text_color(255,255,255); pdf.set_font('Helvetica','B',34)
pdf.multi_cell(0,16,clean('24-Hour\nShip Sprint'),align='C'); pdf.ln(5)
pdf.set_text_color(190,198,224); pdf.set_font('Helvetica','',16)
pdf.cell(0,10,clean('Build in 12. First Sale in the Next 12.'),align='C'); pdf.ln(18)
pdf.set_text_color(155,164,194); pdf.set_font('Helvetica','',12)
pdf.multi_cell(0,7,clean('A practical execution playbook for founders, freelancers, and creators\nwho need to ship now and generate revenue signal fast.'),align='C')
pdf.set_y(-40); pdf.set_text_color(130,140,170); pdf.cell(0,10,clean('Dev1 - 2026-03-02'),align='C')

# Content
pdf.add_page(); pdf.set_text_color(20,20,20)
for raw in lines:
    s=clean(raw.strip())
    if not s: pdf.ln(2); continue
    if s.startswith('|') or s.startswith('```'): continue
    pdf.set_x(15)
    if s.startswith('# '):
        pdf.set_font('Helvetica','B',18); pdf.ln(3); pdf.multi_cell(180,10,s[2:])
    elif s.startswith('## '):
        pdf.set_font('Helvetica','B',14); pdf.ln(2); pdf.multi_cell(180,8,s[3:])
    elif s.startswith('### '):
        pdf.set_font('Helvetica','B',12); pdf.multi_cell(180,7,s[4:])
    elif s == '---':
        y=pdf.get_y(); pdf.set_draw_color(180,180,180); pdf.line(15,y,195,y); pdf.ln(3)
    elif s.startswith('- '):
        pdf.set_font('Helvetica','',11); pdf.multi_cell(180,6,f"- {s[2:]}")
    elif s.startswith('> '):
        pdf.set_font('Helvetica','I',11); pdf.multi_cell(180,6,s[2:])
    else:
        pdf.set_font('Helvetica','',11); pdf.multi_cell(180,6,s)

pdf.output(str(out))
print(out)
