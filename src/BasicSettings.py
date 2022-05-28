def setBasic(window):
    window.title(window.my_title)
    window.geometry(f'{window.initWidth}x{window.initHeight}')
    window.resizable(0, 0)
    window.config(bg=window.bgColor)

    def center(window):
        screenWidth = window.winfo_screenwidth()
        screenHeight = window.winfo_screenheight()
        x = int((screenWidth - window.initWidth) / 2)
        y = int((screenHeight - window.initHeight) / 2)
        window.geometry(f'{window.initWidth}x{window.initHeight}+{x}+{y}')

    center(window)
