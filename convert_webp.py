from PIL import Image, ImageSequence
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No arguments provided.\nPlease provide an argument.")
    elif len(sys.argv) > 2:
        print("You've provided too many arguments.\nOnly provide the file you wish to convert.")
    else:
        try:
            img = Image.open(sys.argv[1])
            s = sys.argv[-1].split(".")
            i = 0
            for frame in ImageSequence.Iterator(img):
                i += 1                
            if s[-1] != "webp":
                print("File is not webp and will not be converted.")
            elif i > 1:
                img.info.pop('background', None)
                img.save(f"{s[0]}.gif", "GIF", save_all=True)
            else:
                img.save(f"{s[0]}.png", "PNG")
        except OSError:
            print(f"Cannot convert {sys.argv[1]}")