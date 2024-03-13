
# Market Segmentation Analysis Module

## Overview
This module is designed to assist in the analysis and visualization of market segmentation data. It allows users to input market segmentation information through a GUI, visualize the data in a table format, and save the segmentation into a structured JSON file for further analysis or record-keeping.

## Features
- Parse market segmentation data from a structured text input.
- Visualize the market segmentation data in a tabular format with text wrapping for improved readability.
- Save the parsed and structured data into a JSON file, including introductory text, market segments, detailed table data, and a concluding note.

## Installation

To use this module, you will need Python installed on your system. This module has been tested with Python 3.8 and above. Additionally, you will need to install the following dependencies:

```bash
pip install pandas matplotlib
```

## Usage

To run the module, navigate to the directory containing the script and execute it with Python:

```bash
python market_seg.py
```

The GUI will prompt you to paste your market segmentation data into the input field. After pasting your data, you can preview the table visualization or save the data to a JSON file.

### Input Format

Your input should follow this structure:

- Start with an introduction, mentioning the purpose of the segmentation.
- Include a section titled `### Market Segments:` listing the market segments.
- Provide a `### Market Segmentation Table:` with the data structured in a markdown table format.
- Conclude with any additional notes or information that should be saved alongside the table data.

### Previewing Data

Click the "Preview Data" button to visualize the market segmentation table. A new window will display the table, adjusting cell widths to accommodate the content and wrapping text as needed.

### Saving Data

Click the "Save to JSON" button to save your market segmentation data. You will be prompted to enter a directory name where the JSON file will be saved. The file will be named with a unique generation number and include all data sections structured as shown in your input.

## Contributing

Contributions to this module are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This module is released under the MIT License. See the LICENSE file for more details.
