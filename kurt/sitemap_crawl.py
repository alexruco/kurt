from dourado import pages_from_sitemaps

def sitemap_crawl(base_url, max_depth):
    """
    Crawl the website using sitemaps to discover internal links and their sitemaps.

    Parameters:
    base_url (str): The base URL to start crawling from.
    max_depth (int): The maximum depth to crawl.

    Returns:
    dict: A dictionary where each link is a key with its properties, internal links discovered, and sitemaps discovered.
    """
    from crawler import crawl  # Import inside the function to avoid circular dependency
    crawled = {}
    sitemaps = pages_from_sitemaps(base_url)

    for sitemap_url, links in sitemaps:
        if sitemap_url not in crawled:
            crawled[sitemap_url] = {
                "internal_link_discovered": [],
                "sitemap_discovered": sitemap_url,
                "depth": 1  # Initialize depth
            }
        internal_crawled = crawl(sitemap_url, 1, max_depth, crawled)
        if internal_crawled:
            crawled[sitemap_url]["internal_link_discovered"].extend(internal_crawled.keys())

    return crawled
