# kurt/__init__.py

"""
Kurt: A Website Crawling and Link Analysis Package
"""

from .crawler import crawl
from .external_links_collector import collect_external_links
from .process_links import process_links, is_internal_link
from .utils import no_content_extensions
from .main import (
    crawl_website,
    internal_links,
    external_links
)

__all__ = [
    'crawl',
    'collect_external_links',
    'process_links',
    'is_internal_link',
    'no_content_extensions',
    'crawl_website',
    'internal_links',
    'external_links'
]
