from kurt.process_links import is_internal_link

def collect_external_links(base_url, result_links, external_links_info):
    """
    Collects external links from the given result links and tracks the internal URLs where they were found.

    Parameters:
    base_url (str): The base URL to compare against.
    result_links (list): The list of links to analyze.
    external_links_info (dict): A dictionary to store unique external links and where they were found.

    Returns:
    None
    """
    for link_info in result_links:
        if isinstance(link_info, str):
            link = link_info
        elif isinstance(link_info, dict):
            link = link_info['url']
        else:
            continue  # Skip if link_info is neither a string nor a dictionary
        
        if not is_internal_link(base_url, link):
            if link not in external_links_info:
                external_links_info[link] = []
            if base_url not in external_links_info[link]:
                external_links_info[link].append(base_url)
