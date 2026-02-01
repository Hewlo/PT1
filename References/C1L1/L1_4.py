import webbrowser

webbrowser.open('https://www.ite.edu.sg')

firefox_path = '/bin/firefox'
webbrowser.register('firefox',None, webbrowser.BackgroundBrowser(firefox_path))
url = 'https://www.kagi.com'
webbrowser.get('firefox').open(url)
webbrowser.get('firefox').open_new_tab('https://www.sg')