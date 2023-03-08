from PIL import Image, ImageSequence
import sys, os

def convert_png(img, s):
    img.save(f"{s[0]}.png", "PNG")

def convert_gif(img, s):
    img.info.pop('background', None)
    img.save(f"{s[0]}.gif", "GIF", save_all=True)

def checkIfAnimated(img, i):
    for frame in ImageSequence.Iterator(img):
        print(i)
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
                cwd = os.getcwd()
                file_list = os.listdir()
                for file in file_list:
                    print(file)
                    if file.split(".")[-1] == "webp":
                        img = Image.open(file)
                        s = file.split(".")
                        i = 0
                        i = checkIfAnimated(img, i)
                        print(i)
                        if i > 1:
                            convert_gif(img, s)
                        else:
                            convert_png(img, s)

            img = Image.open(sys.argv[1]) 
            s = sys.argv[-1].split(".")
            i = 0
            i = checkIfAnimated(img, i)
            if s[-1] != "webp":
                print("File is not webp and will not be converted.")
            elif i > 1:
                convert_gif(img, s)
            else:
                convert_png(img, s)
                
        except OSError:
            print(f"Cannot convert {sys.argv[1]}")