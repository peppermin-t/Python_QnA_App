from PIL import Image

if __name__ == '__main__':
    img = Image.open('assets/MainWindowBackground.jpg')
    img.save('assets/MainWindowBackground.gif')
