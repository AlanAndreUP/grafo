import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import csv
class Automata:
    def __init__(self):
        self.state = 'q0'
        self.errors = []

    def transition(self, input_string):
      for input_char in input_string:
        previous_state = self.state
        if self.state == 'q0':
            if input_char != '<':
                continue
            if input_char == '<':
                self.state = 'q1'
                if input_char == ' ':
                    self.state = 'q1'
            else:
                self.errors.append((previous_state, input_char))
                continue
        elif self.state == 'q1':
            if input_char == 'h':
                self.state = 'q_h'
            elif input_char == 'b':
                self.state = 'q_b'
            elif input_char == 'm':
                self.state = 'q_m'
            elif input_char == 's':
                self.state = 'q_s'
            elif input_char == 'a':
                self.state = 'q_a'
            elif input_char == 'p':
                self.state = 'q_p'
            elif input_char == '/':
                self.state = 'qc_open'
            else:
                continue

        # OPENING STATES

        # States for <html>
        elif self.state == 'q_h':
            if input_char == 't':
                self.state = 'q_ht'
            elif input_char == 'r':
                self.state = 'q_hr'
            elif input_char == 'e':
                self.state = 'q_he'
            elif input_char in '123456':
                self.state = f'q_h_num{input_char}'
            else:
                continue

        elif self.state == 'q_ht':
            if input_char == 'm':
                self.state = 'q_hm'
            else:
                continue

        elif self.state == 'q_hm':
            if input_char == 'l':
                self.state = 'q_hl'
            else:
                continue

        elif self.state == 'q_hl':
            if input_char == '>':
                self.state = 'q_html_close'
            else:
                continue

        # States for <hr>
        elif self.state == 'q_hr':
            if input_char == '>':
                self.state = 'q_hr_close'
            else:
                continue

        # States for <head> and <header>
        elif self.state == 'q_he':
            if input_char == 'a':
                self.state = 'q_hea'
            else:
                continue

        elif self.state == 'q_hea':
            if input_char == 'd':
                self.state = 'q_hed'
            else:
                continue

        elif self.state == 'q_hed':
            if input_char == '>':
                self.state = 'q_head_close'
            elif input_char == 'e':
                self.state = 'q_hee'
            else:
                continue

        elif self.state == 'q_hee':
            if input_char == 'r':
                self.state = 'q_her'
            else:
                continue

        elif self.state == 'q_her':
            if input_char == '>':
                self.state = 'q_header_close'
            else:
                continue
        elif self.state.startswith('q_h_num'):
            if input_char == '>':
                self.state = 'q_hn_close'
            else:
                continue
        elif self.state == 'q_b':
            if input_char == 'o':
                self.state = 'q_bo'
            elif input_char == 'r':
                self.state = 'q_br'
            elif input_char == 'a':
                self.state = 'q_ba'
            elif input_char == 'l':
                self.state = 'q_bl'
            else:
                continue

        elif self.state == 'q_bo':
            if input_char == 'd':
                self.state = 'q_bod'
            else:
                continue

        elif self.state == 'q_bod':
            if input_char == 'y':
                self.state = 'q_body'
            else:
                continue

        elif self.state == 'q_body':
            if input_char == '>':
                self.state = 'q_body_close'
                self.finalState()
            else:
                continue

        elif self.state == 'q_br':
            if input_char == '>':
                self.state = 'q_br_close'
            else:
                continue

        elif self.state == 'q_ba':
            if input_char == 's':
                self.state = 'q_bas'
            else:
                continue

        elif self.state == 'q_bas':
            if input_char == 'e':
                self.state = 'q_bae'
            else:
                continue

        elif self.state == 'q_bae':
            if input_char == '>':
                self.state = 'q_base_close'
            else:
                continue

        # States for <blockquote>
        elif self.state == 'q_bl':
            if input_char == 'o':
                self.state = 'q_blq'
            else:
                continue

        elif self.state == 'q_blq':
            if input_char == 'c':
                self.state = 'q_blc'
            elif input_char == 'u':
                self.state = 'q_blu'
            else:
                continue

        elif self.state == 'q_blc':
            if input_char == 'k':
                self.state = 'q_blk'
            else:
                continue

        elif self.state == 'q_blk':
            if input_char == 'q':
                self.state = 'q_blq'
            else:
                continue

        elif self.state == 'q_blu':
            if input_char == 'o':
                self.state = 'q_blo'
            else:
                continue

        elif self.state == 'q_blo':
            if input_char == 't':
                self.state = 'q_blt'
            else:
                continue

        elif self.state == 'q_blt':
            if input_char == 'e':
                self.state = 'q_ble'
            else:
                continue

        elif self.state == 'q_ble':
            if input_char == '>':
                self.state = 'q_blockquote_close'
            else:
                continue

        # States for <meta> and <main>
        elif self.state == 'q_m':
            if input_char == 'e':
                self.state = 'q_me'
            elif input_char == 'a':
                self.state = 'q_ma'
            else:
                continue

        elif self.state == 'q_me':
            if input_char == 't':
                self.state = 'q_met'
            else:
                continue

        elif self.state == 'q_met':
            if input_char == 'a':
                self.state = 'q_meta'
            else:
                continue

        elif self.state == 'q_meta':
            if input_char == '>':
                self.state = 'q_meta_close'
            else:
                continue

        elif self.state == 'q_ma':
            if input_char == 'i':
                self.state = 'q_mai'
            else:
                continue

        elif self.state == 'q_mai':
            if input_char == 'n':
                self.state = 'q_man'
            else:
                continue

        elif self.state == 'q_man':
            if input_char == '>':
                self.state = 'q_main_close'
                self.finalState()
            else:
                continue

        # States for <style>, <script>, <section>
        elif self.state == 'q_s':
            if input_char == 't':
                self.state = 'q_st'
            elif input_char == 'c':
                self.state = 'q_sc'
            elif input_char == 'e':
                self.state = 'q_se'
            else:
                continue

        elif self.state == 'q_st':
            if input_char == 'y':
                self.state = 'q_sty'
            else:
                continue

        elif self.state == 'q_sty':
            if input_char == 'l':
                self.state = 'q_stl'
            else:
                continue

        elif self.state == 'q_stl':
            if input_char == 'e':
                self.state = 'q_style'
            else:
                continue

        elif self.state == 'q_style':
            if input_char == '>':
                self.state = 'q_style_close'
                self.finalState()
            else:
                continue

        elif self.state == 'q_sc':
            if input_char == 'r':
                self.state = 'q_scr'
            else:
                continue

        elif self.state == 'q_scr':
            if input_char == 'i':
                self.state = 'q_sci'
            else:
                continue

        elif self.state == 'q_sci':
            if input_char == 'p':
                self.state = 'q_scp'
            else:
                continue

        elif self.state == 'q_scp':
            if input_char == 't':
                self.state = 'q_sct'
            else:
                continue

        elif self.state == 'q_sct':
            if input_char == '>':
                self.state = 'q_script_close'
                self.finalState()
            else:
                continue

        elif self.state == 'q_se':
            if input_char == 'c':
                self.state = 'q_sec'
            else:
                continue

        elif self.state == 'q_sec':
            if input_char == 't':
                self.state = 'q_set'
            else:
                continue

        elif self.state == 'q_set':
            if input_char == 'i':
                self.state = 'q_sei'
            else:
                continue

        elif self.state == 'q_sei':
            if input_char == 'o':
                self.state = 'q_seo'
            else:
                continue

        elif self.state == 'q_seo':
            if input_char == 'n':
                self.state = 'q_sen'
            else:
                continue

        elif self.state == 'q_sen':
            if input_char == '>':
                self.state = 'q_section_close'
                self.finalState()
            else:
                continue

        # States for <article>, <aside>
        elif self.state == 'q_a':
            if input_char == 'r':
                self.state = 'q_ar'
            elif input_char == 's':
                self.state = 'q_as'
            else:
                continue

        elif self.state == 'q_ar':
            if input_char == 't':
                self.state = 'q_art'
            else:
                continue

        elif self.state == 'q_art':
            if input_char == 'i':
                self.state = 'q_ari'
            else:
                continue

        elif self.state == 'q_ari':
            if input_char == 'c':
                self.state = 'q_arc'
            else:
                continue

        elif self.state == 'q_arc':
            if input_char == 'l':
                self.state = 'q_arl'
            else:
                continue

        elif self.state == 'q_arl':
            if input_char == 'e':
                self.state = 'q_are'
            else:
                continue

        elif self.state == 'q_are':
            if input_char == '>':
                self.state = 'q_article_close'
                self.finalState()
            else:
                continue

        elif self.state == 'q_as':
            if input_char == 'i':
                self.state = 'q_asi'
            else:
                continue

        elif self.state == 'q_asi':
            if input_char == 'd':
                self.state = 'q_asd'
            else:
                continue

        elif self.state == 'q_asd':
            if input_char == 'e':
                self.state = 'q_ase'
            else:
                continue

        elif self.state == 'q_ase':
            if input_char == '>':
                self.state = 'q_aside_close'
                self.finalState()
            else:
                continue

        # States for <p>, <pre>
        elif self.state == 'q_p':
            if input_char == 'r':
                self.state = 'q_pr'
            elif input_char == '>':
                self.state = 'q_p_close'
                self.finalState()
            else:
                continue

        elif self.state == 'q_pr':
            if input_char == 'e':
                self.state = 'q_pre'
            else:
                continue

        elif self.state == 'q_pre':
            if input_char == '>':
                self.state = 'q_pre_close'
            else:
                continue

        # CLOSING STATES
        elif self.state == 'q_html_close':
            if input_char == '<':
                self.state = 'qc_open'
            else:
                continue
        elif self.state == 'q_head_close':
            if input_char == '<':
                self.state = 'qc_open'
            else:
                continue
        elif self.state == 'qc_open':
            if input_char == '/':
                self.state = 'qc_diagonal'
            else:
              continue

        elif self.state == 'qc_diagonal':
            if input_char == 'h':
                self.state = 'qc_h'
            elif input_char == 'b':
                self.state = 'qc_b'
            elif input_char == 'm':
                self.state = 'qc_m'
            elif input_char == 's':
                self.state = 'qc_s'
            elif input_char == 'a':
                self.state = 'qc_a'
            elif input_char == 'p':
                self.state = 'qc_p'
            else :
                continue

        elif self.state == 'qc_h':
            if input_char == 't':
                self.state = 'qc_ht'
            elif input_char == 'r':
                self.state = 'qc_hr'
            elif input_char == 'e':
                self.state = 'qc_he'
            elif input_char in '123456':
                self.state = f'qc_h_num{input_char}'
            else:
                self.error()

        elif self.state == 'qc_ht':
            if input_char == 'm':
                self.state = 'qc_hm'
            else:
                continue

        elif self.state == 'qc_hm':
            if input_char == 'l':
                self.state = 'qc_hl'
            else:
                continue

        elif self.state == 'qc_hl':
            if input_char == '>':
                self.state = 'qc_html_close'
                self.finalState()
            else:
                continue

        elif self.state == 'qc_hr':
            if input_char == '>':
                self.state = 'qc_hr_close'
                self.finalState()
            else:
                continue

        elif self.state == 'qc_he':
            if input_char == 'a':
                self.state = 'qc_hea'
            else:
                continue

        elif self.state == 'qc_hea':
            if input_char == 'd':
                self.state = 'qc_hed'
            else:
                continue

        elif self.state == 'qc_hed':
            if input_char == '>':
                self.state = 'qc_head_close'
                self.finalState()
            elif input_char == 'e':
                self.state = 'qc_hee'
            else:
                continue

        elif self.state == 'qc_hee':
            if input_char == 'r':
                self.state = 'qc_her'
            else:
                continue

        elif self.state == 'qc_her':
            if input_char == '>':
                self.state = 'qc_header_close'
            else:
                continue

        # Closing states for h1-h6
        elif self.state.startswith('qc_h_num'):
            if input_char == '>':
                self.state = 'qc_hn_close'
                self.finalState()
            else:
                continue

        # Closing states for body, br, base, blockquote
        elif self.state == 'qc_b':
            if input_char == 'o':
                self.state = 'qc_bo'
            elif input_char == 'r':
                self.state = 'qc_br'
            elif input_char == 'a':
                self.state = 'qc_ba'
            elif input_char == 'l':
                self.state = 'qc_bl'
            else:
                continue

        elif self.state == 'qc_bo':
            if input_char == 'd':
                self.state = 'qc_bod'
            else:
                continue

        elif self.state == 'qc_bod':
            if input_char == 'y':
                self.state = 'qc_body'
            else:
                continue

        elif self.state == 'qc_body':
            if input_char == '>':
                self.state = 'qc_body_close'
                self.finalState()
            else:
                continue

        elif self.state == 'qc_br':
            if input_char == '>':
                self.state = 'qc_br_close'
                self.finalState()
            else:
                continue

        elif self.state == 'qc_ba':
            if input_char == 's':
                self.state = 'qc_bas'
            else:
                continue

        elif self.state == 'qc_bas':
            if input_char == 'e':
                self.state = 'qc_bae'
            else:
                continue

        elif self.state == 'qc_bae':
            if input_char == '>':
                self.state = 'qc_base_close'
                self.finalState()
            else:
                continue

        # Closing states for blockquote
        elif self.state == 'qc_bl':
            if input_char == 'o':
                self.state = 'qc_blq'
            else:
                continue

        elif self.state == 'qc_blq':
            if input_char == 'c':
                self.state = 'qc_blc'
            elif input_char == 'u':
                self.state = 'qc_blu'
            else:
                continue

        elif self.state == 'qc_blc':
            if input_char == 'k':
                self.state = 'qc_blk'
            else:
                continue

        elif self.state == 'qc_blk':
            if input_char == 'q':
                self.state = 'qc_blq'
            else:
                continue

        elif self.state == 'qc_blu':
            if input_char == 'o':
                self.state = 'qc_blo'
            else:
                continue
            

        elif self.state == 'qc_blo':
            if input_char == 't':
                self.state = 'qc_blt'
            else:
                continue

        elif self.state == 'qc_blt':
            if input_char == 'e':
                self.state = 'qc_ble'
            else:
                continue

        elif self.state == 'qc_ble':
            if input_char == '>':
                self.state = 'qc_blockquote_close'
                self.finalState()
            else:
                continue

        # Closing states for meta and main
        elif self.state == 'qc_m':
            if input_char == 'e':
                self.state = 'qc_me'
            elif input_char == 'a':
                self.state = 'qc_ma'
            else:
                continue

        elif self.state == 'qc_me':
            if input_char == 't':
                self.state = 'qc_met'
            else:
                continue

        elif self.state == 'qc_met':
            if input_char == 'a':
                self.state = 'qc_meta'
            else:
                continue

        elif self.state == 'qc_meta':
            if input_char == '>':
                self.state = 'qc_meta_close'
                self.finalState()
            else:
                continue

        elif self.state == 'qc_ma':
            if input_char == 'i':
                self.state = 'qc_mai'
            else:
                continue

        elif self.state == 'qc_mai':
            if input_char == 'n':
                self.state = 'qc_man'
            else:
                continue

        elif self.state == 'qc_man':
            if input_char == '>':
                self.state = 'qc_main_close'
                self.finalState()
            else:
                continue

        # Closing states for style, script, section
        elif self.state == 'qc_s':
            if input_char == 't':
                self.state = 'qc_st'
            elif input_char == 'c':
                self.state = 'qc_sc'
            elif input_char == 'e':
                self.state = 'qc_se'
            else:
                continue

        elif self.state == 'qc_st':
            if input_char == 'y':
                self.state = 'qc_sty'
            else:
                continue

        elif self.state == 'qc_sty':
            if input_char == 'l':
                self.state = 'qc_stl'
            else:
                continue

        elif self.state == 'qc_stl':
            if input_char == 'e':
                self.state = 'qc_style'
            else:
                continue

        elif self.state == 'qc_style':
            if input_char == '>':
                self.state = 'qc_style_close'
                self.finalState()
            else:
                continue

        elif self.state == 'qc_sc':
            if input_char == 'r':
                self.state = 'qc_scr'
            else:
                continue

        elif self.state == 'qc_scr':
            if input_char == 'i':
                self.state = 'qc_sci'
            else:
                continue

        elif self.state == 'qc_sci':
            if input_char == 'p':
                self.state = 'qc_scp'
            else:
                continue

        elif self.state == 'qc_scp':
            if input_char == 't':
                self.state = 'qc_sct'
            else:
                continue

        elif self.state == 'qc_sct':
            if input_char == '>':
                self.state = 'qc_script_close'
                self.finalState()
            else:
                continue

        elif self.state == 'qc_se':
            if input_char == 'c':
                self.state = 'qc_sec'
            else:
                continue

        elif self.state == 'qc_sec':
            if input_char == 't':
                self.state = 'qc_set'
            else:
                continue

        elif self.state == 'qc_set':
            if input_char == 'i':
                self.state = 'qc_sei'
            else:
                continue

        elif self.state == 'qc_sei':
            if input_char == 'o':
                self.state = 'qc_seo'
            else:
                continue

        elif self.state == 'qc_seo':
            if input_char == 'n':
                self.state = 'qc_sen'
            else:
                continue

        elif self.state == 'qc_sen':
            if input_char == '>':
                self.state = 'qc_section_close'
                self.finalState()
            else:
                continue

        # Closing states for article and aside
        elif self.state == 'qc_a':
            if input_char == 'r':
                self.state = 'qc_ar'
            elif input_char == 's':
                self.state = 'qc_as'
            else:
                continue

        elif self.state == 'qc_ar':
            if input_char == 't':
                self.state = 'qc_art'
            else:
                continue

        elif self.state == 'qc_art':
            if input_char == 'i':
                self.state = 'qc_ari'
            else:
                continue

        elif self.state == 'qc_ari':
            if input_char == 'c':
                self.state = 'qc_arc'
            else:
                continue

        elif self.state == 'qc_arc':
            if input_char == 'l':
                self.state = 'qc_arl'
            else:
                continue

        elif self.state == 'qc_arl':
            if input_char == 'e':
                self.state = 'qc_are'
            else:
                continue

        elif self.state == 'qc_are':
            if input_char == '>':
                self.state = 'qc_article_close'
                self.finalState()
            else:
                continue

        elif self.state == 'qc_as':
            if input_char == 'i':
                self.state = 'qc_asi'
            else:
                continue

        elif self.state == 'qc_asi':
            if input_char == 'd':
                self.state = 'qc_asd'
            else:
                continue

        elif self.state == 'qc_asd':
            if input_char == 'e':
                self.state = 'qc_ase'
            else:
                continue

        elif self.state == 'qc_ase':
            if input_char == '>':
                self.state = 'qc_aside_close'
                self.finalState()
            else:
                continue

        # Closing states for p and pre
        elif self.state == 'qc_p':
            if input_char == 'r':
                self.state = 'qc_pr'
            elif input_char == '>':
                self.state = 'qc_p_close'
                self.finalState()
            else:
                continue

        elif self.state == 'qc_pr':
            if input_char == 'e':
                self.state = 'qc_pre'
            else:
                continue

        elif self.state == 'qc_pre':
            if input_char == '>':
                self.state = 'qc_pre_close'
                self.finalState()
            else:
                continue

        else:
            continue

    def error(self):
        print(f"Error: invalid transition from state {self.state}")
    def finalState(self):
        if(self.state == 'qc_head_close'):
            self.state = 'q0'
        if(self.state == 'q_body_close'):
            self.state = 'q0'
        self.state = self.state 
       

class AutomataGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Autómata HTML")
        self.label = tk.Label(root, text="Ingrese su código HTML:")
        self.label.pack(pady=10)
        self.text_area = scrolledtext.ScrolledText(root, width=60, height=15, wrap=tk.WORD)
        self.text_area.pack(pady=10)
        self.run_button = tk.Button(root, text="Ejecutar Autómata", command=self.run_automata)
        self.run_button.pack(pady=10)
        self.save_csv_button = tk.Button(root, text="Guardar Errores en CSV", command=self.save_to_csv, state=tk.DISABLED)
        self.save_csv_button.pack(pady=10)
        self.result_area = scrolledtext.ScrolledText(root, width=60, height=5, wrap=tk.WORD, state=tk.DISABLED)
        self.result_area.pack(pady=10)
        self.automata = Automata()

    def run_automata(self):
        input_html = self.text_area.get("1.0", tk.END).strip()
        self.automata = Automata()
        self.result_area.config(state=tk.NORMAL)
        self.result_area.delete("1.0", tk.END)
        self.automata.transition(input_html)
        final_state_message = f"Estado final del autómata: {self.automata.state}\n"
        self.result_area.insert(tk.END, final_state_message)
        if self.automata.errors:
            self.result_area.insert(tk.END, "Errores detectados:\n")
            for error in self.automata.errors:
                self.result_area.insert(tk.END, f"Error en estado {error[0]} con símbolo '{error[1]}'\n")

        self.result_area.config(state=tk.DISABLED)
        if self.automata.errors:
            self.save_csv_button.config(state=tk.NORMAL)

    def save_to_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

        if not file_path:
            return 
        try:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Estado', 'Símbolo'])

                for error in self.automata.errors:
                    writer.writerow(error)

            messagebox.showinfo("Éxito", "Errores guardados exitosamente en CSV.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {str(e)}")
root = tk.Tk()
app = AutomataGUI(root)
root.mainloop()
