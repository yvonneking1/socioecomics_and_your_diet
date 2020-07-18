# Project Overview

This project is to explore the correlations (if any) between socioeconomic standings of communities and the availability of plant-based restaurants

## Executive Summary

## How to Reproduce
1. Download Data Files and save into a folder named Data inside your main folder:
> - [IRS Income by zipcode](https://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-2017-zip-code-data-soi)
> - [Vegan Restaurants](https://www.kaggle.com/datafiniti/vegetarian-vegan-restaurants)

## Deliverables

## Project Planning

**Acquisition, Prep, and Initial Exploration**
- Collect all files

- Create a dataframe using pandas for each file
> After each file was collected into the Data folder, I read them into pandas one by one for cleaning and preparation

- Clean and prepare the data to perform aggregations and merge each dataframe together

- Look at shape of data

## Exploration

**Initial Hypotheses**

> The more affluent a community is the more likely they are to have a plant based restaurant.

**Tested Hypotheses**

## Key Findings:

### Technical Skills

# Data Dictionary
### Description of all the features in the dataframe
| Feature                            | Datatype | Description                                                                                                                        |
|------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------|
| STATEFIPS                     | Char  | The State Federal Information Processing code                                                                       |
| STATE                   | Char  | Two-digit State abbreviation code                                                                      |
| ZIPCODE                   | Char  | 5-digit Zip Code                                                                     |
| N1                  | Num  | Number of returns                                                                    |
| A00100                 | Num  | Adjusted gross income                                                                   |
| A02650                 | Num  | Total income amount                                                                 |
| N02650                 | Num  | Number of return with total income                                                                |
| avg_gross_income                 | float64  | Adjusted gross income divided by Number of returns                                                                |
| avg_total_income                 | float64  | Total income amount divided by Number of returns                                                                |


# Data Sources
[Yelp](https://www.yelp.com/dataset/download)

[Kaggle](https://www.kaggle.com/datafiniti/vegetarian-vegan-restaurants)

[IRS](https://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-2017-zip-code-data-soi)