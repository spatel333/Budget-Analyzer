# Budget Analyzer

## Overview
Use this to track finances & generate charts. Query bank institutions, extract statements, transform data, load charts & analysis.

## Key Methods
* Query API: APIs allow us to access information from URLs in a systemic, structured way. Here we simply login and request access to a person's bank documents (with no login information being stored)

* ETL (Extract, Transform, Load)
"A long-standing data integration process used to combine data from multiple sources into a single, consistent data set..." - IBM (see references)
ETL is a standard way of handling data.
    * Extract:      Pull from database
    * Transform:    Structure the information & prune out noise
    * Load:         Generate charts, graphs, & metrics to help understand the data

## Languages & their use
* Bash

Shell scripts are utilized for:
    * Homebrew Installation (a lightweight package manger)
    * Python3.9 Installation
    * Creating a virtual environment (to isolate packages from global)
    * Installing packages & activating the virtual environment

* Python

Python3.9 is used for everything else
## References
* [IBM ETL](https://www.ibm.com/topics/etl)