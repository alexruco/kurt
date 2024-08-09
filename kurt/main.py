# kurt/main.py

from kurt.crawl_website import crawl_website

def internal_links(base_url, max_depth):
    """
    Crawl the website and filter only internal links.
    
    Parameters:
    base_url (str): The base URL to start crawling from.
    max_depth (int): The maximum depth to crawl.
    
    Returns:
    dict: A dictionary where each internal link is a key with its properties and crawl depth.
    """
    # Perform the full crawl with both internal and external links enabled
    crawled, _ = crawl_website(base_url, max_depth, crawl_internal=True, crawl_external=True)
    
    # Filter out only internal links
    internal_links = {link: info for link, info in crawled.items() if info['is_internal']}
    
    return internal_links

def external_links(base_url, max_depth):
    """
    Crawl the website and filter only external links.
    
    Parameters:
    base_url (str): The base URL to start crawling from.
    max_depth (int): The maximum depth to crawl.
    
    Returns:
    dict: A dictionary where each external link is a key and the internal URLs where they were found.
    """
    # Perform the full crawl with both internal and external links enabled
    _, external_links_info = crawl_website(base_url, max_depth, crawl_internal=True, crawl_external=True)
    
    # Return only the external links information
    return external_links_info

# Example usage
if __name__ == "__main__":
    base_url = 'https://mysitefaster.com'
    max_depth = 2
   
    # Crawl for internal links
    crawl_internal = internal_links(base_url, max_depth)
    
    # Print the crawled internal links data
    if crawl_internal:
        print("\nInternal Links Found:")
        for link, info in crawl_internal.items():
            print(f"Internal Link: {link}")
            print(f"  Found in: {info['found_in']}")
            print(f"  Depth: {info['depth']}")

    # Crawl for external links
    #crawl_external = external_links(base_url, max_depth)
    
    # Print external links and where they were found
    #if crawl_external:
    #    print("\nExternal Links Found:")
    #    for link, found_in in crawl_external.items():
    #        print(f"External Link: {link}")
    #        print(f"  Found in: {', '.join(found_in)}")
