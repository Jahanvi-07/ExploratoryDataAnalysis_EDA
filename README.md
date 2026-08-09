# ExploratoryDataAnalysis_EDA — Books Dataset

## 1. Project Overview

This project performs Exploratory Data Analysis (EDA) on a dataset of 1,000 books collected from the public website Books to Scrape.

The purpose of the analysis is to understand the structure of the dataset, identify patterns and trends, detect potential data issues, perform statistical analysis, and visualize important relationships.

## 2. Objectives

The main objectives of this project are:

* Understand the structure and characteristics of the dataset.
* Identify the variables and their data types.
* Check for missing values and duplicate records.
* Calculate descriptive statistics.
* Analyze book prices and ratings.
* Identify the most expensive and cheapest books.
* Study the relationship between price and rating.
* Detect potential price outliers.
* Create visualizations to identify patterns and trends.
* Draw meaningful conclusions from the analysis.

## 3. Dataset

The dataset contains 1,000 book records and the following variables:

| Column         | Description                     |
| -------------- | ------------------------------- |
| `title`        | Title of the book               |
| `price_gbp`    | Book price in British pounds    |
| `rating`       | Book rating from 1 to 5         |
| `availability` | Availability status of the book |
| `url`          | URL of the book page            |

## 4. Tools and Technologies

* Python
* Pandas
* Matplotlib
* Seaborn

## 5. Analysis Questions

The following questions were considered before performing the analysis:

1. How large is the dataset?
2. What variables are present and what are their data types?
3. Are there any missing values?
4. Are there duplicate records?
5. What is the average, minimum, and maximum book price?
6. Which book ratings occur most frequently?
7. How are book prices distributed?
8. Is there a relationship between book price and rating?
9. Are there any unusual or extreme book prices?
10. What useful insights can be obtained from the dataset?

## 6. Data Quality Analysis

The dataset contains:

* **1,000 records**
* **5 columns**
* **0 missing values**
* **0 duplicate rows**

All 1,000 books have an availability status of "In stock".

The dataset is therefore structurally complete for the variables analyzed.

## 7. Descriptive Statistics

### Price

| Statistic |  Value |
| --------- | -----: |
| Mean      | £35.07 |
| Median    | £35.98 |
| Minimum   | £10.00 |
| Maximum   | £59.99 |

The average book price is £35.07, while the median price is £35.98. Prices range from £10.00 to £59.99.

### Rating

| Rating | Number of Books |
| -----: | --------------: |
|      1 |             226 |
|      2 |             196 |
|      3 |             203 |
|      4 |             179 |
|      5 |             196 |

The 1-star rating is the most frequent, with 226 books, while the 4-star rating is the least frequent, with 179 books.

## 8. Price and Rating Relationship

The correlation between book price and rating is approximately:

**0.0282**

This value is very close to zero, indicating an extremely weak positive linear relationship between price and rating in this dataset.

Therefore, the analysis does not provide evidence that higher-priced books tend to receive higher ratings.

This conclusion applies specifically to the scraped dataset and should not be generalized to the entire book market.

## 9. Outlier Analysis

The Interquartile Range (IQR) method was used to detect potential price outliers.

The analysis identified:

**0 price outliers**

Therefore, no book prices were classified as unusual according to the 1.5 × IQR rule.

## 10. Visualizations

The project generates the following visualizations:

### Price Distribution

`price_distribution.png`

Shows how book prices are distributed across the dataset.

### Rating Distribution

`rating_distribution.png`

Shows the number of books associated with each rating from 1 to 5.

### Price by Rating

`price_by_rating.png`

Compares the distribution of book prices across different ratings.

### Price vs Rating

`price_vs_rating.png`

Shows the relationship between book price and rating using a scatter plot.

## 11. Key Findings

The main findings from the analysis are:

1. The dataset contains 1,000 books with 5 variables.
2. There are no missing values or duplicate records.
3. The average book price is £35.07.
4. The median book price is £35.98.
5. Book prices range from £10.00 to £59.99.
6. The 1-star rating is the most common rating.
7. All books in the dataset are listed as being in stock.
8. No price outliers were detected using the IQR method.
9. The correlation between price and rating is approximately 0.0282.
10. Book price and rating therefore show almost no linear relationship in this dataset.

## 12. Conclusion

The EDA provided an overall understanding of the structure, quality, distribution, and relationships within the books dataset.

The dataset was found to be complete, with no missing values or duplicate records. Book prices varied between £10.00 and £59.99, with an average price of £35.07.

The analysis also showed that price and rating have almost no linear relationship, suggesting that higher prices do not necessarily correspond to higher ratings within this dataset.

The visualizations and statistical analysis helped identify important patterns and validate the quality of the dataset before further analysis.

## 13. Project Structure

```text
ExploratoryDataAnalysis/
│
├── eda.py
├── books_dataset.csv
├── requirements.txt
├── price_distribution.png
├── rating_distribution.png
├── price_by_rating.png
├── price_vs_rating.png
└── README.md
```

## 14. How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the EDA program:

```bash
python eda.py
```

The program performs the analysis and generates the four visualization files.
