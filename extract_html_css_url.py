import requests
from bs4 import BeautifulSoup
import tkinter as tk

def extract_html_css():
    url = url_entry.get()
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    css_files = soup.find_all('link', rel='stylesheet')
    inline_css = soup.find_all('style')
    html_output.delete('1.0', tk.END)
    css_output.delete('1.0', tk.END)
    html_output.insert(tk.END, html_content)
    for css_file in css_files:
        css_url = css_file['href']
        css_response = requests.get(css_url)
        css_content = css_response.text
        css_output.insert(tk.END, css_content)
    for css in inline_css:
        css_output.insert(tk.END, css.string)

# Create the GUI window
window = tk.Tk()
window.title('Website HTML/CSS Extractor')

# Create the URL input field and button
url_label = tk.Label(window, text='Enter URL:')
url_label.pack()
url_entry = tk.Entry(window)
url_entry.pack()
extract_button = tk.Button(window, text='Extract HTML/CSS', command=extract_html_css)
extract_button.pack()

# Create the HTML output field
html_label = tk.Label(window, text='HTML:')
html_label.pack()
html_output = tk.Text(window, height=10)
html_output.pack()

# Create the CSS output field
css_label = tk.Label(window, text='CSS:')
css_label.pack()
css_output = tk.Text(window, height=10)
css_output.pack()

# Run the GUI window
window.mainloop()



