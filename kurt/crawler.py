#kurt/crawler.py

from urllib.parse import urlparse
from kurt.process_links import process_links, is_internal_link
from virginia import check_page_availability
from kurt.external_links_collector import collect_external_links
from kurt.utils import no_content_extensions

def crawl(url, depth, max_depth, crawled, external_links_info, crawl_internal=True, crawl_external=True):
    """
    Recursively crawl the given URL up to max_depth levels deep and collect external links.

    Parameters:
    url (str): The URL to crawl.
    depth (int): The current depth of the crawl.
    max_depth (int): The maximum depth to crawl.
    crawled (dict): The dictionary to store the crawled data.
    external_links_info (dict): A dictionary to store unique external links and where they were found.
    crawl_internal (bool): Whether to crawl internal links.
    crawl_external (bool): Whether to collect external links.

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
        if crawl_internal and url not in crawled[url]["found_in"]:
            crawled[url]["found_in"].append(url)
        return crawled, external_links_info
    
    # Process the links on this URL
    base_url, result_links = process_links(url)
    print(f"Processed {len(result_links)} links from {url}")

    if not result_links or result_links == "ERROR: base url unavailable":
        return crawled, external_links_info

    # Mark this URL as crawled if crawl_internal is True
    if crawl_internal:
        crawled[url] = {
            "availability": check_page_availability(url),
            "is_internal": is_internal_link(base_url, url),
            "found_in": [],  # This will be updated later with the correct referring URLs
            "depth": depth
        }

    # Collect external links and their sources if crawl_external is True
    if crawl_external:
        collect_external_links(base_url, result_links, external_links_info)
    
    for link_info in result_links:
        link = link_info['url']
        is_internal = link_info['is_internal']

        if is_internal:
            if link not in crawled:
                # Recursive crawl for internal links but only if crawl_internal is True
                if crawl_internal:
                    print(f"Recursively crawling internal link: {link}")
                    crawled, external_links_info = crawl(link, depth + 1, max_depth, crawled, external_links_info, crawl_internal, crawl_external)
            else:
                # Update "found_in" only if the link is already in the crawled dictionary
                if crawl_internal and url not in crawled[link]["found_in"]:
                    crawled[link]["found_in"].append(url)
        elif not is_internal and crawl_external:
            # Ensure external links are properly recorded
            if link not in external_links_info:
                external_links_info[link] = []
            if url not in external_links_info[link]:
                external_links_info[link].append(url)

    return crawled, external_links_info

    """
    Recursively crawl the given URL up to max_depth levels deep and collect external links.

    Parameters:
    url (str): The URL to crawl.
    depth (int): The current depth of the crawl.
    max_depth (int): The maximum depth to crawl.
    crawled (dict): The dictionary to store the crawled data.
    external_links_info (dict): A dictionary to store unique external links and where they were found.
    crawl_internal (bool): Whether to crawl internal links.
    crawl_external (bool): Whether to collect external links.

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
        print(f"URL already crawled: {url}")
        return crawled, external_links_info
    
    # Process the links on this URL
    base_url, result_links = process_links(url)
    print(f"Processed {len(result_links)} links from {url}")

    if not result_links or result_links == "ERROR: base url unavailable":
        return crawled, external_links_info

    # Mark this URL as crawled
    if crawl_internal:
        crawled[url] = {
            "availability": check_page_availability(url),
            "is_internal": is_internal_link(base_url, url),
            "found_in": [],  # Initialize with an empty list
            "depth": depth
        }

    # Collect external links and their sources if crawl_external is True
    if crawl_external:
        collect_external_links(base_url, result_links, external_links_info)
    
    for link_info in result_links:
        link = link_info['url']
        is_internal = link_info['is_internal']

        if is_internal and crawl_internal:
            if link not in crawled:
                print(f"Recursively crawling internal link: {link}")
                crawled, external_links_info = crawl(link, depth + 1, max_depth, crawled, external_links_info, crawl_internal, crawl_external)
            
            # Ensure the link is in crawled before updating "found_in"
            if link in crawled and url not in crawled[link]["found_in"]:
                crawled[link]["found_in"].append(url)
        elif not is_internal and crawl_external:
            if link not in external_links_info:
                external_links_info[link] = []
            if url not in external_links_info[link]:
                external_links_info[link].append(url)

    return crawled, external_links_info

    """
    Recursively crawl the given URL up to max_depth levels deep and collect external links.

    Parameters:
    url (str): The URL to crawl.
    depth (int): The current depth of the crawl.
    max_depth (int): The maximum depth to crawl.
    crawled (dict): The dictionary to store the crawled data.
    external_links_info (dict): A dictionary to store unique external links and where they were found.
    crawl_internal (bool): Whether to crawl internal links.
    crawl_external (bool): Whether to collect external links.

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
        print(f"URL already crawled: {url}")
        return crawled, external_links_info
    
    # Process the links on this URL
    base_url, result_links = process_links(url)
    print(f"Processed {len(result_links)} links from {url}")

    if not result_links or result_links == "ERROR: base url unavailable":
        return crawled, external_links_info

    # Mark this URL as crawled
    if crawl_internal:
        crawled[url] = {
            "availability": check_page_availability(url),
            "is_internal": is_internal_link(base_url, url),
            "found_in": [],  # This will be updated later with the correct referring URLs
            "depth": depth
        }

    # Collect external links and their sources if crawl_external is True
    if crawl_external:
        collect_external_links(base_url, result_links, external_links_info)
    
    for link_info in result_links:
        link = link_info['url']
        is_internal = link_info['is_internal']

        if is_internal and crawl_internal:
            if link not in crawled:
                print(f"Recursively crawling internal link: {link}")
                crawled, external_links_info = crawl(link, depth + 1, max_depth, crawled, external_links_info, crawl_internal, crawl_external)
            if url not in crawled[link]["found_in"]:
                crawled[link]["found_in"].append(url)  # Update "found_in" with the correct source URL
        elif not is_internal and crawl_external:
            if link not in external_links_info:
                external_links_info[link] = []
            if url not in external_links_info[link]:
                external_links_info[link].append(url)

    return crawled, external_links_info

    """
    Recursively crawl the given URL up to max_depth levels deep and collect external links.

    Parameters:
    url (str): The URL to crawl.
    depth (int): The current depth of the crawl.
    max_depth (int): The maximum depth to crawl.
    crawled (dict): The dictionary to store the crawled data.
    external_links_info (dict): A dictionary to store unique external links and where they were found.
    crawl_internal (bool): Whether to crawl internal links.
    crawl_external (bool): Whether to collect external links.

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
    if crawl_internal:
        crawled[url] = {
            "availability": check_page_availability(url),
            "is_internal": is_internal_link(base_url, url),
            "found_in": [url],
            "depth": depth
        }

    # Collect external links and their sources if crawl_external is True
    if crawl_external:
        collect_external_links(base_url, result_links, external_links_info)
    
    for link_info in result_links:
        link = link_info['url']
        is_internal = link_info['is_internal']

        if is_internal and crawl_internal:
            if link not in crawled:
                print(f"Recursively crawling internal link: {link}")
                crawl(link, depth + 1, max_depth, crawled, external_links_info, crawl_internal, crawl_external)
            else:
                print(f"Updating 'found_in' for already crawled URL: {link}")
                crawled[link]["found_in"].append(url)  # Update "found_in" with current URL
        elif not is_internal and crawl_external:
            print(f"Skipping external link: {link} (not crawled)")

    return crawled, external_links_info