def draw_ascii_art(command, size=5):
    """Draws ASCII art based on user input."""
    try:
        return generate_custom_text_art(command)
    except NameError:
        return "Invalid command. Try 'square', 'triangle', 'circle', or 'custom'."
    

def generate_custom_text_art(text):
    """Generates ASCII art for custom text using pyfiglet."""
    try:
        import pyfiglet
        ascii_art = pyfiglet.figlet_format(text)
        return ascii_art
    except ImportError:
        return "pyfiglet module not installed. Run 'pip install pyfiglet' to enable custom text art."

# Example usage
if __name__ == "__main__":
    print("Welcome to the ASCII Art Drawer!")
    while True:
        command = input("\nEnter the shape to draw (or 'exit' to quit): ").strip().lower()
        if command == "exit":
            print("Goodbye!")
            break
        size = input("Enter the size of the shape (default is 5): ").strip()
        size = int(size) if size.isdigit() else 5
        print(draw_ascii_art(command, size))
