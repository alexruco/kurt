from urllib.parse import urlparse
from kurt.process_links import process_links, is_internal_link
from virginia import check_page_availability
from kurt.external_links_collector import collect_external_links
from kurt.utils import no_content_extensions

def crawl(url, depth, max_depth, crawled, external_links_info):
    """
    Recursively crawl the given URL up to max_depth levels deep and collect external links.

    Parameters:
    url (str): The URL to crawl.
    depth (int): The current depth of the crawl.
    max_depth (int): The maximum depth to crawl.
    crawled (dict): The dictionary to store the crawled data.
    external_links_info (dict): A dictionary to store unique external links and where they were found.

    Returns:
    dict, dict: The updated crawled data dictionary and the dictionary of external links with their sources.
    """
    print(f"Crawling URL: {url} at depth: {depth}")

    # Skip URLs that end with file extensions from no_content_extensions
    parsed_url = urlparse(url)
    if any(parsed_url.path.endswith(f".{ext}") for ext in no_content_extensions()):
        print(f"Skipping non-content URL: {url}")
        return crawled, external_links_info
    
    if depth > max_depth:
        print(f"Reached max depth at URL: {url}")
        return crawled, external_links_info
    
    if url in crawled:
        # If already crawled, just update the "found_in" list and return
        print(f"Updating 'found_in' for already crawled URL: {url}")
        crawled[url]["found_in"].append(url)
        return crawled, external_links_info
    
    # Process the links on this URL
    base_url, result_links = process_links(url)
    print(f"Processed {len(result_links)} links from {url}")

    if not result_links or result_links == "ERROR: base url unavailable":
        return crawled, external_links_info

    # Mark this URL as crawled
    crawled[url] = {
        "availability": check_page_availability(url),
        "is_internal": is_internal_link(base_url, url),
        "found_in": [url],
        "depth": depth
    }

    # Collect external links and their sources
    collect_external_links(base_url, result_links, external_links_info)
    
    for link_info in result_links:
        link = link_info['url']
        is_internal = link_info['is_internal']

        if is_internal:
            if link not in crawled:
                print(f"Recursively crawling internal link: {link}")
                crawl(link, depth + 1, max_depth, crawled, external_links_info)
            else:
                print(f"Updating 'found_in' for already crawled URL: {link}")
                crawled[link]["found_in"].append(url)  # Update "found_in" with current URL
        else:
            print(f"Skipping external link: {link} (not crawled)")

    return crawled, external_links_info
