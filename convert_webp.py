from PIL import Image, ImageSequence
import sys, os

def convert_png(img, s):
    img.save(f"{s[0]}.png", "PNG")

def convert_gif(img, s):
    img.info.pop('background', None)
    img.save(f"{s[0]}.gif", "GIF", save_all=True, disposal=2)

def convert_all():
    file_list = os.listdir()
    for file in file_list:
        if file.split(".")[-1] == "webp":
            img = Image.open(file)
            s = file.split(".")
            i = check_animated(img)
            if i > 1:
                convert_gif(img, s)
            else:
                convert_png(img, s)

def check_animated(img):
    i = 0
    for frame in ImageSequence.Iterator(img):
        i += 1
        if i >= 2:
            return i

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No arguments provided.\nPlease provide an argument.")
    elif len(sys.argv) > 2:
        print("You've provided too many arguments.\nOnly provide the file you wish to convert.")
    else:
        try:
            if sys.argv[1] == "ALL":
                convert_all()
            img = Image.open(sys.argv[1]) 
            s = sys.argv[-1].split(".")
            i = check_animated(img)
            if s[-1] != "webp":
                print("File is not webp and will not be converted.")
            elif i > 1:
                convert_gif(img, s)
            else:
                convert_png(img, s)
                
        except OSError:
            print(f"Some type of OS error lol")