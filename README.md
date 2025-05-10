# 1. Bloom Filter Password Uniqueness Checker

- Custom `BloomFilter` class with configurable size and number of hash functions.
- Function to check if passwords are unique or already used.
- Handles invalid or empty input values gracefully.
- Includes unit tests using Python's built-in `unittest`.
- Efficient for large datasets with minimal memory usage.

## How It Works

The BloomFilter uses multiple SHA-256 hash variants to map passwords to a bit array.
The password is not stored, but its hashed fingerprints are.
This allows checking for presence without revealing or storing actual passwords.
False positives are possible, but false negatives are not.

## Running Tests

To run unit tests:

python bloom_filter.py test

## 2. IP Address Count Comparison
This project compares the performance of two methods for counting unique IP addresses in a log file: Exact Count using Python's Counter and Approximate Count using the HyperLogLog algorithm from the datasketch library. The goal is to evaluate the accuracy and efficiency of these methods.

Table of Contents
Installation

Usage

Results

Dependencies

Installation
Before running the script, ensure that you have the required libraries installed. You can install them via pip:

pip install datasketch tabulate
Usage
Step 1: Set the Log File Path
In the script, the LOG_FILE variable is set to the path of the log file containing the IP addresses. Update this variable to point to the correct location of your log file.

LOG_FILE = "/path/to/your/lms-stage-access.log"
Step 2: Run the Script
After setting the correct file path, you can run the script:
python ip_count_comparison.py
Step 3: Output
Once the script completes, you will get the following outputs:

Console Output: A comparison of the exact count and the HyperLogLog approximation for unique IP addresses, as well as the execution time for each method.

Text File (comparison_results.txt): The comparison results in a GitHub-style table format.

JSON File (comparison_results.json): The results are also saved in JSON format for easy programmatic access.

Results
The script prints a comparison table with the following metrics:

Unique Elements: The count of unique IP addresses.

Execution Time (sec): The time taken by each method to process the log file.

Example output:

sql
Копіювати
Редагувати
Comparison Results:
| Metric | Exact Count | HyperLogLog |
|----------------------|-------------|-------------|
| Unique Elements | 100000.0 | 99652.0 |
| Execution Time (sec) | 0.45 | 0.1 |
Results are also saved in two formats:

Text file (comparison_results.txt).

JSON file (comparison_results.json).
