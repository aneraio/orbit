import json
import os

# Define the data structure for the Beachhead Market Selection Worksheet
beachhead_market_selection = {
    "worksheet": [
        {"criteria": "Economically Attractive", "market_segment_1": "", "market_segment_2": "", "market_segment_3": "", "market_segment_4": ""},
        {"criteria": "Accessible to Our Sales Force", "market_segment_1": "", "market_segment_2": "", "market_segment_3": "", "market_segment_4": ""},
        {"criteria": "Strong Value Proposition", "market_segment_1": "", "market_segment_2": "", "market_segment_3": "", "market_segment_4": ""},
        {"criteria": "Complete Product", "market_segment_1": "", "market_segment_2": "", "market_segment_3": "", "market_segment_4": ""},
        {"criteria": "Competition", "market_segment_1": "", "market_segment_2": "", "market_segment_3": "", "market_segment_4": ""},
        {"criteria": "Strategic Value", "market_segment_1": "", "market_segment_2": "", "market_segment_3": "", "market_segment_4": ""},
        {"criteria": "Personal Alignment", "market_segment_1": "", "market_segment_2": "", "market_segment_3": "", "market_segment_4": ""},
        {"criteria": "Overall Rating", "market_segment_1": "", "market_segment_2": "", "market_segment_3": "", "market_segment_4": ""},
        {"criteria": "Ranking", "market_segment_1": "", "market_segment_2": "", "market_segment_3": "", "market_segment_4": ""},
        {"criteria": "Key Deciding Factors", "market_segment_1": "", "market_segment_2": "", "market_segment_3": "", "market_segment_4": ""}
    ]
}

# Specify the file path where you want to save the JSON file
# This example saves it in a 'tools' subdirectory relative to the script
script_dir = os.path.dirname(os.path.abspath(__file__))
tools_dir = os.path.join(script_dir, 'tools')
json_file_path = os.path.join(tools_dir, 'beachhead_market_selection.json')

# Ensure the 'tools' subdirectory exists
if not os.path.exists(tools_dir):
    os.makedirs(tools_dir)

# Write the data to the JSON file
with open(json_file_path, 'w', encoding='utf-8') as f:
    json.dump(beachhead_market_selection, f, ensure_ascii=False, indent=4)

print(f'Beachhead Market Selection Worksheet saved to {json_file_path}')
