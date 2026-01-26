# NOVA Documentation - Visual Style Guide

## Overview

NOVA documentation now features a professional, visually attractive design inspired by Raspberry Pi handbooks. The PDFs are designed to be engaging for children, technicians, and engineers.

## Brand Colors

### Primary Colors
- **NOVA Red**: `#DC2626` (RGB: 220, 38, 38)
  - Used for: Main headings (H1, H3), emphasis, warnings
  
- **NOVA Blue**: `#2563EB` (RGB: 37, 99, 235)
  - Used for: Sub-headings (H2, H4), links, info boxes, accents

### Secondary Colors
- **Background**: White (#FFFFFF)
- **Text**: Dark gray (#1F2937)
- **Code blocks**: Light gray gradient (#F3F4F6 to #E5E7EB)

## Typography

### Fonts
- **Body text**: DejaVu Sans, 11pt
- **Code**: DejaVu Sans Mono, 9-9.5pt
- **Headings**: DejaVu Sans Bold, various sizes

### Heading Sizes
- **H1**: 28pt (36pt for first page title)
- **H2**: 20pt
- **H3**: 15pt
- **H4**: 13pt
- **H5-H6**: 11pt

## Visual Elements

### Logo
The NOVA logo features a red-to-blue gradient background with white text.
- Full size: `docs/assets/branding/nova_logo.png` (800x200px)
- Header size: `docs/assets/branding/nova_logo_small.png` (400x100px)

### Icons
Located in `docs/assets/branding/`:
- `icon_warning.png` - Red alert icon
- `icon_info.png` - Blue information icon
- `icon_success.png` - Green check icon
- `icon_code.png` - Code brackets icon
- `corner_decoration.png` - Decorative element

### Layout Features

#### Headers and Footers
- **Top left**: NOVA logo (80x20px)
- **Top right**: Section name
- **Bottom center**: Page number (blue, bold)
- **Bottom left**: "NOVA Development Board"

#### Margins
- Top: 2.5cm
- Bottom: 3cm
- Left/Right: 2cm

### Styling Details

#### Headings
- **H1**: Red text, blue bottom border (3px)
- **H2**: Blue text, red left border (4px), left padding
- **H3**: Red text
- **H4**: Blue text

#### Code Blocks
- Light gray gradient background
- Blue left border (4px)
- Rounded corners (4px)
- Drop shadow
- Monospace font

#### Tables
- Red-to-blue gradient header
- White text in header
- Alternating row colors
- Hover effect (light blue)
- Drop shadow

#### Images
- Centered with auto margins
- Rounded corners (6px)
- Drop shadow
- Max width 100%

#### Blockquotes
- Red left border (4px)
- Light red background (#FEF2F2)
- Italic text

#### Horizontal Rules
- Red-to-blue gradient (2px height)

## Building PDFs

### Using the Build Script

Generate all PDFs with enhanced styling:

```bash
python3 scripts/build_all_pdfs.py
```

This will:
1. Convert `docs/manual_for_kids.md` → `docs/manual_for_kids.pdf`
2. Convert `docs/instructivo.md` → `docs/Documento_NOVA.pdf`
3. Convert `README.md` → `docs/NOVA_Guide.pdf`

### Manual Conversion

Convert a single markdown file:

```bash
python3 scripts/md_to_pdf_enhanced.py input.md output.pdf
```

Example:
```bash
python3 scripts/md_to_pdf_enhanced.py docs/manual_for_kids.md docs/manual_for_kids.pdf
```

## Regenerating Branding Assets

### Logo
```bash
python3 scripts/create_nova_logo.py
```

Creates:
- `docs/assets/branding/nova_logo.png`
- `docs/assets/branding/nova_logo_small.png`

### Icons
```bash
python3 scripts/create_icons.py
```

Creates all icon files in `docs/assets/branding/`

## Dependencies

Required Python packages:
```bash
pip install markdown weasyprint Pillow
```

### What Each Package Does
- **markdown**: Converts Markdown to HTML
- **weasyprint**: Converts HTML/CSS to PDF with advanced styling
- **Pillow**: Creates logo and icon images

## Design Philosophy

The NOVA visual style follows these principles:

1. **Accessibility**: Clear typography, good contrast, readable sizes
2. **Professionalism**: Clean layout, consistent spacing, quality fonts
3. **Brand Identity**: Red and blue colors throughout, NOVA logo presence
4. **Engagement**: Colorful elements, styled code blocks, visual hierarchy
5. **Raspberry Pi Inspiration**: Similar handbook feel, technical yet friendly

## Tips for Creating Content

### For Best Results

1. **Use proper markdown headings** (# ## ###)
2. **Include code in fenced blocks** with ``` 
3. **Add images** with descriptive alt text
4. **Use tables** for structured data
5. **Break up long content** with horizontal rules (---)
6. **Emphasize key points** with **bold** or *italic*

### Markdown Features Supported

- ✅ Headings (H1-H6)
- ✅ Paragraphs with justified text
- ✅ Bold and italic
- ✅ Bullet and numbered lists
- ✅ Code blocks (fenced with ```)
- ✅ Inline code with `backticks`
- ✅ Tables
- ✅ Images (PNG, JPEG, WebP)
- ✅ Links
- ✅ Blockquotes
- ✅ Horizontal rules
- ✅ Line breaks

## Examples

### Creating a Warning Section

```markdown
> **Importante**: Usa cables USB que sean de datos, no solo de carga.
```

### Adding Code Examples

```markdown
```python
from machine import Pin
led = Pin(25, Pin.OUT)
led.value(1)
```
```

### Using Tables

```markdown
| Component | Pin | Function |
|-----------|-----|----------|
| LED       | 25  | Output   |
| Button    | 15  | Input    |
```

## File Structure

```
NOVA/
├── docs/
│   ├── assets/
│   │   └── branding/
│   │       ├── nova_logo.png
│   │       ├── nova_logo_small.png
│   │       ├── icon_*.png
│   │       └── corner_decoration.png
│   ├── manual_for_kids.md
│   ├── manual_for_kids.pdf ← Enhanced
│   ├── instructivo.md
│   ├── Documento_NOVA.pdf ← Enhanced
│   └── NOVA_Guide.pdf ← Enhanced
├── scripts/
│   ├── md_to_pdf_enhanced.py ← Main converter
│   ├── build_all_pdfs.py ← Batch builder
│   ├── create_nova_logo.py
│   └── create_icons.py
└── README.md
```

## Updating the Style

To modify the visual style, edit `scripts/md_to_pdf_enhanced.py`:

- **Colors**: Change RGB values in `get_enhanced_css()`
- **Fonts**: Modify font-family in CSS
- **Spacing**: Adjust margins and padding
- **Borders**: Change border styles and colors

After making changes, rebuild all PDFs:
```bash
python3 scripts/build_all_pdfs.py
```

## License

The NOVA visual style and branding assets are part of the NOVA project.

---

**Questions?** Check the scripts in the `scripts/` directory for implementation details.
