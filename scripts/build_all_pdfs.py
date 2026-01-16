#!/usr/bin/env python3
"""Build all NOVA documentation PDFs with enhanced styling.

This script:
1. Finds all markdown files in docs/
2. Converts them to beautifully styled PDFs
3. Replaces old PDFs with new enhanced versions
4. Generates a README and index PDF from the main README.md
"""
import os
import sys
from pathlib import Path

# Add scripts directory to path
script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))

from md_to_pdf_enhanced import convert

def build_all_pdfs():
    """Build all documentation PDFs."""
    repo_root = script_dir.parent
    docs_dir = repo_root / "docs"
    
    # List of markdown files to convert
    markdown_files = [
        (docs_dir / "manual_for_kids.md", docs_dir / "manual_for_kids.pdf"),
        (docs_dir / "instructivo.md", docs_dir / "Documento_NOVA.pdf"),  # Replace old Documento_NOVA.pdf
        (repo_root / "README.md", docs_dir / "NOVA_Guide.pdf"),
    ]
    
    print("=" * 60)
    print("NOVA PDF Builder - Enhanced Edition")
    print("=" * 60)
    print()
    
    success_count = 0
    error_count = 0
    
    for md_file, pdf_file in markdown_files:
        if not md_file.exists():
            print(f"⚠ Saltando {md_file.name} - archivo no encontrado")
            error_count += 1
            continue
        
        try:
            print(f"📄 Procesando: {md_file.name}")
            convert(str(md_file), str(pdf_file))
            print(f"✓ Generado: {pdf_file.name}")
            print()
            success_count += 1
        except Exception as e:
            print(f"✗ Error procesando {md_file.name}: {e}")
            print()
            error_count += 1
    
    print("=" * 60)
    print(f"Resumen: {success_count} PDFs generados, {error_count} errores")
    print("=" * 60)
    
    if error_count > 0:
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(build_all_pdfs())
