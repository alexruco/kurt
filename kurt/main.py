import json
from urllib.parse import urlparse
from hellen import fetch_all_links, handle_links, is_internal_link
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

# Example usage
if __name__ == "__main__":
    base_url = 'https://smileup.pt'
    base_url, result_links = process_links(base_url=base_url)
    
    # Print the result
    print(f"Base URL: {base_url}")
    for link_info in result_links:
        print(f"URL: {link_info['url']}, Availability: {link_info['availability']}, Is Internal: {link_info['is_internal']}")
    
    # Example of using is_internal_link (for future use)
    example_link = 'https://smileup.pt/about'
    print(f"Is the link '{example_link}' internal? {is_internal_link(base_url, example_link)}")
