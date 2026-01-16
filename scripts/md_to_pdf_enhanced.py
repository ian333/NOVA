"""Enhanced Markdown to PDF converter with NOVA branding.

This script converts markdown files to beautifully styled PDFs with:
- NOVA branding (red and blue colors)
- Professional fonts and typography
- Header and footer with logo and page numbers
- Styled code blocks, tables, and images
- Raspberry Pi handbook inspired design
"""
import sys
import os
from pathlib import Path
from markdown import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

def get_enhanced_css():
    """Return CSS with NOVA branding and professional styling."""
    
    # Get the path to the logo
    script_dir = Path(__file__).parent.parent
    logo_path = script_dir / "docs" / "assets" / "branding" / "nova_logo_small.png"
    logo_url = f"file://{logo_path.absolute()}"
    
    css = f"""
    @page {{
        size: A4;
        margin: 2.5cm 2cm 3cm 2cm;
        
        @top-left {{
            content: "";
            background-image: url('{logo_url}');
            background-size: 80px 20px;
            background-repeat: no-repeat;
            background-position: left center;
            width: 100px;
            height: 30px;
        }}
        
        @top-right {{
            content: string(section);
            font-family: 'DejaVu Sans', Arial, sans-serif;
            font-size: 9pt;
            color: #666;
            font-weight: 600;
        }}
        
        @bottom-center {{
            content: counter(page);
            font-family: 'DejaVu Sans', Arial, sans-serif;
            font-size: 10pt;
            color: #2563eb;
            font-weight: bold;
        }}
        
        @bottom-left {{
            content: "NOVA Development Board";
            font-family: 'DejaVu Sans', Arial, sans-serif;
            font-size: 8pt;
            color: #999;
        }}
    }}
    
    /* First page styling */
    @page :first {{
        margin-top: 1cm;
        
        @top-left {{
            content: none;
        }}
        
        @top-right {{
            content: none;
        }}
    }}
    
    * {{
        box-sizing: border-box;
    }}
    
    body {{
        font-family: 'DejaVu Sans', 'Segoe UI', Arial, sans-serif;
        font-size: 11pt;
        line-height: 1.6;
        color: #1f2937;
        background-color: white;
    }}
    
    /* Headings with NOVA colors */
    h1 {{
        font-family: 'DejaVu Sans', Arial, sans-serif;
        font-size: 28pt;
        font-weight: bold;
        color: #dc2626;  /* NOVA Red */
        margin: 0.8em 0 0.5em 0;
        padding-bottom: 0.3em;
        border-bottom: 3px solid #2563eb;  /* NOVA Blue */
        page-break-after: avoid;
        string-set: section content();
    }}
    
    h2 {{
        font-family: 'DejaVu Sans', Arial, sans-serif;
        font-size: 20pt;
        font-weight: bold;
        color: #2563eb;  /* NOVA Blue */
        margin: 0.9em 0 0.4em 0;
        page-break-after: avoid;
        border-left: 4px solid #dc2626;
        padding-left: 12px;
    }}
    
    h3 {{
        font-family: 'DejaVu Sans', Arial, sans-serif;
        font-size: 15pt;
        font-weight: 600;
        color: #dc2626;  /* NOVA Red */
        margin: 0.7em 0 0.3em 0;
        page-break-after: avoid;
    }}
    
    h4 {{
        font-family: 'DejaVu Sans', Arial, sans-serif;
        font-size: 13pt;
        font-weight: 600;
        color: #2563eb;  /* NOVA Blue */
        margin: 0.6em 0 0.3em 0;
        page-break-after: avoid;
    }}
    
    h5, h6 {{
        font-family: 'DejaVu Sans', Arial, sans-serif;
        font-size: 11pt;
        font-weight: 600;
        color: #4b5563;
        margin: 0.5em 0 0.3em 0;
    }}
    
    /* Paragraphs */
    p {{
        margin: 0.5em 0;
        text-align: justify;
        hyphens: auto;
    }}
    
    /* Links */
    a {{
        color: #2563eb;
        text-decoration: none;
        font-weight: 500;
    }}
    
    a:hover {{
        text-decoration: underline;
    }}
    
    /* Lists */
    ul, ol {{
        margin: 0.5em 0 0.5em 1.5em;
        padding: 0;
    }}
    
    li {{
        margin: 0.3em 0;
        line-height: 1.5;
    }}
    
    /* Code blocks - styled like Raspberry Pi */
    pre {{
        background: linear-gradient(135deg, #f3f4f6 0%, #e5e7eb 100%);
        border-left: 4px solid #2563eb;
        border-radius: 4px;
        padding: 12px 15px;
        margin: 1em 0;
        overflow-x: auto;
        font-family: 'DejaVu Sans Mono', 'Courier New', monospace;
        font-size: 9pt;
        line-height: 1.4;
        page-break-inside: avoid;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }}
    
    code {{
        font-family: 'DejaVu Sans Mono', 'Courier New', monospace;
        font-size: 9.5pt;
        background-color: #f3f4f6;
        padding: 2px 6px;
        border-radius: 3px;
        color: #dc2626;
    }}
    
    pre code {{
        background: none;
        padding: 0;
        color: #1f2937;
    }}
    
    /* Tables - professional style */
    table {{
        width: 100%;
        border-collapse: collapse;
        margin: 1em 0;
        font-size: 10pt;
        page-break-inside: avoid;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }}
    
    thead {{
        background: linear-gradient(135deg, #dc2626 0%, #2563eb 100%);
        color: white;
    }}
    
    th {{
        padding: 10px 12px;
        text-align: left;
        font-weight: 600;
        border: none;
    }}
    
    td {{
        padding: 8px 12px;
        border-bottom: 1px solid #e5e7eb;
    }}
    
    tbody tr:nth-child(even) {{
        background-color: #f9fafb;
    }}
    
    tbody tr:hover {{
        background-color: #eff6ff;
    }}
    
    /* Images */
    img {{
        max-width: 100%;
        height: auto;
        display: block;
        margin: 1.5em auto;
        border-radius: 6px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        page-break-inside: avoid;
    }}
    
    /* Blockquotes */
    blockquote {{
        margin: 1em 0;
        padding: 10px 15px 10px 20px;
        border-left: 4px solid #dc2626;
        background-color: #fef2f2;
        font-style: italic;
        color: #4b5563;
        border-radius: 0 4px 4px 0;
    }}
    
    /* Horizontal rules */
    hr {{
        border: none;
        height: 2px;
        background: linear-gradient(90deg, #dc2626 0%, #2563eb 100%);
        margin: 2em 0;
    }}
    
    /* Info boxes (styled divs) */
    .info-box {{
        background-color: #eff6ff;
        border: 2px solid #2563eb;
        border-radius: 6px;
        padding: 15px;
        margin: 1em 0;
        page-break-inside: avoid;
    }}
    
    .warning-box {{
        background-color: #fef2f2;
        border: 2px solid #dc2626;
        border-radius: 6px;
        padding: 15px;
        margin: 1em 0;
        page-break-inside: avoid;
    }}
    
    /* Page breaks */
    .page-break {{
        page-break-after: always;
    }}
    
    /* First page title styling */
    body > h1:first-child {{
        font-size: 36pt;
        text-align: center;
        color: #dc2626;
        margin-top: 1em;
        margin-bottom: 0.3em;
        border-bottom: 4px solid #2563eb;
        padding-bottom: 0.5em;
    }}
    
    /* Strong and emphasis */
    strong {{
        font-weight: 700;
        color: #dc2626;
    }}
    
    em {{
        font-style: italic;
        color: #2563eb;
    }}
    """
    
    return css

