from crawler import crawl

def crawl_website(base_url, max_depth):
    """
    Crawl the website starting from base_url up to max_depth levels deep.
    
    Parameters:
    base_url (str): The base URL to start crawling from.
    max_depth (int): The maximum depth to crawl.
    
    Returns:
    dict, list: A dictionary where each link is a key with its properties and crawl depth, and a list of external links.
    """
    crawled = {}
    external_links = []
    crawled, external_links = crawl(base_url, 1, max_depth, crawled, external_links)
    return crawled, external_links

# Example usage
if __name__ == "__main__":
    base_url = 'https://mysitefaster.com'
    max_depth = 2
    crawled_data, external_links = crawl_website(base_url, max_depth)
    
    # Print the crawled data
    for link, info in crawled_data.items():
        print(f"Link: {link}")
        print(f"  Internal Links Discovered: {info['found_in']}")
        print(f"  Depth: {info['depth']}")
    
    # Print external links
    print("\nExternal Links Found:")
    for link in external_links:
        print(link)
