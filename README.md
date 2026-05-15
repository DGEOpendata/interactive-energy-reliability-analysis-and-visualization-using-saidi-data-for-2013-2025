markdown
# Interactive Energy Reliability Analysis and Visualization Using SAIDI Data for 2013-2025

## Overview
This project provides an interactive platform for analyzing and visualizing the Annual SAIDI (System Average Interruption Duration Index) data for customers in the Emirate of Abu Dhabi for the years 2013 to 2025. The dataset measures the average outage duration in minutes per customer annually and serves as a key performance indicator for electricity reliability.

The platform allows users to:
- Explore SAIDI data interactively.
- Visualize trends in electricity reliability over time.
- Download processed data for further analysis.
- Gain insights into energy infrastructure performance.

## Requirements
- Python 3.7+
- Pandas
- Matplotlib

## Installation
1. Clone the repository:
   bash
   git clone https://github.com/yourusername/saidi-analysis.git
   cd saidi-analysis
   

2. Install the required Python libraries:
   bash
   pip install pandas matplotlib
   

## Usage
### Load and Explore the Data
1. Place the `SAIDI.csv` dataset file in the project directory.
2. Run the following script to load and explore the data:
   bash
   python analyze_saidi.py
   
3. The script will output basic information about the dataset and generate a line chart showing the SAIDI trends over time. The chart will be saved as `saidi_trend_analysis.png`.

### Customize the Analysis
You can modify the `analyze_saidi.py` script to customize the analysis and visualizations. For example:
- Add new visualizations, such as bar charts or scatter plots.
- Incorporate additional datasets to analyze correlations.
- Customize the appearance of the charts.

### Export Processed Data
The script also includes functionality to export the processed dataset to a new CSV file named `Processed_SAIDI.csv`. You can use this file for further analysis or reporting.

## Contributing
We welcome contributions to this project! If you have suggestions for new features or improvements, feel free to submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
We would like to thank the local electricity distribution companies and regulatory authorities in the Emirate of Abu Dhabi for providing the SAIDI data.

---

This README file provides an overview of the project and instructions for setting it up and using it. If you have any questions or need further assistance, please don't hesitate to reach out to the project maintainers.
