#import json
from kurt.process_links import process_links, is_internal_link
#from dourado import pages_from_sitemaps, consolidate_sitemaps
from crawler import crawl
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
    crawled = {}
    return crawl(base_url, 1, max_depth, crawled)


# Example usage
if __name__ == "__main__":
    base_url = 'https://mysitefaster.com'
    max_depth = 2
    crawled_data = sitemap_crawl(base_url, max_depth)
    
    # Print the crawled data
    for link, info in crawled_data.items():
        print(f"Link: {link}")
        print(f"  Internal Links Discovered: {info['internal_link_discovered']}")
        print(f"  Sitemap Discovered: {info['sitemap_discovered']}")
        print(f"  Depth: {info['depth']}")
