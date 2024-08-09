
# kurt/utils.py

def no_content_extensions():
    """
    Returns a list of file extensions that typically represent non-HTML content.
    """
    return [
        'jpg', 'jpeg', 'png', 'gif', 'webp', 'bmp', 'svg',
        'mp4', 'mov', 'avi', 'mkv', 'flv', 'wmv',
        'mp3', 'wav', 'ogg', 'flac', 'aac',
        'pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',
        'zip', 'rar', '7z', 'tar', 'gz',
        'exe', 'msi', 'dmg',
        'iso', 'img',
        'txt', 'csv', 'json', 'xml'
    ]
