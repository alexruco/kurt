from kurt.process_links import is_internal_link


def collect_external_links(base_url, result_links):
    """
    Collects external links from the given result links.

    Parameters:
    base_url (str): The base URL to compare against.
    result_links (list): The list of links to analyze.

    Returns:
    list: A list of external links.
    """
    external_links = []
    
    for link_info in result_links:
        if isinstance(link_info, str):
            link = link_info
        elif isinstance(link_info, dict):
            link = link_info['url']
        else:
            continue  # Skip if link_info is neither a string nor a dictionary
        
        if not is_internal_link(base_url, link):
            external_links.append(link)

    return external_links
