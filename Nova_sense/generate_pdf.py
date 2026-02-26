#!/usr/bin/env python3
"""
Generador simple de PDF para el manual Cosmo-Gyroscope.
- Lee `Manual_Cosmo_Gyroscope.md` y coloca texto en un PDF A4.
- Inserta imágenes si se encuentran en `manual/images/` cuando el markdown contiene
  etiquetas tipo `[IMAGE: images/filename.png]`.

Requisitos: `reportlab`
pip install reportlab

Ejecución:
python generate_pdf.py
"""
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Preformatted
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors

HERE = os.path.dirname(__file__)
MD_PATH = os.path.join(HERE, 'Manual_Cosmo_Gyroscope.md')
OUT_PDF = os.path.join(HERE, 'Manual_Cosmo_Gyroscope.pdf')
IMAGES_DIR = os.path.join(HERE, 'images')

styles = getSampleStyleSheet()
# Use unique style names to avoid KeyError if styles already exist in stylesheet
if 'GHeading1' not in styles:
    styles.add(ParagraphStyle(name='GHeading1', fontSize=18, leading=22, spaceAfter=8))
if 'GHeading2' not in styles:
    styles.add(ParagraphStyle(name='GHeading2', fontSize=14, leading=18, spaceAfter=6))
if 'GBody' not in styles:
    styles.add(ParagraphStyle(name='GBody', fontSize=10.5, leading=14))
code_style = ParagraphStyle('GCode', fontName='Courier', fontSize=8, leading=10)


def build_flowables(md_text):
    flowables = []
    lines = md_text.splitlines()
    in_code = False
    code_block = []
    for line in lines:
        if line.startswith('```'):
            if not in_code:
                in_code = True
                code_block = []
            else:
                in_code = False
                flowables.append(Preformatted('\n'.join(code_block), code_style))
            continue
        if in_code:
            code_block.append(line)
            continue
        line = line.rstrip()
        if line.startswith('# '):
            flowables.append(Paragraph(line[2:].strip(), styles['GHeading1']))
            continue
        if line.startswith('## '):
            flowables.append(Paragraph(line[3:].strip(), styles['GHeading2']))
            continue
        if line.startswith('### '):
            flowables.append(Paragraph(line[4:].strip(), styles['GHeading2']))
            continue
        if line.startswith('[IMAGE:') and line.endswith(']'):
            fname = line[len('[IMAGE:'): -1].strip()
            # Allow path like images/foo.png or just foo.png
            candidate = os.path.join(HERE, fname) if os.path.isabs(fname) or 'images' in fname else os.path.join(IMAGES_DIR, fname)
            if os.path.exists(candidate):
                try:
                    img = Image(candidate)
                    img._restrictSize(160*mm, 110*mm)
                    flowables.append(img)
                except Exception as e:
                    flowables.append(Paragraph(f"[ERROR inserting image: {fname} - {e}]", styles['GBody']))
            else:
                # Placeholder box
                flowables.append(Paragraph(f"[IMAGEN NO ENCONTRADA: {fname}]", styles['GBody']))
            flowables.append(Spacer(1, 6))
            continue
        if line.strip() == '':
            flowables.append(Spacer(1, 6))
            continue
        # normal paragraph
        flowables.append(Paragraph(line, styles['GBody']))
    return flowables


def main():
    if not os.path.exists(MD_PATH):
        print('No se encontró', MD_PATH)
        return
    with open(MD_PATH, 'r', encoding='utf-8') as f:
        md_text = f.read()
    doc = SimpleDocTemplate(OUT_PDF, pagesize=A4,
                            rightMargin=20*mm, leftMargin=20*mm, topMargin=20*mm, bottomMargin=20*mm)
    flowables = build_flowables(md_text)
    doc.build(flowables)
    print('PDF generado en:', OUT_PDF)

if __name__ == '__main__':
    main()
