import hmac
import hashlib
import time
import os

def generate_hmac(key: bytes, message: bytes, algorithm):
    """Generate HMAC using the given hash algorithm"""
    return hmac.new(key, message, algorithm).hexdigest()

def benchmark_mac(algorithm, message_sizes):
    """Measure execution time for different message sizes"""
    key = os.urandom(16)  # Generate a random 16-byte secret key
    results = {}

    for size in message_sizes:
        message = os.urandom(size)  # Generate a random message of given size
        start_time = time.time()  # Start timer
        mac = generate_hmac(key, message, algorithm)
        end_time = time.time()  # End timer
        results[size] = end_time - start_time  # Store execution time

    return results

# Define message sizes in bytes (1KB, 10KB, 100KB, 1MB)
message_sizes = [1024, 10240, 102400, 1048576]

# Measure execution time for SHA-1 and SHA-256
sha1_results = benchmark_mac(hashlib.sha1, message_sizes)
sha256_results = benchmark_mac(hashlib.sha256, message_sizes)

# Print the results
print("Message Size (Bytes) | SHA-128 Time (s) | SHA-256 Time (s)")
print("-------------------------------------------------------")
for size in message_sizes:
    print(f"{size:<20} | {sha1_results[size]:<12.6f} | {sha256_results[size]:<12.6f}")