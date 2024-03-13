import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel
from tkinter.scrolledtext import ScrolledText
import os
import json
import time
from io import StringIO
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def ts_to_gen(ts, pow_val=1.0002, base_ts=1675084800, div_val=3300):
    gen = pow(pow_val, (float(ts) - base_ts) / div_val)
    return f"{gen:.10f}".replace(".", "_")


def parse_markdown_sections(text):
    intro, segments_md, table_md = text.partition('### Market Segments:')[0], \
        text.partition('### Market Segments:')[2].partition('### Market Segmentation Table:')[0], \
        text.partition('### Market Segmentation Table:')[2]
    segments_list = segments_md.strip().split('\n')[1:]  # Clean up segment list
    return intro.strip(), segments_list, table_md.strip()


def markdown_table_to_df(table_md):
    # Extract and clean the table rows
    lines = table_md.split('\n')[2:]  # Skip the header and delimiter
    header = table_md.split('\n')[0]  # Header row
    header_cols = [col.strip() for col in header.split('|') if col]  # Clean column names

    # Convert markdown to DataFrame
    data = []
    for line in lines:
        row_data = [cell.strip() for cell in line.split('|') if cell]  # Clean row cells
        if row_data:  # Ignore empty lines
            data.append(row_data)

    df = pd.DataFrame(data, columns=header_cols)
    return df


def show_table_with_matplotlib(df):
    # Configure popup window
    popup = Toplevel(root)
    popup.title("Table Preview")

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')
    ax.axis('tight')

    table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 1.5)

    canvas = FigureCanvasTkAgg(fig, master=popup)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


def on_preview():
    text = text_input.get("1.0", "end-1c")
    intro, segments, table_md = parse_markdown_sections(text)
    df = markdown_table_to_df(table_md)  # Convert markdown table to dataframe for preview
    show_table_with_matplotlib(df)  # Display table in a popup window


def on_save():
    text = text_input.get("1.0", "end-1c")
    intro, segments, table_md = parse_markdown_sections(text)
    df = markdown_table_to_df(table_md)  # Convert markdown table to dataframe for saving
    subdir = simpledialog.askstring("Input", "Enter directory name for saving:")
    if subdir:
        timestamp = time.time()
        gen_number = ts_to_gen(timestamp)
        filename = f"{gen_number}_project_mar_seg.json"
        table_data = df.to_dict(orient='records')  # Convert dataframe to dictionary for JSON
        save_to_json(intro, segments, table_data, subdir, filename, gen_number)


def save_to_json(intro, segments, table_data, subdir, filename, gen_number):
    if not os.path.exists(subdir):
        os.makedirs(subdir)
    filepath = os.path.join(subdir, filename)
    combined_data = {
        'mit.orbit.gen.ms': gen_number,
        'Introduction': intro,
        'Market Segments': segments,
        'Market Segmentation Table': table_data
    }
    with open(filepath, 'w') as file:
        json.dump(combined_data, file, indent=4)
    messagebox.showinfo("Success", f"Data saved to {filepath}")


# Tkinter GUI setup
root = tk.Tk()
root.title("Table to JSON Converter")
root.geometry("800x600")

text_input = ScrolledText(root, height=20, width=75)
text_input.pack(pady=20)

preview_btn = tk.Button(root, text="Preview Data", command=on_preview)
preview_btn.pack(pady=5)

save_btn = tk.Button(root, text="Save to JSON", command=on_save)
save_btn.pack(pady=5)

root.mainloop()
