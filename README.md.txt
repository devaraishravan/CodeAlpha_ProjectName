# Data Redundancy Removal System

## Project Description

This project is designed to identify redundant and false positive data entries, validate incoming data, prevent duplicate records from being stored, and maintain an accurate database.

## Features

* Duplicate Data Detection
* False Positive Detection
* Validation Mechanism
* Unique Data Insertion
* MySQL Database Integration

## Technologies Used

* Python
* MySQL
* MySQL Connector
* RapidFuzz
* VS Code

## Workflow

1. User enters Name, Email, and Phone Number.
2. System checks if Email or Phone already exists.
3. If found, classify as Redundant Data.
4. If the name is highly similar to an existing record, classify as False Positive.
5. If no match is found, classify as Unique Data.
6. Store only unique data in the database.

## Output Categories

* Redundant Data Found
* False Positive Detected
* Unique Data Inserted

## Author

Shravan
