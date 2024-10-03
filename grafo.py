import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import csv
class Automata:
    def __init__(self):
        self.state = 'q0'
        self.errors = []

    def transition(self, input_char):
        previous_state = self.state
        if self.state == 'q0':
            if input_char == '<':
                self.state = 'q1'
            else:
                self.errors.append((previous_state, input_char))
                self.error()
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
                self.error()

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
                self.error()

        elif self.state == 'q_ht':
            if input_char == 'm':
                self.state = 'q_hm'
            else:
                self.error()

        elif self.state == 'q_hm':
            if input_char == 'l':
                self.state = 'q_hl'
            else:
                self.error()

        elif self.state == 'q_hl':
            if input_char == '>':
                self.state = 'q_html_close'
            else:
                self.error()

        # States for <hr>
        elif self.state == 'q_hr':
            if input_char == '>':
                self.state = 'q_hr_close'
            else:
                self.error()

        # States for <head> and <header>
        elif self.state == 'q_he':
            if input_char == 'a':
                self.state = 'q_hea'
            else:
                self.error()

        elif self.state == 'q_hea':
            if input_char == 'd':
                self.state = 'q_hed'
            else:
                self.error()

        elif self.state == 'q_hed':
            if input_char == '>':
                self.state = 'q_head_close'
            elif input_char == 'e':
                self.state = 'q_hee'
            else:
                self.error()

        elif self.state == 'q_hee':
            if input_char == 'r':
                self.state = 'q_her'
            else:
                self.error()

        elif self.state == 'q_her':
            if input_char == '>':
                self.state = 'q_header_close'
            else:
                self.error()
        elif self.state.startswith('q_h_num'):
            if input_char == '>':
                self.state = 'q_hn_close'
            else:
                self.error()
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
                self.error()

        elif self.state == 'q_bo':
            if input_char == 'd':
                self.state = 'q_bod'
            else:
                self.error()

        elif self.state == 'q_bod':
            if input_char == 'y':
                self.state = 'q_body'
            else:
                self.error()

        elif self.state == 'q_body':
            if input_char == '>':
                self.state = 'q_body_close'
            else:
                self.error()

        elif self.state == 'q_br':
            if input_char == '>':
                self.state = 'q_br_close'
            else:
                self.error()

        elif self.state == 'q_ba':
            if input_char == 's':
                self.state = 'q_bas'
            else:
                self.error()

        elif self.state == 'q_bas':
            if input_char == 'e':
                self.state = 'q_bae'
            else:
                self.error()

        elif self.state == 'q_bae':
            if input_char == '>':
                self.state = 'q_base_close'
            else:
                self.error()

        # States for <blockquote>
        elif self.state == 'q_bl':
            if input_char == 'o':
                self.state = 'q_blq'
            else:
                self.error()

        elif self.state == 'q_blq':
            if input_char == 'c':
                self.state = 'q_blc'
            elif input_char == 'u':
                self.state = 'q_blu'
            else:
                self.error()

        elif self.state == 'q_blc':
            if input_char == 'k':
                self.state = 'q_blk'
            else:
                self.error()

        elif self.state == 'q_blk':
            if input_char == 'q':
                self.state = 'q_blq'
            else:
                self.error()

        elif self.state == 'q_blu':
            if input_char == 'o':
                self.state = 'q_blo'
            else:
                self.error()

        elif self.state == 'q_blo':
            if input_char == 't':
                self.state = 'q_blt'
            else:
                self.error()

        elif self.state == 'q_blt':
            if input_char == 'e':
                self.state = 'q_ble'
            else:
                self.error()

        elif self.state == 'q_ble':
            if input_char == '>':
                self.state = 'q_blockquote_close'
            else:
                self.error()

        # States for <meta> and <main>
        elif self.state == 'q_m':
            if input_char == 'e':
                self.state = 'q_me'
            elif input_char == 'a':
                self.state = 'q_ma'
            else:
                self.error()

        elif self.state == 'q_me':
            if input_char == 't':
                self.state = 'q_met'
            else:
                self.error()

        elif self.state == 'q_met':
            if input_char == 'a':
                self.state = 'q_meta'
            else:
                self.error()

        elif self.state == 'q_meta':
            if input_char == '>':
                self.state = 'q_meta_close'
            else:
                self.error()

        elif self.state == 'q_ma':
            if input_char == 'i':
                self.state = 'q_mai'
            else:
                self.error()

        elif self.state == 'q_mai':
            if input_char == 'n':
                self.state = 'q_man'
            else:
                self.error()

        elif self.state == 'q_man':
            if input_char == '>':
                self.state = 'q_main_close'
            else:
                self.error()

        # States for <style>, <script>, <section>
        elif self.state == 'q_s':
            if input_char == 't':
                self.state = 'q_st'
            elif input_char == 'c':
                self.state = 'q_sc'
            elif input_char == 'e':
                self.state = 'q_se'
            else:
                self.error()

        elif self.state == 'q_st':
            if input_char == 'y':
                self.state = 'q_sty'
            else:
                self.error()

        elif self.state == 'q_sty':
            if input_char == 'l':
                self.state = 'q_stl'
            else:
                self.error()

        elif self.state == 'q_stl':
            if input_char == 'e':
                self.state = 'q_style'
            else:
                self.error()

        elif self.state == 'q_style':
            if input_char == '>':
                self.state = 'q_style_close'
            else:
                self.error()

        elif self.state == 'q_sc':
            if input_char == 'r':
                self.state = 'q_scr'
            else:
                self.error()

        elif self.state == 'q_scr':
            if input_char == 'i':
                self.state = 'q_sci'
            else:
                self.error()

        elif self.state == 'q_sci':
            if input_char == 'p':
                self.state = 'q_scp'
            else:
                self.error()

        elif self.state == 'q_scp':
            if input_char == 't':
                self.state = 'q_sct'
            else:
                self.error()

        elif self.state == 'q_sct':
            if input_char == '>':
                self.state = 'q_script_close'
            else:
                self.error()

        elif self.state == 'q_se':
            if input_char == 'c':
                self.state = 'q_sec'
            else:
                self.error()

        elif self.state == 'q_sec':
            if input_char == 't':
                self.state = 'q_set'
            else:
                self.error()

        elif self.state == 'q_set':
            if input_char == 'i':
                self.state = 'q_sei'
            else:
                self.error()

        elif self.state == 'q_sei':
            if input_char == 'o':
                self.state = 'q_seo'
            else:
                self.error()

        elif self.state == 'q_seo':
            if input_char == 'n':
                self.state = 'q_sen'
            else:
                self.error()

        elif self.state == 'q_sen':
            if input_char == '>':
                self.state = 'q_section_close'
            else:
                self.error()

        # States for <article>, <aside>
        elif self.state == 'q_a':
            if input_char == 'r':
                self.state = 'q_ar'
            elif input_char == 's':
                self.state = 'q_as'
            else:
                self.error()

        elif self.state == 'q_ar':
            if input_char == 't':
                self.state = 'q_art'
            else:
                self.error()

        elif self.state == 'q_art':
            if input_char == 'i':
                self.state = 'q_ari'
            else:
                self.error()

        elif self.state == 'q_ari':
            if input_char == 'c':
                self.state = 'q_arc'
            else:
                self.error()

        elif self.state == 'q_arc':
            if input_char == 'l':
                self.state = 'q_arl'
            else:
                self.error()

        elif self.state == 'q_arl':
            if input_char == 'e':
                self.state = 'q_are'
            else:
                self.error()

        elif self.state == 'q_are':
            if input_char == '>':
                self.state = 'q_article_close'
            else:
                self.error()

        elif self.state == 'q_as':
            if input_char == 'i':
                self.state = 'q_asi'
            else:
                self.error()

        elif self.state == 'q_asi':
            if input_char == 'd':
                self.state = 'q_asd'
            else:
                self.error()

        elif self.state == 'q_asd':
            if input_char == 'e':
                self.state = 'q_ase'
            else:
                self.error()

        elif self.state == 'q_ase':
            if input_char == '>':
                self.state = 'q_aside_close'
            else:
                self.error()

        # States for <p>, <pre>
        elif self.state == 'q_p':
            if input_char == 'r':
                self.state = 'q_pr'
            elif input_char == '>':
                self.state = 'q_p_close'
            else:
                self.error()

        elif self.state == 'q_pr':
            if input_char == 'e':
                self.state = 'q_pre'
            else:
                self.error()

        elif self.state == 'q_pre':
            if input_char == '>':
                self.state = 'q_pre_close'
            else:
                self.error()

        # CLOSING STATES
        elif self.state == 'q_html_close':
            if input_char == '<':
                self.state = 'qc_open'
            else:
                self.error()

        elif self.state == 'qc_open':
            if input_char == '/':
                self.state = 'qc_diagonal'
            else:
                self.error()

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
            # Continuing with CLOSING STATES...
        
        # Closing states for HTML tags
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
                self.error()

        elif self.state == 'qc_hm':
            if input_char == 'l':
                self.state = 'qc_hl'
            else:
                self.error()

        elif self.state == 'qc_hl':
            if input_char == '>':
                self.state = 'qc_html_close'
            else:
                self.error()

        elif self.state == 'qc_hr':
            if input_char == '>':
                self.state = 'qc_hr_close'
            else:
                self.error()

        elif self.state == 'qc_he':
            if input_char == 'a':
                self.state = 'qc_hea'
            else:
                self.error()

        elif self.state == 'qc_hea':
            if input_char == 'd':
                self.state = 'qc_hed'
            else:
                self.error()

        elif self.state == 'qc_hed':
            if input_char == '>':
                self.state = 'qc_head_close'
            elif input_char == 'e':
                self.state = 'qc_hee'
            else:
                self.error()

        elif self.state == 'qc_hee':
            if input_char == 'r':
                self.state = 'qc_her'
            else:
                self.error()

        elif self.state == 'qc_her':
            if input_char == '>':
                self.state = 'qc_header_close'
            else:
                self.error()

        # Closing states for h1-h6
        elif self.state.startswith('qc_h_num'):
            if input_char == '>':
                self.state = 'qc_hn_close'
            else:
                self.error()

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
                self.error()

        elif self.state == 'qc_bo':
            if input_char == 'd':
                self.state = 'qc_bod'
            else:
                self.error()

        elif self.state == 'qc_bod':
            if input_char == 'y':
                self.state = 'qc_body'
            else:
                self.error()

        elif self.state == 'qc_body':
            if input_char == '>':
                self.state = 'qc_body_close'
            else:
                self.error()

        elif self.state == 'qc_br':
            if input_char == '>':
                self.state = 'qc_br_close'
            else:
                self.error()

        elif self.state == 'qc_ba':
            if input_char == 's':
                self.state = 'qc_bas'
            else:
                self.error()

        elif self.state == 'qc_bas':
            if input_char == 'e':
                self.state = 'qc_bae'
            else:
                self.error()

        elif self.state == 'qc_bae':
            if input_char == '>':
                self.state = 'qc_base_close'
            else:
                self.error()

        # Closing states for blockquote
        elif self.state == 'qc_bl':
            if input_char == 'o':
                self.state = 'qc_blq'
            else:
                self.error()

        elif self.state == 'qc_blq':
            if input_char == 'c':
                self.state = 'qc_blc'
            elif input_char == 'u':
                self.state = 'qc_blu'
            else:
                self.error()

        elif self.state == 'qc_blc':
            if input_char == 'k':
                self.state = 'qc_blk'
            else:
                self.error()

        elif self.state == 'qc_blk':
            if input_char == 'q':
                self.state = 'qc_blq'
            else:
                self.error()

        elif self.state == 'qc_blu':
            if input_char == 'o':
                self.state = 'qc_blo'
            else:
                self.error()

        elif self.state == 'qc_blo':
            if input_char == 't':
                self.state = 'qc_blt'
            else:
                self.error()

        elif self.state == 'qc_blt':
            if input_char == 'e':
                self.state = 'qc_ble'
            else:
                self.error()

        elif self.state == 'qc_ble':
            if input_char == '>':
                self.state = 'qc_blockquote_close'
            else:
                self.error()

        # Closing states for meta and main
        elif self.state == 'qc_m':
            if input_char == 'e':
                self.state = 'qc_me'
            elif input_char == 'a':
                self.state = 'qc_ma'
            else:
                self.error()

        elif self.state == 'qc_me':
            if input_char == 't':
                self.state = 'qc_met'
            else:
                self.error()

        elif self.state == 'qc_met':
            if input_char == 'a':
                self.state = 'qc_meta'
            else:
                self.error()

        elif self.state == 'qc_meta':
            if input_char == '>':
                self.state = 'qc_meta_close'
            else:
                self.error()

        elif self.state == 'qc_ma':
            if input_char == 'i':
                self.state = 'qc_mai'
            else:
                self.error()

        elif self.state == 'qc_mai':
            if input_char == 'n':
                self.state = 'qc_man'
            else:
                self.error()

        elif self.state == 'qc_man':
            if input_char == '>':
                self.state = 'qc_main_close'
            else:
                self.error()

        # Closing states for style, script, section
        elif self.state == 'qc_s':
            if input_char == 't':
                self.state = 'qc_st'
            elif input_char == 'c':
                self.state = 'qc_sc'
            elif input_char == 'e':
                self.state = 'qc_se'
            else:
                self.error()

        elif self.state == 'qc_st':
            if input_char == 'y':
                self.state = 'qc_sty'
            else:
                self.error()

        elif self.state == 'qc_sty':
            if input_char == 'l':
                self.state = 'qc_stl'
            else:
                self.error()

        elif self.state == 'qc_stl':
            if input_char == 'e':
                self.state = 'qc_style'
            else:
                self.error()

        elif self.state == 'qc_style':
            if input_char == '>':
                self.state = 'qc_style_close'
            else:
                self.error()

        elif self.state == 'qc_sc':
            if input_char == 'r':
                self.state = 'qc_scr'
            else:
                self.error()

        elif self.state == 'qc_scr':
            if input_char == 'i':
                self.state = 'qc_sci'
            else:
                self.error()

        elif self.state == 'qc_sci':
            if input_char == 'p':
                self.state = 'qc_scp'
            else:
                self.error()

        elif self.state == 'qc_scp':
            if input_char == 't':
                self.state = 'qc_sct'
            else:
                self.error()

        elif self.state == 'qc_sct':
            if input_char == '>':
                self.state = 'qc_script_close'
            else:
                self.error()

        elif self.state == 'qc_se':
            if input_char == 'c':
                self.state = 'qc_sec'
            else:
                self.error()

        elif self.state == 'qc_sec':
            if input_char == 't':
                self.state = 'qc_set'
            else:
                self.error()

        elif self.state == 'qc_set':
            if input_char == 'i':
                self.state = 'qc_sei'
            else:
                self.error()

        elif self.state == 'qc_sei':
            if input_char == 'o':
                self.state = 'qc_seo'
            else:
                self.error()

        elif self.state == 'qc_seo':
            if input_char == 'n':
                self.state = 'qc_sen'
            else:
                self.error()

        elif self.state == 'qc_sen':
            if input_char == '>':
                self.state = 'qc_section_close'
            else:
                self.error()

        # Closing states for article and aside
        elif self.state == 'qc_a':
            if input_char == 'r':
                self.state = 'qc_ar'
            elif input_char == 's':
                self.state = 'qc_as'
            else:
                self.error()

        elif self.state == 'qc_ar':
            if input_char == 't':
                self.state = 'qc_art'
            else:
                self.error()

        elif self.state == 'qc_art':
            if input_char == 'i':
                self.state = 'qc_ari'
            else:
                self.error()

        elif self.state == 'qc_ari':
            if input_char == 'c':
                self.state = 'qc_arc'
            else:
                self.error()

        elif self.state == 'qc_arc':
            if input_char == 'l':
                self.state = 'qc_arl'
            else:
                self.error()

        elif self.state == 'qc_arl':
            if input_char == 'e':
                self.state = 'qc_are'
            else:
                self.error()

        elif self.state == 'qc_are':
            if input_char == '>':
                self.state = 'qc_article_close'
            else:
                self.error()

        elif self.state == 'qc_as':
            if input_char == 'i':
                self.state = 'qc_asi'
            else:
                self.error()

        elif self.state == 'qc_asi':
            if input_char == 'd':
                self.state = 'qc_asd'
            else:
                self.error()

        elif self.state == 'qc_asd':
            if input_char == 'e':
                self.state = 'qc_ase'
            else:
                self.error()

        elif self.state == 'qc_ase':
            if input_char == '>':
                self.state = 'qc_aside_close'
            else:
                self.error()

        # Closing states for p and pre
        elif self.state == 'qc_p':
            if input_char == 'r':
                self.state = 'qc_pr'
            elif input_char == '>':
                self.state = 'qc_p_close'
            else:
                self.error()

        elif self.state == 'qc_pr':
            if input_char == 'e':
                self.state = 'qc_pre'
            else:
                self.error()

        elif self.state == 'qc_pre':
            if input_char == '>':
                self.state = 'qc_pre_close'
            else:
                self.error()

        else:
            self.error()

    def error(self):
        print(f"Error: invalid transition from state {self.state}")
        self.state = 'q0'
       

class AutomataGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Autómata HTML")

        # Etiqueta de instrucciones
        self.label = tk.Label(root, text="Ingrese su código HTML:")
        self.label.pack(pady=10)

        # Cuadro de texto para ingresar HTML
        self.text_area = scrolledtext.ScrolledText(root, width=60, height=15, wrap=tk.WORD)
        self.text_area.pack(pady=10)

        # Botón para iniciar el autómata
        self.run_button = tk.Button(root, text="Ejecutar Autómata", command=self.run_automata)
        self.run_button.pack(pady=10)

        # Botón para guardar el CSV
        self.save_csv_button = tk.Button(root, text="Guardar Errores en CSV", command=self.save_to_csv, state=tk.DISABLED)
        self.save_csv_button.pack(pady=10)

        # Cuadro de texto para mostrar el resultado
        self.result_area = scrolledtext.ScrolledText(root, width=60, height=5, wrap=tk.WORD, state=tk.DISABLED)
        self.result_area.pack(pady=10)

        # Almacenar errores
        self.automata = Automata()

    def run_automata(self):
        input_html = self.text_area.get("1.0", tk.END).strip()  # Obtener el texto del área
        self.automata = Automata()  # Reiniciar el autómata para cada ejecución

        # Reiniciar el área de resultado
        self.result_area.config(state=tk.NORMAL)
        self.result_area.delete("1.0", tk.END)

        # Ejecutar el autómata con la entrada
        for char in input_html:
            self.automata.transition(char)

        # Mostrar el estado final
        final_state_message = f"Estado final del autómata: {self.automata.state}\n"
        self.result_area.insert(tk.END, final_state_message)

        # Mostrar los errores si hay
        if self.automata.errors:
            self.result_area.insert(tk.END, "Errores detectados:\n")
            for error in self.automata.errors:
                self.result_area.insert(tk.END, f"Error en estado {error[0]} con símbolo '{error[1]}'\n")

        self.result_area.config(state=tk.DISABLED)

        # Activar botón para guardar en CSV si hay errores
        if self.automata.errors:
            self.save_csv_button.config(state=tk.NORMAL)

    def save_to_csv(self):
        # Abrir diálogo para guardar el archivo
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

        if not file_path:
            return  # Cancelado por el usuario

        # Escribir los errores en el archivo CSV
        try:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Estado', 'Símbolo'])

                for error in self.automata.errors:
                    writer.writerow(error)

            messagebox.showinfo("Éxito", "Errores guardados exitosamente en CSV.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {str(e)}")

# Crear la ventana principal
root = tk.Tk()
app = AutomataGUI(root)

# Iniciar el bucle de la aplicación
root.mainloop()
