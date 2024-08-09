# kurt/main.py

from kurt.crawler import crawl

def internal_links(base_url, max_depth):
    """
    Crawl the website for internal links only.
    
    Parameters:
    base_url (str): The base URL to start crawling from.
    max_depth (int): The maximum depth to crawl.
    
    Returns:
    dict: A dictionary where each internal link is a key with its properties and crawl depth.
    """
    crawl_internal = True 
    crawl_external = False
    crawled = {}
    external_links_info = {}
    crawled, external_links_info = crawl(base_url, 1, max_depth, crawled, external_links_info, crawl_internal, crawl_external)
    return crawled

def external_links(base_url, max_depth):
    """
    Crawl the website for external links only.
    
    Parameters:
    base_url (str): The base URL to start crawling from.
    max_depth (int): The maximum depth to crawl.
    
    Returns:
    dict: A dictionary where each external link is a key and the internal URLs where they were found.
    """
    crawl_internal = False 
    crawl_external = True
    crawled = {}
    external_links_info = {}
    crawled, external_links_info = crawl(base_url, 1, max_depth, crawled, external_links_info, crawl_internal, crawl_external)
    return external_links_info


# Example usage
if __name__ == "__main__":
    base_url = 'https://mysitefaster.com'
    max_depth = 2
    
    # Crawl for internal links
    crawl_internal = internal_links(base_url, max_depth)
    
    # Crawl for external links
    crawl_external = external_links(base_url, max_depth)
    
    # Print the crawled internal links data
    if crawl_internal:
        for link, info in crawl_internal.items():
            print(f"Link: {link}")
            print(f"  Internal Links Discovered: {info['found_in']}")
            print(f"  Depth: {info['depth']}")
    
    # Print external links and where they were found
    if crawl_external:
        print("\nExternal Links Found:")
        for link, found_in in crawl_external.items():
            print(f"External Link: {link}")
            print(f"  Found in: {', '.join(found_in)}")
