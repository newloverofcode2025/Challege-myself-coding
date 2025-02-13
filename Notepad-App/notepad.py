import tkinter as tk
from tkinter import filedialog, messagebox, font, colorchooser, ttk
import os
import enchant
class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Notepad")
        self.root.geometry("800x600")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=1, fill='both')

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_tab)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)
        self.edit_menu.add_command(label="Find", command=self.find_text)
        self.edit_menu.add_command(label="Replace", command=self.replace_text)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        self.view_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.view_menu.add_command(label="Word Wrap", command=self.toggle_word_wrap)
        self.view_menu.add_command(label="Font", command=self.change_font)
        self.view_menu.add_command(label="Zoom In", command=self.zoom_in)
        self.view_menu.add_command(label="Zoom Out", command=self.zoom_out)
        self.menu_bar.add_cascade(label="View", menu=self.view_menu)

        self.theme_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.theme_menu.add_command(label="Light Theme", command=self.light_theme)
        self.theme_menu.add_command(label="Dark Theme", command=self.dark_theme)
        self.theme_menu.add_command(label="Custom Theme", command=self.custom_theme)
        self.menu_bar.add_cascade(label="Theme", menu=self.theme_menu)

        self.status_bar = tk.Label(self.root, text="Ready", anchor='w')
        self.status_bar.pack(side='bottom', fill='x')

        self.tabs = []
        self.spell_checker = enchant.Dict("en_US")
        self.font_size = 12
        self.word_wrap = False

        self.new_tab()

    def new_tab(self):
        text_area = tk.Text(self.notebook, wrap='word', undo=True)
        self.notebook.add(text_area, text="Untitled")
        self.tabs.append(text_area)
        text_area.bind('<KeyRelease>', self.update_status_bar)
        text_area.bind('<KeyRelease>', self.check_spelling, add='+')
        text_area.bind('<Return>', self.auto_indent)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("Python files", "*.py"), ("HTML files", "*.html"), ("CSS files", "*.css"), ("JavaScript files", "*.js")])
        if file_path:
            text_area = tk.Text(self.notebook, wrap='word', undo=True)
            with open(file_path, "r") as file:
                text_area.insert(tk.END, file.read())
            self.notebook.add(text_area, text=os.path.basename(file_path))
            self.tabs.append(text_area)
            text_area.bind('<KeyRelease>', self.update_status_bar)
            text_area.bind('<KeyRelease>', self.check_spelling, add='+')
            text_area.bind('<Return>', self.auto_indent)

    def save_file(self):
        current_tab = self.notebook.nametowidget(self.notebook.select())
        file_path = filedialog.asksaveasfilename(filetypes=[("Text files", "*.txt"), ("Python files", "*.py"), ("HTML files", "*.html"), ("CSS files", "*.css"), ("JavaScript files", "*.js")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(current_tab.get(1.0, tk.END))
            self.notebook.tab(current_tab, text=os.path.basename(file_path))

    def exit_app(self):
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            self.root.destroy()

    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")

    def find_text(self):
        search_text = tk.simpledialog.askstring("Find", "Enter text to find:")
        if search_text:
            self.text_area.tag_remove("highlight", "1.0", tk.END)
            start_pos = "1.0"
            while True:
                start_pos = self.text_area.search(search_text, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(search_text)}c"
                self.text_area.tag_add("highlight", start_pos, end_pos)
                start_pos = end_pos
                self.text_area.tag_config("highlight", background="yellow")

    def replace_text(self):
        search_text = tk.simpledialog.askstring("Replace", "Enter text to find:")
        replace_text = tk.simpledialog.askstring("Replace", "Enter text to replace:")
        if search_text and replace_text:
            content = self.text_area.get(1.0, tk.END)
            new_content = content.replace(search_text, replace_text)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, new_content)

    def toggle_word_wrap(self):
        self.word_wrap = not self.word_wrap
        for tab in self.tabs:
            tab.config(wrap='word' if self.word_wrap else 'none')

    def change_font(self):
        font_tuple = font.askfont(self.root)
        if font_tuple:
            font_obj = font.Font(family=font_tuple['family'], size=font_tuple['size'], weight=font_tuple['weight'])
            for tab in self.tabs:
                tab.config(font=font_obj)

    def zoom_in(self):
        self.font_size += 2
        self.update_font()

    def zoom_out(self):
        if self.font_size > 2:
            self.font_size -= 2
            self.update_font()

    def update_font(self):
        font_obj = font.Font(family="Arial", size=self.font_size)
        for tab in self.tabs:
            tab.config(font=font_obj)

    def light_theme(self):
        for tab in self.tabs:
            tab.config(bg="white", fg="black")
        self.status_bar.config(bg="lightgray", fg="black")

    def dark_theme(self):
        for tab in self.tabs:
            tab.config(bg="black", fg="white")
        self.status_bar.config(bg="gray", fg="white")

    def custom_theme(self):
        color = colorchooser.askcolor(title="Choose a color")
        if color:
            for tab in self.tabs:
                tab.config(bg=color[1], fg="black")
            self.status_bar.config(bg=color[1], fg="black")

    def update_status_bar(self, event=None):
        current_tab = self.notebook.nametowidget(self.notebook.select())
        line, column = current_tab.index(tk.INSERT).split('.')
        self.status_bar.config(text=f"Line: {line} | Column: {column}")

    def check_spelling(self, event=None):
        current_tab = self.notebook.nametowidget(self.notebook.select())
        current_tab.tag_remove("misspelled", "1.0", tk.END)
        content = current_tab.get("1.0", tk.END)
        words = content.split()
        for word in words:
            if not self.spell_checker.check(word):
                start = f"1.0+{content.find(word)}c"
                end = f"{start}+{len(word)}c"
                current_tab.tag_add("misspelled", start, end)
        current_tab.tag_config("misspelled", foreground="red")

    def auto_indent(self, event=None):
        current_tab = self.notebook.nametowidget(self.notebook.select())
        line = current_tab.get('insert linestart', 'insert lineend')
        indent = len(line) - len(line.lstrip())
        current_tab.insert(tk.INSERT, '\n' + ' ' * indent)
        return 'break'

if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()