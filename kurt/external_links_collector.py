# kurt/external_links_collector.py

from kurt.process_links import is_internal_link

def collect_external_links(base_url, result_links, external_links_info):
    """
    Collect external links and track the internal pages where they are found.

    Parameters:
    base_url (str): The URL of the internal page where the links were found.
    result_links (list): A list of link information dictionaries.
    external_links_info (dict): A dictionary to store unique external links and where they were found.
    """
    for link_info in result_links:
        link = link_info['url']
        if not is_internal_link(base_url, link):
            if link in external_links_info:
                if base_url not in external_links_info[link]:
                    external_links_info[link].append(base_url)
            else:
                external_links_info[link] = [base_url]
