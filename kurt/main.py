from sitemap_crawl import sitemap_crawl

def crawl_website(base_url, max_depth):
    """
    Crawl the website starting from base_url up to max_depth levels deep.
    
    Parameters:
    base_url (str): The base URL to start crawling from.
    max_depth (int): The maximum depth to crawl.
    
    Returns:
    dict: A dictionary where each link is a key with its properties and crawl depth.
    """
    return sitemap_crawl(base_url, max_depth)

# Example usage
if __name__ == "__main__":
    base_url = 'https://mysitefaster.com'
    max_depth = 2
    crawled_data = crawl_website(base_url, max_depth)
    
    for link, info in crawled_data.items():
        print(f"Link: {link}")
        print(f"  Internal Links Discovered: {info['internal_link_discovered']}")
        print(f"  Sitemap Discovered: {info['sitemap_discovered']}")
        print(f"  Depth: {info['depth']}")
