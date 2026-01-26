"""Create a simple NOVA logo in red and blue colors."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import os

def create_nova_logo():
    """Create NOVA logo with red and blue colors."""
    # Get output directory relative to script location
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / 'docs' / 'assets' / 'branding'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create a new image with white background
    width, height = 800, 200
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Define colors (NOVA red and blue)
    red = (220, 38, 38)  # Vibrant red
    blue = (37, 99, 235)  # Vibrant blue
    
    # Draw a gradient background bar
    for y in range(40, 160):
        ratio = (y - 40) / 120
        color = tuple(int(red[i] * (1 - ratio) + blue[i] * ratio) for i in range(3))
        draw.rectangle([(10, y), (790, y+1)], fill=color)
    
    # Try to use a default font
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 100)
    except:
        font = ImageFont.load_default()
    
    # Draw the text "NOVA" in white
    text = "NOVA"
    # Calculate text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Center the text
    x = (width - text_width) // 2
    y = (height - text_height) // 2 - 10
    
    # Draw shadow
    draw.text((x+3, y+3), text, fill=(0, 0, 0, 128), font=font)
    # Draw text
    draw.text((x, y), text, fill='white', font=font)
    
    # Save the logo
    output_path = output_dir / 'nova_logo.png'
    img.save(output_path)
    print(f"Logo created at {output_path}")
    
    # Create a smaller version for headers
    img_small = img.resize((400, 100), Image.Resampling.LANCZOS)
    output_path_small = output_dir / 'nova_logo_small.png'
    img_small.save(output_path_small)
    print(f"Small logo created at {output_path_small}")

if __name__ == '__main__':
    create_nova_logo()
