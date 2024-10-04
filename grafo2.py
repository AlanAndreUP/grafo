import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import pandas as pd
from docx import Document
from bs4 import BeautifulSoup
import csv

import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
class HTMLTagAutomata:
    def __init__(self):
        self.state = 'q0'
        self.errors = []
        self.transitions = self._build_transition_table()
        
    def _build_transition_table(self):
        tags = {
            'html': ['h', 't', 'm', 'l'],
            'head': ['h', 'e', 'a', 'd'],
            'body': ['b', 'o', 'd', 'y'],
            'header': ['h', 'e', 'a', 'd', 'e', 'r'],
            'main': ['m', 'a', 'i', 'n'],
            'section': ['s', 'e', 'c', 't', 'i', 'o', 'n'],
            'article': ['a', 'r', 't', 'i', 'c', 'l', 'e'],
            'aside': ['a', 's', 'i', 'd', 'e'],
            'h1': ['h', '1'],
            'h2': ['h', '2'],
            'h3': ['h', '3'],
            'h4': ['h', '4'],
            'h5': ['h', '5'],
            'h6': ['h', '6'],
            'p': ['p'],
            'br': ['b', 'r'],
            'pre': ['p', 'r', 'e'],
            'style': ['s', 't', 'y', 'l', 'e'],
            'script': ['s', 'c', 'r', 'i', 'p', 't'],
            'meta': ['m', 'e', 't', 'a'],
            'base': ['b', 'a', 's', 'e'],
            'blockquote': ['b', 'l', 'o', 'c', 'k', 'q', 'u', 'o', 't', 'e']
        }

        transitions = {}
        for tag, chars in tags.items():
            current = 'q0'
            for i, char in enumerate(chars):
                next_state = f'q_{tag[:i+1]}'  # Create state for each letter of the tag
                transitions[(current, char)] = next_state
                current = next_state
            transitions[(current, '>')] = f'q_{tag}_close'  # State when tag closes
            
            # Handle closing tags (</tag>)
            current = 'qc_open'
            for i, char in enumerate(chars):
                next_state = f'qc_{tag[:i+1]}'
                transitions[(current, char)] = next_state
                current = next_state
            transitions[(current, '>')] = f'qc_{tag}_close'

        transitions[('q0', '<')] = 'q1'
        transitions[('q1', '/')] = 'qc_open'
        
        return transitions

    def transition(self, input_string):
        for input_char in input_string:
            previous_state = self.state
            next_state = self.transitions.get((self.state, input_char))

            if next_state:
                self.state = next_state
            else:
                self.errors.append((previous_state, input_char))
                self.error()

    def error(self):
        # Reset the state to initial on error
        self.state = 'q0'
    
    def is_final_state(self):
        return '_close' in self.state

    def get_current_tag(self):
        if '_close' in self.state:
            parts = self.state.split('_')
            return '_'.join(parts[1:-1])  # Extract tag name
        return None

class HTMLValidator:
    def __init__(self):
        self.automata = HTMLTagAutomata()
        self.tag_stack = []
        self.errors = []

    def validate(self, html_text):
        inside_tag = False
        current_tag = ''
        closing = False

        for char in html_text:
            if char == '<':
                inside_tag = True
                current_tag = ''
                closing = False
            elif char == '/':
                closing = True
            elif char == '>':
                inside_tag = False
                if closing:
                    # Handle closing tag
                    if self.tag_stack and self.tag_stack[-1] == current_tag:
                        self.tag_stack.pop()
                    else:
                        self.errors.append(f"Unexpected closing tag: {current_tag}")
                else:
                    # Handle opening tag
                    self.tag_stack.append(current_tag)
                current_tag = ''
            elif inside_tag:
                current_tag += char

    def get_validation_result(self):
        if not self.errors and not self.tag_stack:
            return True, "HTML structure is valid"
        
        error_messages = []
        if self.errors:
            error_messages.extend(self.errors)
        if self.tag_stack:
            error_messages.append(f"Unclosed tags: {', '.join(reversed(self.tag_stack))}")
        
        return False, "\n".join(error_messages)
    def report_occurrences(self, output_file):
        occurrences = []

        for i, error in enumerate(self.errors):
            occurrences.append({'Error': error, 'Line': i + 1})

        for tag in self.tag_stack:
            occurrences.append({'Error': f'Unclosed tag: {tag}', 'Line': 'N/A'})

        # Write to CSV
        with open(output_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Error', 'Line'])
            writer.writeheader()
            writer.writerows(occurrences)

class HTMLValidatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("HTML Tag Validator")
        self.setup_ui()
        
    def setup_ui(self):
        # UI configuration
        self.text_area = scrolledtext.ScrolledText(self.root, width=60, height=20)
        self.text_area.pack(pady=10, padx=10)
        
        validate_button = tk.Button(self.root, text="Validate HTML", command=self.validate_html)
        validate_button.pack(pady=5)

        load_button = tk.Button(self.root, text="Load File", command=self.load_file)
        load_button.pack(pady=5)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=5)

    def validate_html(self):
        html_text = self.text_area.get("1.0", tk.END)
        validator = HTMLValidator()
        validator.validate(html_text)
        is_valid, message = validator.get_validation_result()
        
        if is_valid:
            self.result_label.config(text="Valid HTML!", fg="green")
        else:
            self.result_label.config(text=f"Invalid HTML:\n{message}", fg="red")

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[
            ("All Files", "*.*"),
            ("CSV Files", "*.csv"),
            ("Excel Files", "*.xlsx"),
            ("Word Documents", "*.docx"),
            ("HTML Files", "*.html")
        ])
        
        if file_path:
            content = ""
            if file_path.endswith('.csv'):
                content = self.load_csv(file_path)
            elif file_path.endswith('.xlsx'):
                content = self.load_excel(file_path)
            elif file_path.endswith('.docx'):
                content = self.load_docx(file_path)
            elif file_path.endswith('.html'):
                content = self.load_html(file_path)
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, content)

    def load_csv(self, file_path):
        df = pd.read_csv(file_path)
        return df.to_string(index=False)

    def load_excel(self, file_path):
        df = pd.read_excel(file_path)
        return df.to_string(index=False)

    def load_docx(self, file_path):
        doc = Document(file_path)
        content = []
        for paragraph in doc.paragraphs:
            content.append(paragraph.text)
        return "\n".join(content)

    def load_html(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            return soup.get_text()

def main():
    root = tk.Tk()
    app = HTMLValidatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()