from PIL import Image
import sys

if __name__ == "__main__":
    try:
        img = Image.open(sys.argv[1])
        s = sys.argv[1].split(".webp")
        print(s)
        img.save(f"{s[0]}.png", "PNG")
    except OSError:
        print(f"Cannot convert {sys.argv[1]}")

