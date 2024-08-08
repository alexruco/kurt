from kurt.process_links import process_links, is_internal_link

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
    
    def crawl(url, depth):
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
                crawl(link, depth + 1)
            else:
                print(f"Skipping link: {link} (Internal: {link_info['is_internal']}, Available: {link_info['availability']})")
    
    crawl(base_url, 1)
    return crawled

# Example usage
if __name__ == "__main__":
    base_url = 'https://smileup.pt'
    max_depth = 2
    crawled_data = crawl_website(base_url, max_depth)
    
    # Print the crawled data
    for link, info in crawled_data.items():
        print(f"Link: {link}")
        print(f"  Availability: {info['availability']}")
        print(f"  Is Internal: {info['is_internal']}")
        print(f"  Found in: {info['found_in']}")
        print(f"  Depth: {info['depth']}")
