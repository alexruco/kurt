# Kurt 🚀

Welcome to **Kurt**! This project is designed to help you crawl websites and retrieve a comprehensive list of internal and external links, along with page details.

## Features ✨

- **Crawl Internal Links**: Discover and list all internal links within a website, providing insights into the structure and depth of the pages. 🕸️
- **Identify External Links**: Collect all external links found on the website and trace back where they were discovered. 🌐
- **Filter Non-Content Links**: Automatically skip non-HTML content like images and media files, ensuring the crawler focuses on meaningful content. 🎯


## Installation 💻

You can install the package via pip:

```bash
pip install GIT+https://github.com/alexruco/kurt
```
### Usage 📚

```markdown
## Usage 📚

Here's a quick example to get you started:

```python
from kurt import crawl_website, internal_links, external_links

# Crawl a website for both internal and external links
base_url = 'https://example.com'
max_depth = 2

# Crawl and retrieve both internal and external links
crawled_data, external_links_info = crawl_website(base_url, max_depth)

# Print internal links
for link, info in crawled_data.items():
    print(f"Internal Link: {link}")
    print(f"  Found in: {info['found_in']}")
    print(f"  Depth: {info['depth']}")

# Print external links
print("\nExternal Links Found:")
for link, found_in in external_links_info.items():
    print(f"External Link: {link}")
    print(f"  Found in: {', '.join(found_in)}")

```

## Running Tests 🧪

To run the tests, you can use the `unittest` module or `pytest`.

```bash
python -m unittest discover tests
# or
pytest
```

### Contributing 🤝

```markdown
## Contributing 🤝

We welcome contributions from the community! Here’s how you can get involved:

1. **Report Bugs**: If you find a bug, please open an issue [here](https://github.com/yourusername/kurt/issues).
2. **Suggest Features**: We’d love to hear your ideas! Suggest new features by opening an issue.
3. **Submit Pull Requests**: Ready to contribute? Fork the repo, make your changes, and submit a pull request. Please ensure your code follows our coding standards and is well-documented.
4. **Improve Documentation**: Help us improve our documentation. Feel free to make edits or add new content.

### How to Submit a Pull Request

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin my-feature-branch`.
5. Open a pull request on the original repository.

## License 📄

This project is licensed under the MIT License. Feel free to use, modify, and distribute this software in accordance with the terms outlined in the [LICENSE](LICENSE) file.

Named in honor of Marvel Comics character Kurt Wagner, The Knightcrawler, created by Len Wein and Dave Cockrum