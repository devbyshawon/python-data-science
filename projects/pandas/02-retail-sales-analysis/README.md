# 02 — Retail Sales Data Analysis

A beginner Pandas project exploring Global Superstore sales by product, category, region, and month from January 2011 through December 2014.

## Project files

```text
02-retail-sales-analysis/
├── README.md
├── retail_sales_analysis.ipynb
└── data/
    └── retail_sales.csv
```

## Dataset

The notebook expects a prepared Global Superstore CSV at `data/retail_sales.csv` with these nine columns:

| Field | Field | Field |
| --- | --- | --- |
| Order ID | Order Date | Product ID |
| Product Name | Category | Quantity |
| Unit Price | Region | Customer ID |

Each row represents an order line. An order can have several lines. The original notebook's saved outputs show 51,290 input rows and 51,281 rows after removing nine exact duplicate rows. The notebook parses slash-separated dates as month/day/year and hyphen-separated dates as day-month-year.

Use the same prepared CSV as the original analysis. Record its source URL, redistribution terms, and the steps used to create it, especially how `Unit Price` was obtained and which currency applies. If redistribution is restricted, provide acquisition and preparation instructions in place of committing the CSV.

## Run the notebook

1. Place the prepared CSV at `data/retail_sales.csv`.
2. From the project folder, install the dependencies and open Jupyter.

   ```bash
   python -m pip install pandas matplotlib seaborn jupyter
   python -m jupyter notebook
   ```

3. Open `retail_sales_analysis.ipynb`, select a Python 3 kernel, and choose **Restart Kernel and Run All Cells**. The original notebook metadata records Python 3.14.0. The reviewed notebook's results still need to be regenerated with the prepared CSV.

## Analysis

- Preview and describe the data. Check column types, missing values, duplicate rows, and date formats.
- Clean a working copy and calculate line revenue as `Quantity × Unit Price`.
- Filter by category, region, and inclusive date range, separately and together.
- Sum revenue by Product ID, category, region, and calendar month. Use the most frequent product name as the label for each ID.
- Rank products by revenue and units sold. Calculate average order value by summing revenue within each order and averaging those order totals.
- Display a monthly revenue line chart and a category revenue bar chart. Additional charts show regional revenue, the two product rankings, category revenue share, and the relationship between units and revenue.

## Results from the original saved run

| Metric | Result |
| --- | ---: |
| Total calculated revenue | 12,641,024.34 |
| Units sold | 178,290 |
| Unique orders | 25,035 |
| Average order value | 504.93 |
| Unique customers | 1,590 |
| Unique product IDs | 10,292 |
| Highest-revenue month | November 2014 (508,954.73) |

Technology led in revenue, Office Supplies sold the most units, and Central led regional revenue. The Canon imageCLASS 2200 Advanced Copier led the product revenue ranking. The Sanford Pencil Sharpener, Easy-Erase led by quantity with 163 units.

## Limitations

Revenue reflects the supplied unit prices and quantities. The preparation and currency of those prices determine how the resulting amounts should be interpreted. The input lacks product cost data, so the analysis cannot establish profit or margins. The date range describes historical sales.
