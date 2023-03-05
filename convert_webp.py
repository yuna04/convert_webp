from PIL import Image
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No arguments provided.\nPlease provide an argument.")
    elif len(sys.argv) > 1:
        print("You've provided too many arguments.\nOnly provide the file you wish to convert.")
    else:
        try:
            img = Image.open(sys.argv[1])
            s = sys.argv[1].split(".webp")
            print(s)
            img.save(f"{s[0]}.png", "PNG")
        except OSError:
            print(f"Cannot convert {sys.argv[1]}")

