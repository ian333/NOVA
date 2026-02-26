from pathlib import Path
import sys
try:
    import PyPDF2
except Exception as e:
    print('MISSING_PYPDF2')
    raise

pdf_path = Path('..') / 'manual_intermedio.pdf'
out_path = Path('manual_intermedio_text.txt')
reader = PyPDF2.PdfReader(str(pdf_path))
with out_path.open('w', encoding='utf-8') as f:
    f.write(f'PDF: {pdf_path}\nPages: {len(reader.pages)}\n\n')
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ''
        f.write('--- PAGE %d ---\n' % i)
        f.write(text)
        f.write('\n\n')
print('EXTRACTION_COMPLETE', out_path)
print('PAGES', len(reader.pages))