def md_to_html(md_text, base_path):
    """Convert markdown to HTML with image path fixes."""
    # Convert markdown to HTML
    html = markdown(md_text, extensions=["fenced_code", "tables", "nl2br"])
    
    # Fix image paths to absolute file:// URLs
    from html.parser import HTMLParser
    
    class ImgFixer(HTMLParser):
        def __init__(self):
            super().__init__()
            self.out = ""
        
        def handle_starttag(self, tag, attrs):
            if tag.lower() == "img":
                attrs = dict(attrs)
                src = attrs.get("src", "")
                if src and not (src.startswith("http://") or src.startswith("https://") or src.startswith("file://")):
                    abs_path = os.path.abspath(os.path.join(base_path, src))
                    if os.path.exists(abs_path):
                        attrs["src"] = "file://" + abs_path.replace('\\', '/')
                attr_str = "".join(f' {k}="{v}"' for k, v in attrs.items())
                self.out += f"<{tag}{attr_str}>"
            else:
                attr_str = "".join(f' {k}="{v}"' for k, v in attrs)
                self.out += f"<{tag}{attr_str}>"
        
        def handle_endtag(self, tag):
            self.out += f"</{tag}>"
        
        def handle_data(self, data):
            self.out += data
        
        def handle_startendtag(self, tag, attrs):
            if tag.lower() == "img":
                attrs = dict(attrs)
                src = attrs.get("src", "")
                if src and not (src.startswith("http://") or src.startswith("https://") or src.startswith("file://")):
                    abs_path = os.path.abspath(os.path.join(base_path, src))
                    if os.path.exists(abs_path):
                        attrs["src"] = "file://" + abs_path.replace('\\', '/')
                attr_str = "".join(f' {k}="{v}"' for k, v in attrs.items())
                self.out += f"<{tag}{attr_str}/>"
            else:
                attr_str = "".join(f' {k}="{v}"' for k, v in attrs)
                self.out += f"<{tag}{attr_str}/>"
    
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>NOVA Documentation</title>
    </head>
    <body>
    ___CONTENT___
    </body>
    </html>
    """
    
    full = template.replace('___CONTENT___', html)
    fixer = ImgFixer()
    fixer.feed(full)
    return fixer.out

def convert(md_path, out_pdf):
    """Convert markdown file to PDF with enhanced styling."""
    base = os.path.dirname(md_path)
    
    print(f"Reading {md_path}...")
    with open(md_path, 'r', encoding='utf-8') as f:
        md = f.read()
    
    print("Converting markdown to HTML...")
    html_content = md_to_html(md, base)
    
    print("Applying NOVA styling and generating PDF...")
    
    # Create font configuration
    font_config = FontConfiguration()
    
    # Create CSS
    css = CSS(string=get_enhanced_css(), font_config=font_config)
    
    # Convert to PDF
    HTML(string=html_content, base_url=base).write_pdf(
        out_pdf, 
        stylesheets=[css],
        font_config=font_config
    )
    
    print(f'✓ PDF generado exitosamente en {out_pdf}')
    print(f'  - Estilo NOVA aplicado (rojo y azul)')
    print(f'  - Tipografía profesional')
    print(f'  - Encabezados y números de página')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Uso: python md_to_pdf_enhanced.py input.md output.pdf')
        sys.exit(1)
    
    md_path = sys.argv[1]
    out_pdf = sys.argv[2]
    
    if not os.path.exists(md_path):
        print(f'Error: Archivo {md_path} no encontrado')
        sys.exit(1)
    
    convert(md_path, out_pdf)
