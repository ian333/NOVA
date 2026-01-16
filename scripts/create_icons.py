"""Create decorative icons and elements for NOVA PDFs."""
from PIL import Image, ImageDraw
import os

def create_icons():
    """Create simple icon set for documentation."""
    output_dir = '/home/runner/work/NOVA/NOVA/docs/assets/branding'
    
    # Icon 1: Warning/Alert icon (red circle with exclamation)
    img = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([10, 10, 90, 90], fill=(220, 38, 38), outline=(180, 30, 30), width=3)
    draw.rectangle([45, 30, 55, 60], fill='white')
    draw.ellipse([45, 70, 55, 80], fill='white')
    img.save(os.path.join(output_dir, 'icon_warning.png'))
    print("Created warning icon")
    
    # Icon 2: Info icon (blue circle with i)
    img = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([10, 10, 90, 90], fill=(37, 99, 235), outline=(29, 78, 216), width=3)
    draw.rectangle([45, 40, 55, 70], fill='white')
    draw.ellipse([45, 30, 55, 40], fill='white')
    img.save(os.path.join(output_dir, 'icon_info.png'))
    print("Created info icon")
    
    # Icon 3: Success/Check icon (green circle with checkmark)
    img = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([10, 10, 90, 90], fill=(34, 197, 94), outline=(22, 163, 74), width=3)
    # Draw checkmark
    draw.line([30, 50, 45, 65], fill='white', width=8)
    draw.line([45, 65, 70, 35], fill='white', width=8)
    img.save(os.path.join(output_dir, 'icon_success.png'))
    print("Created success icon")
    
    # Icon 4: Code icon (brackets)
    img = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Left bracket
    draw.line([30, 25, 20, 25], fill=(37, 99, 235), width=5)
    draw.line([20, 25, 20, 75], fill=(37, 99, 235), width=5)
    draw.line([20, 75, 30, 75], fill=(37, 99, 235), width=5)
    # Right bracket
    draw.line([70, 25, 80, 25], fill=(220, 38, 38), width=5)
    draw.line([80, 25, 80, 75], fill=(220, 38, 38), width=5)
    draw.line([80, 75, 70, 75], fill=(220, 38, 38), width=5)
    img.save(os.path.join(output_dir, 'icon_code.png'))
    print("Created code icon")
    
    # Decorative element: Corner decoration
    img = Image.new('RGBA', (200, 200), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Draw arc with gradient effect
    for i in range(5):
        color_red = int(220 - i * 30)
        color_blue = int(38 + i * 40)
        draw.arc([10 + i*5, 10 + i*5, 190 - i*5, 190 - i*5], 
                 start=180, end=270, fill=(color_red, color_blue, 100), width=3)
    img.save(os.path.join(output_dir, 'corner_decoration.png'))
    print("Created corner decoration")

if __name__ == '__main__':
    create_icons()
    print("All icons created successfully!")
