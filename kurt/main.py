import json
from kurt.process_links import process_links, is_internal_link
from dourado import pages_from_sitemaps, consolidate_sitemaps
from virginia import check_page_availability

def crawl(url, depth, max_depth, crawled):
    """
    Recursively crawl the given URL up to max_depth levels deep.

    Parameters:
    url (str): The URL to crawl.
    depth (int): The current depth of the crawl.
    max_depth (int): The maximum depth to crawl.
    crawled (dict): The dictionary to store the crawled data.

    Returns:
    None
    """
    print(f"Crawling URL: {url} at depth: {depth}")
    if depth > max_depth:
        print(f"Reached max depth at URL: {url}")
        return
    base_url, result_links = process_links(url)
    print(f"Processed {len(result_links)} links from {url}")
    
    for link_info in result_links:
        link = link_info['url']
        if link not in crawled:
            crawled[link] = {
                "availability": link_info['availability'],
                "is_internal": link_info['is_internal'],
                "found_in": [],
                "depth": depth
            }
        crawled[link]["found_in"].append(base_url)
        
        if link_info['is_internal'] and link_info['availability']:
            print(f"Recursively crawling internal link: {link}")
            crawl(link, depth + 1, max_depth, crawled)
        else:
            print(f"Skipping link: {link} (Internal: {link_info['is_internal']}, Available: {link_info['availability']})")

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
    crawl(base_url, 1, max_depth, crawled)
    return crawled

def sitemap_crawl(base_url, max_depth):
    """
    Crawl the website using sitemaps to discover internal links and their sitemaps.

    Parameters:
    base_url (str): The base URL to start crawling from.
    max_depth (int): The maximum depth to crawl.

    Returns:
    dict: A dictionary where each link is a key with its properties, internal links discovered, and sitemaps discovered.
    """
    crawled = {}
    sitemaps = pages_from_sitemaps(base_url)
    
    for sitemap_url, links in sitemaps:
        if sitemap_url not in crawled:
            crawled[sitemap_url] = {
                "internal_link_discovered": [],
                "sitemap_discovered": sitemap_url,
                "depth": 0  # Initialize depth
            }
        internal_crawled = crawl(sitemap_url, 1, max_depth, {})
        crawled[sitemap_url]["internal_link_discovered"].extend(internal_crawled.keys())
        crawled[sitemap_url]["depth"] = 1  # Set depth after crawling

    return crawled

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
