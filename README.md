# ebay_data_db

This project implements a relational database system for auction data downloaded from eBay. The project involves designing a relational schema, transforming JSON data into SQLite-compatible load files, and executing queries over the resulting database.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Schema Design](#schema-design)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Deliverables](#project-deliverables)
- [License](#license)

## Overview

The project starts with a large set of semi-structured JSON auction data and ends with a fully functional SQLite database that supports efficient querying. The tasks include:
1. Translating JSON data into a relational schema.
2. Writing a Python data transformation script.
3. Bulk-loading data into a SQLite database.
4. Running SQL queries for insights into the auction data.

The dataset represents a snapshot of auctions as of December 20, 2001.

## Features

- **Relational Schema Design**: Converts JSON data into normalized tables.
- **Python Data Parser**: Transforms JSON data into SQLite-compatible `.dat` files.
- **SQLite Integration**: Efficiently bulk-loads data into tables.
- **Query Execution**: Predefined SQL queries provide insights into the auction data.

## Schema Design

The schema includes:
- **Item**: Information about items being auctioned.
- **User**: Details about users, including bidders and sellers.
- **Seller and Bidder**: Specialized roles derived from the `User` table.
- **Sell**: Links items to their respective sellers and categories.
- **Bids**: Records of user bids on items.

Primary and foreign keys ensure data integrity, and redundant attributes like `NumberOfBids` are maintained for performance.

## Getting Started

### Prerequisites
- Python 3.x
- SQLite 3.x

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ervardaan/ebay_data_db.git
   cd ebay_data_db
   ```

2, Install dependencies (if any)
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. Data Transformation
   Run the parser to transform JSON data into .dat files:

    ```bash
    sh runParser.sh
    ```
    
2. Database Setup
   Create the database schema:
   ```bash
   sqlite3 auctionbase.db < create.sql
   ```

3. Load the data into the database:
   ```bash
   sqlite3 auctionbase.db < load.txt

4. Run Queries
   Execute SQL queries to analyze the data:
   ```bash
   sqlite3 auctionbase.db < query1.sql
   ```
   
### Project Deliverables
- Schema Design: Includes ER diagram and normalized relational schema.
- Python Parser: A script to transform JSON data into .dat files.
- SQL Scripts: Scripts for database creation, data loading, and queries.

####Files in this Repository
- design.pdf: Documentation of the schema design.
- parser.py: Python script for JSON to .dat transformation.
- runParser.sh: Shell script for automated data transformation.
- create.sql: SQL commands for schema creation.
- load.txt: Commands to load data into SQLite.
- queryX.sql: Predefined SQL queries for analysis.

