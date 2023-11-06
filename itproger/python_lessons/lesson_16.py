import webbrowser

def validator(func): # декоратор
    def wrapper(url):
        if '.' in url:
            func(url)
        else:
            print('Invalid URL')
    return wrapper

@validator
def open_browser(url):
    webbrowser.open(url)

open_browser('https://google.com')