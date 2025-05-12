from tkinter import Tk
from tkhtmlview import HTMLLabel

root = Tk()
root.title("HTML com link")

html_content = """
<h2>Bem-vindo!</h2>
<p>Visite o <a href='https://www.python.org'>site oficial do Python</a>.</p>
"""

label = HTMLLabel(root, html=html_content)
label.pack(padx=10, pady=10)

root.mainloop()
