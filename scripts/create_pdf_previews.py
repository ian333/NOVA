"""Generate preview images from PDFs for documentation."""
from pdf2image import convert_from_path
from PIL import Image
from pathlib import Path
import os

def create_pdf_previews():
    """Create preview images from PDF files."""
    # Get directories relative to script location
    script_dir = Path(__file__).parent.parent
    docs_dir = script_dir / 'docs'
    output_dir = docs_dir / 'assets' / 'previews'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # PDF files to convert
    pdf_files = [
        'manual_for_kids.pdf',
        'Documento_NOVA.pdf',
        'NOVA_Guide.pdf'
    ]
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(docs_dir, pdf_file)
        if not os.path.exists(pdf_path):
            print(f"Skipping {pdf_file} - file not found")
            continue
        
        print(f"Converting {pdf_file}...")
        
        # Convert first page only
        images = convert_from_path(pdf_path, first_page=1, last_page=1, dpi=150)
        
        if images:
            img = images[0]
            
            # Create a thumbnail (800px wide)
            img.thumbnail((800, 1200), Image.Resampling.LANCZOS)
            
            # Save as PNG
            base_name = pdf_file.replace('.pdf', '')
            output_path = os.path.join(output_dir, f'{base_name}_preview.png')
            img.save(output_path, 'PNG')
            print(f"  ✓ Saved preview: {output_path}")
            
            # Also create a small thumbnail (400px)
            img_small = images[0].copy()
            img_small.thumbnail((400, 600), Image.Resampling.LANCZOS)
            output_path_small = os.path.join(output_dir, f'{base_name}_thumb.png')
            img_small.save(output_path_small, 'PNG')
            print(f"  ✓ Saved thumbnail: {output_path_small}")

if __name__ == '__main__':
    print("Generating PDF previews...")
    create_pdf_previews()
    print("Done!")
