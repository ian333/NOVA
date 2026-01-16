"""Markdown to PDF converter (fixed). Use: python md_to_pdf_fixed.py input.md output.pdf"""
import sys
import os

try:
    from markdown import markdown
except Exception:
    sys.exit("Missing dependency 'markdown'. Install with: pip install markdown")

try:
    from xhtml2pdf import pisa
except Exception:
    sys.exit("Missing dependency 'xhtml2pdf'. Install with: pip install xhtml2pdf")


def md_to_html(md_text, base_path):
    html = markdown(md_text, extensions=["fenced_code", "tables"])
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
                    attrs["src"] = "file://" + abs_path.replace('\\\\', '/')
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
                    attrs["src"] = "file://" + abs_path.replace('\\\\', '/')
                attr_str = "".join(f' {k}="{v}"' for k, v in attrs.items())
                self.out += f"<{tag}{attr_str}/>"
            else:
                attr_str = "".join(f' {k}="{v}"' for k, v in attrs)
                self.out += f"<{tag}{attr_str}/>"

    template = """
    <html>
    <head>
    <meta charset="utf-8">
    <style>
    body { font-family: DejaVu Sans, Arial, Helvetica, sans-serif; }
    pre { background: #f6f8fa; padding: 8px; }
    code { font-family: monospace; }
    table { border-collapse: collapse; }
    table, th, td { border: 1px solid #ddd; padding: 6px; }
    img { max-width: 100%; height: auto; }
    </style>
    </head>
    <body>
    ___CONTENT___
    </body>
    </html>
    """

    full = template.replace('___CONTENT___', html)
    return full


def convert(md_path, out_pdf):
    base = os.path.dirname(md_path)
    with open(md_path, 'r', encoding='utf-8') as f:
        md = f.read()
    html = md_to_html(md, base)
    tmp_html = out_pdf + '.tmp.html'
    with open(tmp_html, 'w', encoding='utf-8') as f:
        f.write(html)
    with open(tmp_html, 'r', encoding='utf-8') as fh:
        result = pisa.CreatePDF(fh.read(), dest=open(out_pdf, 'wb'))
    if result.err:
        print('Error: PDF generation returned errors')
        sys.exit(1)
    else:
        os.remove(tmp_html)
        print('PDF generado en', out_pdf)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python md_to_pdf_fixed.py input.md output.pdf')
        sys.exit(1)
    md_path = sys.argv[1]
    out_pdf = sys.argv[2]
    convert(md_path, out_pdf)
