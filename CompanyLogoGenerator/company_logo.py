from PIL import Image, ImageDraw, ImageFont
import os
from art import text2art

def get_company_name():
    """
    Prompts the user for the company name or initials and validates the input.
    :return: A valid string entered by the user
    """
    while True:
        name = input("Enter the company name or initials: ").strip()
        if name:
            return name
        print("Please enter a valid company name or initials.")

def generate_ascii_logo(name):
    """
    Generates an ASCII art logo from the company name or initials.
    :param name: The company name or initials
    """
    ascii_art = text2art(name, font="block")  # Use 'block' font for a bold look
    print("\nASCII Logo:")
    print(ascii_art)

def generate_image_logo(name):
    """
    Generates an image logo from the company name or initials.
    :param name: The company name or initials
    """
    # Define image dimensions and background color
    width, height = 400, 200
    background_color = (255, 255, 255)  # White
    text_color = (0, 0, 0)  # Black

    # Create a blank image
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Load a font (use a default font if none is available)
    try:
        font = ImageFont.truetype("arial.ttf", 60)  # Use Arial font if available
    except IOError:
        font = ImageFont.load_default()

    # Calculate text size and position using textbbox
    text_bbox = draw.textbbox((0, 0), name, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # Draw the text on the image
    draw.text((x, y), name, fill=text_color, font=font)

    # Save the image
    output_path = "company_logo.png"
    image.save(output_path)
    print(f"\nImage logo saved as '{output_path}'.")

if __name__ == "__main__":
    print("Welcome to the Company Logo Generator! 🎨")

    # Get user input
    company_name = get_company_name()

    # Generate ASCII logo
    generate_ascii_logo(company_name)

    # Generate image logo
    generate_image_logo(company_name)