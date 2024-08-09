from kurt.crawler import crawl

def crawl_website(base_url, max_depth):
    """
    Crawl the website starting from base_url up to max_depth levels deep.
    
    Parameters:
    base_url (str): The base URL to start crawling from.
    max_depth (int): The maximum depth to crawl.
    
    Returns:
    dict, dict: A dictionary where each internal link is a key with its properties and crawl depth, and a dictionary of external links with the internal URLs where they were found.
    """
    crawled = {}
    external_links_info = {}
    crawled, external_links_info = crawl(base_url, 1, max_depth, crawled, external_links_info)
    return crawled, external_links_info

# Example usage
if __name__ == "__main__":
    base_url = 'https://mysitefaster.com'
    max_depth = 2
    crawled_data, external_links_info = crawl_website(base_url, max_depth)
    
    # Print the crawled data
    for link, info in crawled_data.items():
        print(f"Link: {link}")
        print(f"  Internal Links Discovered: {info['found_in']}")
        print(f"  Depth: {info['depth']}")
    
    # Print external links and where they were found
    print("\nExternal Links Found:")
    for link, found_in in external_links_info.items():
        print(f"External Link: {link}")
        print(f"  Found in: {', '.join(found_in)}")
