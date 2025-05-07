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
