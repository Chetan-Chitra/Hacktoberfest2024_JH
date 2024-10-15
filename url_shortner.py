import hashlib

# Dictionary to store the shortened URLs
url_mapping = {}

def shorten_url(original_url):
    # Generate a unique hash for the given URL
    short_hash = hashlib.md5(original_url.encode()).hexdigest()[:6]  # Taking only first 6 characters
    short_url = f"http://short.url/{short_hash}"
    
    # Store the mapping of the short URL and original URL
    url_mapping[short_url] = original_url
    return short_url

def retrieve_url(short_url):
    # Retrieve the original URL based on the shortened one
    return url_mapping.get(short_url, "URL not found")

# Example usage:
if __name__ == "__main__":
    original_url = input("Enter the original URL: ")
    short_url = shorten_url(original_url)
    print(f"Shortened URL: {short_url}")

    # Retrieve the original URL from the shortened version
    retrieved_url = retrieve_url(short_url)
    print(f"Original URL from shortened one: {retrieved_url}")
