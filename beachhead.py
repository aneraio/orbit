import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel
import tkinter.scrolledtext as scrolledtext
import os
import json
import time
import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def ts_to_gen(ts, pow_val=1.0002, base_ts=1675084800, div_val=3300):
    gen = pow(pow_val, (ts - base_ts) / div_val)
    return f"{gen:.10f}".replace(".", "_")

def parse_beachhead_sections(text):
    # Attempt to directly locate the table section for parsing
    try:
        # Find start of the table
        table_start_index = text.index("| Criteria |")
        table_text = text[table_start_index:]

        # Extract headers
        headers = table_text.split('\n')[0].split('|')[2:]  # Skip "Criteria" and empty strings due to split
        headers = [header.strip() for header in headers]

        # Extract rows
        rows = table_text.split('\n')[2:]  # Skip header and divider rows
        table_data = []
        for row in rows:
            if '|' in row:  # Check row contains table divider '|'
                columns = [cell.strip().replace('**', '').replace('<br>', '\n') for cell in row.split('|')[1:]]
                table_data.append((columns[0], columns[1:]))  # Separate criteria name from data
    except ValueError as e:
        messagebox.showerror("Parsing Error", "Error locating table data. Please check the format.")
        return "Unknown Title", [], []

    title_search = re.search(r'"(.*?)"', text)
    title = title_search.group(1) if title_search else "Unknown Title"

    return title, headers, table_data

def show_beachhead_with_matplotlib(title, headers, table_data):
    if not table_data:
        messagebox.showinfo("Preview Error", "No data available to preview.")
        return

    popup = Toplevel(root)
    popup.title("Beachhead Preview")

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')
    ax.axis('tight')

    ax.text(0, 1, title, fontsize=12, va='top', ha='left', fontweight='bold')

    cell_text = [[criteria] + data for criteria, data in table_data]

    table = ax.table(cellText=cell_text, colLabels=["Criteria"] + headers, loc='center', cellLoc='left')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)

    canvas = FigureCanvasTkAgg(fig, master=popup)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def on_preview():
    text = text_input.get("1.0", "end-1c")
    title, headers, table_data = parse_beachhead_sections(text)
    if headers and table_data:
        show_beachhead_with_matplotlib(title, headers, table_data)
    else:
        messagebox.showinfo("Info", "No data to preview. Please ensure the input format is correct.")

def on_save():
    text = text_input.get("1.0", "end-1c")
    title, headers, table_data = parse_beachhead_sections(text)
    if not table_data:
        messagebox.showinfo("Info", "No data to save. Please ensure the input format is correct and try again.")
        return

    subdir = simpledialog.askstring("Input", "Enter directory name for saving:")
    if subdir:
        timestamp = time.time()
        gen_number = ts_to_gen(timestamp)
        filename = f"{gen_number}_beachhead_analysis.json"
        criteria_dicts = [{criteria: data} for criteria, data in table_data]
        save_to_json(title, headers, criteria_dicts, subdir, filename, gen_number)

def save_to_json(title, headers, criteria_data, subdir, filename, gen_number):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_subdir_path = os.path.join(script_dir, subdir)
    if not os.path.exists(full_subdir_path):
        os.makedirs(full_subdir_path)
    filepath = os.path.join(full_subdir_path, filename)

    combined_data = {
        'Title': title,
        'Headers': headers,
        'Criteria Data': criteria_data,
        'mit.orbit.gen.bh': gen_number
    }

    with open(filepath, 'w') as file:
        json.dump(combined_data, file, indent=4)

    messagebox.showinfo("Success", "Data saved to " + filepath)

root = tk.Tk()
root.title("Beachhead Market Analysis Tool")
root.geometry("800x600")

label = tk.Label(root, text="Paste Beachhead Worksheet content here:", font=("Arial", 12))
label.pack(pady=(10, 0))

text_input = scrolledtext.ScrolledText(root, height=18, width=75)
text_input.pack(pady=10)

preview_btn = tk.Button(root, text="Preview Data", command=on_preview)
preview_btn.pack(pady=5)

save_btn = tk.Button(root, text="Save to JSON", command=on_save)
save_btn.pack(pady=5)

root.mainloop()
