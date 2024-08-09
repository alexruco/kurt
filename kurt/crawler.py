from kurt.process_links import process_links, is_internal_link
from virginia import check_page_availability
from external_links_collector import collect_external_links


def crawl(url, depth, max_depth, crawled, external_links):
    """
    Recursively crawl the given URL up to max_depth levels deep and collect external links.

    Parameters:
    url (str): The URL to crawl.
    depth (int): The current depth of the crawl.
    max_depth (int): The maximum depth to crawl.
    crawled (dict): The dictionary to store the crawled data.
    external_links (list): The list to store external links.

    Returns:
    dict, list: The updated crawled data dictionary and the list of external links.
    """
    print(f"Crawling URL: {url} at depth: {depth}")
    
    if depth > max_depth:
        print(f"Reached max depth at URL: {url}")
        return crawled, external_links
    
    if url in crawled:
        print(f"Skipping already crawled URL: {url}")
        return crawled, external_links
    
    base_url, result_links = process_links(url)
    print(f"Processed {len(result_links)} links from {url}")

    if not result_links or result_links == "ERROR: base url unavailable":
        return crawled, external_links

    crawled[url] = {
        "availability": check_page_availability(url),
        "is_internal": is_internal_link(base_url, url),
        "found_in": [base_url],
        "depth": depth
    }

    # Collect external links
    external_links.extend(collect_external_links(base_url, result_links))
    
    for link_info in result_links:
        link = link_info['url']
        
        if link not in crawled:
            print(f"Recursively crawling internal link: {link}")
            crawl(link, depth + 1, max_depth, crawled, external_links)
        else:
            print(f"Skipping link: {link} (already crawled)")

    return crawled, external_links
