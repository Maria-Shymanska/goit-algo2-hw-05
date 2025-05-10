import re
import time
import json
from datasketch import HyperLogLog
from collections import Counter
from tabulate import tabulate
import os

# File path to your log file
LOG_FILE = "/Users/Lenovo/Downloads/lms-stage-access.log"

# Regex pattern to match IP addresses
IP_REGEX = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

def load_ips(filepath):
    ips = []
    
    # Check if the file exists
    if not os.path.exists(filepath):
        print(f"Error: The file '{filepath}' does not exist. Please check the file path.")
        return ips

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                match = IP_REGEX.search(line)
                if match:
                    ips.append(match.group())
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    
    return ips

def exact_count(ips):
    start = time.time()
    counter = Counter(ips)
    unique_count = len(counter)
    elapsed = time.time() - start
    return unique_count, elapsed

def hll_count(ips, p=12):
    hll = HyperLogLog(p)
    start = time.time()
    for ip in ips:
        hll.update(ip.encode("utf-8"))
    estimate = len(hll)
    elapsed = time.time() - start
    return estimate, elapsed

def main():
    print("Loading log file...")
    ips = load_ips(LOG_FILE)
    print(f"Valid IP rows: {len(ips)}")

    if not ips:
        print("No valid IP addresses found. Exiting...")
        return

    # Perform exact count
    exact_result, exact_time = exact_count(ips)
    
    # Perform HyperLogLog count
    hll_result, hll_time = hll_count(ips)

    # Prepare comparison table
    table = [
        ["Unique Elements", exact_result, round(hll_result, 2)],
        ["Execution Time (sec)", round(exact_time, 4), round(hll_time, 4)],
    ]

    # Print comparison results to console
    print("\nComparison Results:")
    print(tabulate(table, headers=["Metric", "Exact Count", "HyperLogLog"], tablefmt="github"))

    # Save results to a text file
    with open("comparison_results.txt", "w", encoding="utf-8") as f:
        f.write("Comparison Results:\n")
        f.write(tabulate(table, headers=["Metric", "Exact Count", "HyperLogLog"], tablefmt="github"))

    # Save results to a JSON file
    results_json = {
        "exact": {
            "unique_elements": exact_result,
            "time_seconds": round(exact_time, 4),
        },
        "hyperloglog": {
            "unique_elements": round(hll_result, 2),
            "time_seconds": round(hll_time, 4),
        }
    }

    with open("comparison_results.json", "w", encoding="utf-8") as f:
        json.dump(results_json, f, indent=4, ensure_ascii=False)

    print("\nResults saved to 'comparison_results.txt' and 'comparison_results.json'.")

if __name__ == "__main__":
    main()




