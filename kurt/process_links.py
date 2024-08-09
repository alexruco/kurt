# kurt/process_links.py
from urllib.parse import urlparse
from hellen import fetch_all_links, handle_links
from virginia import check_page_availability

def process_links(base_url):
    page_links = fetch_all_links(base_url=base_url)
    if page_links == "ERROR: base url unavailable":
        return base_url, page_links
    links = handle_links(base_url=base_url, page_links=page_links)

    # Build list with availability information and internal link status
    result_links = []
    for link in links:
        availability = check_page_availability(link)
        is_internal = is_internal_link(base_url, link)
        result_links.append({"url": link, "availability": availability, "is_internal": is_internal})

    return base_url, result_links

def is_internal_link(base_url, link):
    """
    Determine if a given link is internal to the base URL.

    Parameters:
    base_url (str): The base URL.
    link (str): The link to check.

    Returns:
    bool: True if the link is internal, False otherwise.
    """
    base_domain = urlparse(base_url).netloc
    link_domain = urlparse(link).netloc
    return base_domain == link_domain