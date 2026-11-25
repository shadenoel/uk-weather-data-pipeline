# UK Weather Data Pipeline

## Project Overview
This project aims to build an automated ETL pipeline that extracts weather data for multiple UK cities from a REST API, transforms the data using Python and loads it into a SQLite database daily.

## Project Objectives
- Automating data extraction from a REST API.
- Retaining original source data in JSON format.
- Transforming and loading structured weather data.
- Ensuring data quality and preventing duplicate records.
- Enabling analysis of weather trends across UK cities.

## Technologies Used
- Python - Data extraction and processing
- Open-Meteo API - Weather data source
- Requests - HTTP requests and API integration
- JSON - Raw data storage
- Pandas - Data cleaning and transformation
- SQLite - Structured data storage
- SQL - Data validation and analysis
- pytest - Automated testing
- Git and GitHub - Version control
- GitHub Actions - Pipeline automation and CI/CD

## Pipeline Architecture
The planned pipeline will follow an Extract, Transform, Load (ETL) architecture.

Weather data will be extracted from the Open-Meteo API using Python and stored as raw JSON files. The raw data will then be cleaned and transformed using Pandas before being loaded into a SQLite database.

Data quality checks, logging and error handling will be implemented to improve pipeline reliability. GitHub Actions will be used to automate daily pipeline execution.

## Project Status
This project is currently in the development phase