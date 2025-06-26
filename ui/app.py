import os
import tkinter as tk
from tkinter import filedialog, messagebox
from core.converter import csv_to_xml

class CsvToXmlUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Konversi CSV/XLSX ke XML")
        self.geometry("500x180")
        self.resizable(False, False)
        self.init_ui()

    def init_ui(self):
        # Input file
        tk.Label(self, text='File CSV/XLSX:').grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.file_input = tk.Entry(self, width=40)
        self.file_input.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self, text='Pilih...', command=self.browse_file).grid(row=0, column=2, padx=5, pady=5)

        # Variable set name
        tk.Label(self, text='Nama Variable Set:').grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.name_input = tk.Entry(self, width=40)
        self.name_input.grid(row=1, column=1, padx=5, pady=5)

        # Output file
        tk.Label(self, text='File XML Output:').grid(row=2, column=0, sticky='e', padx=5, pady=5)
        self.output_input = tk.Entry(self, width=40)
        self.output_input.grid(row=2, column=1, padx=5, pady=5)
        tk.Button(self, text='Pilih...', command=self.browse_output).grid(row=2, column=2, padx=5, pady=5)

        # Convert button
        self.convert_btn = tk.Button(self, text='Konversi', command=self.run_conversion)
        self.convert_btn.grid(row=3, column=1, pady=10)

        # Status label
        self.status_label = tk.Label(self, text='', fg='blue')
        self.status_label.grid(row=4, column=0, columnspan=3, pady=5)

    def browse_file(self):
        filename = filedialog.askopenfilename(
            title='Pilih File CSV/XLSX',
            filetypes=[('CSV/XLSX Files', '*.csv *.xlsx *.xls')]
        )
        if filename:
            self.file_input.delete(0, tk.END)
            self.file_input.insert(0, filename)
            base = os.path.splitext(os.path.basename(filename))[0]
            self.name_input.delete(0, tk.END)
            self.name_input.insert(0, base)

    def browse_output(self):
        filename = filedialog.asksaveasfilename(
            title='Simpan File XML',
            defaultextension='.xml',
            filetypes=[('XML Files', '*.xml')]
        )
        if filename:
            self.output_input.delete(0, tk.END)
            self.output_input.insert(0, filename)

    def run_conversion(self):
        csv_path = self.file_input.get().strip()
        var_set_name = self.name_input.get().strip()
        output_path = self.output_input.get().strip()
        self.status_label.config(text='')

        if not csv_path or not var_set_name:
            messagebox.showerror('Error', 'File CSV/XLSX dan nama variable set wajib diisi.')
            return

        if not output_path:
            input_dir = os.path.dirname(csv_path) or '.'
            output_path = os.path.join(input_dir, f"{var_set_name}.xml")
            self.output_input.delete(0, tk.END)
            self.output_input.insert(0, output_path)

        # Alert if output file exists
        if os.path.exists(output_path):
            if not messagebox.askyesno('Konfirmasi Overwrite', f'File output "{output_path}" sudah ada. Apakah Anda ingin menimpanya?'):
                self.status_label.config(text='Konversi dibatalkan. File output sudah ada.', fg='red')
                return

        self.convert_btn.config(state=tk.DISABLED)
        self.update_idletasks()
        result = csv_to_xml(csv_path, output_path, var_set_name)
        self.convert_btn.config(state=tk.NORMAL)

        if result:
            self.status_label.config(text=f'Berhasil: File XML dibuat di {result}', fg='blue')
            messagebox.showinfo('Berhasil', f'File XML berhasil dibuat: {result}')
        else:
            self.status_label.config(text='Gagal membuat file XML.', fg='red')
            messagebox.showerror('Error', 'Gagal membuat file XML.')

def launch_gui():
    app = CsvToXmlUI()
    app.mainloop()

if __name__ == "__main__":
    launch_gui()