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

        # States for <h>
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

        # States for <b>
        elif self.state == 'q_b':
            if input_char == 'o':
                self.state = 'q_bo'
            elif input_char == 'r':
                self.state = 'q_br'
            elif input_char == 'a':
                self.state = 'q_ba'
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

        # States for <meta>
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

        # States for <style>
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

        # States for <a>
        elif self.state == 'q_a':
            if input_char == '>':
                self.state = 'q_a_close'
            else:
                self.error()

        # States for <p>
        elif self.state == 'q_p':
            if input_char == '>':
                self.state = 'q_p_close'
            else:
                self.error()

        # States for closing tags </...>
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
            else:
                self.error()

        # States for closing <h> tags
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

        # States for closing <body> tags
        elif self.state == 'qc_b':
            if input_char == 'o':
                self.state = 'qc_bo'
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
                self.state = 'q_html_close'
            else:
                self.error()

        # States for closing <meta>
        elif self.state == 'qc_m':
            if input_char == 'e':
                self.state = 'qc_me'
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

        # States for closing <style>
        elif self.state == 'qc_s':
            if input_char == 't':
                self.state = 'qc_st'
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
                self.state = 'q_html_close'
            else:
                self.error()

        # States for closing <a>
        elif self.state == 'qc_a':
            if input_char == '>':
                self.state = 'q_html_close'
            else:
                self.error()

        # States for closing <p>
        elif self.state == 'qc_p':
            if input_char == '>':
                self.state = 'q_html_close'
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
