from kurt.process_links import process_links, is_internal_link
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
    dict: The updated crawled data dictionary.
    """
    print(f"Crawling URL: {url} at depth: {depth}")
    if depth > max_depth:
        print(f"Reached max depth at URL: {url}")
        return crawled  # Return the current state of the crawled data

    # Expecting process_links to return a list of dictionaries
    base_url, result_links = process_links(url)
    print(f"Processed {len(result_links)} links from {url}")

    if not result_links:  # If no links are found, return the crawled data as-is
        return crawled

    for link_info in result_links:
        # Handle the case where link_info might be a string (URL) instead of a dictionary
        if isinstance(link_info, str):
            link = link_info
            availability = check_page_availability(link)
            is_internal = is_internal_link(base_url, link)
        elif isinstance(link_info, dict):
            link = link_info['url']
            availability = link_info['availability']
            is_internal = link_info['is_internal']
        else:
            continue  # Skip if link_info is neither a string nor a dictionary

        if link not in crawled:
            crawled[link] = {
                "availability": availability,
                "is_internal": is_internal,
                "found_in": [],
                "depth": depth
            }
        crawled[link]["found_in"].append(base_url)
        
        if is_internal and availability:
            print(f"Recursively crawling internal link: {link}")
            crawl(link, depth + 1, max_depth, crawled)
        else:
            print(f"Skipping link: {link} (Internal: {is_internal}, Available: {availability})")

    return crawled
