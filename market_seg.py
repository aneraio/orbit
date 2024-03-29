import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel
import tkinter.scrolledtext as scrolledtext  # Adjusted import for clarity
import os
import json
import time
from io import StringIO
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import textwrap

def ts_to_gen(ts, pow_val=1.0002, base_ts=1675084800, div_val=3300):
    gen = pow(pow_val, (float(ts) - base_ts) / div_val)
    return f"{gen:.10f}".replace(".", "_")


def parse_markdown_sections(text):
    # Initial split by '###' to get preliminary sections
    sections = text.split('###')

    # Handling pre-segment intro text if exists before the first '###'
    pre_segment_intro = sections[0].strip()

    # Variables to hold content of different sections
    intro = ""
    segments_list = []
    table_md = ""
    ending_note = ""

    for section in sections[1:]:
        if ':' in section:
            header, content = section.split(':', 1)
        else:
            header, content = section, ""
        header = header.strip()
        content = content.strip()

        if header == 'Market Segments':
            intro = pre_segment_intro  # Assuming the pre-segment intro is relevant to the introduction
            segments_list = [seg.strip() for seg in content.split('\n') if seg.strip()]
        elif header in ['Market Segmentation Table', 'Market Segmentation Matrix']:
            table_md = content
        elif 'Note' in header:  # Capturing ending notes based on 'Note' in the header
            ending_note += content + '\n\n'

    # Ensure that ending_note does not have trailing new lines
    ending_note = ending_note.strip()

    return intro, segments_list, table_md, ending_note


def markdown_table_to_df(table_md):
    lines = table_md.split('\n')[2:]  # Skip the header and delimiter
    header = table_md.split('\n')[0]  # Header row
    header_cols = [col.strip() for col in header.split('|') if col]  # Clean column names

    data = []
    for line in lines:
        row_data = [cell.strip() for cell in line.split('|') if cell]  # Clean row cells
        if row_data:  # Ignore empty lines
            data.append(row_data)

    df = pd.DataFrame(data, columns=header_cols)
    return df

def show_table_with_matplotlib(df, intro, segments, ending_note):
    popup = Toplevel(root)
    popup.title("Table Preview")

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')
    ax.axis('tight')

    intro_text = intro + '\n\n' + '\n'.join(segments)
    ax.text(0, 1, intro_text, fontsize=10, va='top', ha='left')

    table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='left', colWidths=[0.1] * len(df.columns))
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 2)

    ax.text(0, -0.5, ending_note, fontsize=10, va='top', ha='left', wrap=True)

    canvas = FigureCanvasTkAgg(fig, master=popup)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def on_preview():
    text = text_input.get("1.0", "end-1c")
    intro, segments, table_md, ending_note = parse_markdown_sections(text)
    df = markdown_table_to_df(table_md)
    show_table_with_matplotlib(df, intro, segments, ending_note)

def on_save():
    text = text_input.get("1.0", "end-1c")
    intro, segments, table_md, ending_note = parse_markdown_sections(text)
    df = markdown_table_to_df(table_md)
    subdir = simpledialog.askstring("Input", "Enter directory name for saving:")
    if subdir:
        timestamp = time.time()
        gen_number = ts_to_gen(timestamp)
        filename = f"{gen_number}_project_mar_seg.json"
        table_data = df.to_dict(orient='records')
        save_to_json(intro, segments, table_data, ending_note, subdir, filename, gen_number)



def save_to_json(intro, segments, table_data, ending_note, subdir, filename, gen_number):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Assuming the script is in the root of your project, adjust the path as needed
    # For example, if your script is inside a 'src' folder, use os.path.join(script_dir, '..', subdir)
    full_subdir_path = os.path.join(script_dir, subdir)

    # Check if the subdir exists, if not, create it
    if not os.path.exists(full_subdir_path):
        os.makedirs(full_subdir_path)

    # Combine the subdir path with the filename to get the full path to save the file
    filepath = os.path.join(full_subdir_path, filename)

    combined_data = {
        'mit.orbit.gen.ms': gen_number,
        'Introduction': intro,
        'Market Segments': segments,
        'Market Segmentation Table': table_data,
        'Ending Note': ending_note
    }

    # Save the combined data to the specified JSON file
    with open(filepath, 'w') as file:
        json.dump(combined_data, file, indent=4)

    # Notify the user that the data was saved successfully
    messagebox.showinfo("Success", f"Data saved to {filepath}")


root = tk.Tk()
root.title("Orbit - Market Segmentation Module")
root.geometry("800x600")

# Label instructing the user where to paste the market segmentation output
label = tk.Label(root, text="Paste market segmentation output here:", font=("Arial", 12))
label.pack(pady=(10,0)) # Adjust vertical spacing as needed

# Adjusted the height of the text input to leave space for the label above
text_input = scrolledtext.ScrolledText(root, height=18, width=75)
text_input.pack(pady=10)

preview_btn = tk.Button(root, text="Preview Data", command=on_preview)
preview_btn.pack(pady=5)

save_btn = tk.Button(root, text="Save to JSON", command=on_save)
save_btn.pack(pady=5)

root.mainloop()
