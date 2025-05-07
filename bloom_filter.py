import hashlib
import logging
import unittest

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class BloomFilter:
    def __init__(self, size: int, num_hashes: int):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0] * size
        logging.info(f"BloomFilter created: size={size}, num_hashes={num_hashes}")

    def _hashes(self, item: str):
        for i in range(self.num_hashes):
            hash_input = f"{item}_{i}".encode("utf-8")
            digest = hashlib.sha256(hash_input).hexdigest()
            yield int(digest, 16) % self.size

    def add(self, item: str):
        if not isinstance(item, str) or not item:
            logging.warning(f"Attempted to add an invalid item: {item}")
            return
        for index in self._hashes(item):
            self.bit_array[index] = 1

    def __contains__(self, item: str) -> bool:
        if not isinstance(item, str) or not item:
            return False
        return all(self.bit_array[index] for index in self._hashes(item))


def check_password_uniqueness(bloom_filter: BloomFilter, passwords: list[str]) -> dict[str, str]:
    results = {}
    for password in passwords:
        if not isinstance(password, str) or not password:
            results[password] = "invalid"
            logging.warning(f"Invalid password: {password}")
            continue
        if password in bloom_filter:
            results[password] = "already used"
            logging.info(f"Duplicate password: {password}")
        else:
            results[password] = "unique"
            bloom_filter.add(password)
            logging.info(f"New unique password: {password}")
    return results


# Example Usage

def example_usage():
    print("\n=== Example Usage ===")
    bloom = BloomFilter(size=1000, num_hashes=3)

    existing_passwords = ["password123", "admin123", "qwerty123"]
    for password in existing_passwords:
        bloom.add(password)

    new_passwords = ["password123", "newpassword", "admin123", "guest"]
    results = check_password_uniqueness(bloom, new_passwords)

    for password, status in results.items():
        print(f"Password '{password}' — {status}.")


#   Unit Tests 
class TestBloomFilter(unittest.TestCase):
    def setUp(self):
        self.bloom = BloomFilter(size=1000, num_hashes=3)
        self.bloom.add("test123")

    def test_existing_password(self):
        self.assertIn("test123", self.bloom)

    def test_new_password(self):
        self.assertNotIn("new456", self.bloom)

    def test_password_check_function(self):
        passwords = ["test123", "new456", "", None]
        result = check_password_uniqueness(self.bloom, passwords)
        expected = {
            "test123": "already used",
            "new456": "unique",
            "": "invalid",
            None: "invalid"
        }
        self.assertEqual(result, expected)


if __name__ == "__main__":
    import sys

    if "test" in sys.argv:
        unittest.main(argv=["first-arg-is-ignored"])
    else:
        example_usage()



