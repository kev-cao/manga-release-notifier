import re

class Chapter:
    """Represents the latest chapter of a manga in a soup.
    You can access the title of the manga, the latest chapter title, and the chapter number.
    """
    def __init__(self, soup):
        """Uses the soup to get the latest chapter."""
        self.soup = soup
        self.__init_manga_title()
        self.__init_chapter_details()

    def __init_manga_title(self):
        """Gets the title of the manga in the soup."""
        try:
            story_info = self.soup.select_one('.panel-story-info')
            self.manga_title = story_info.h1.get_text() 
        except AttributeError as e:
            raise ValueError('Could not retrieve manga title.')

    def __init_chapter_details(self):
        """Gets the details of the latest chapter from the soup."""
        try: 
            chapter_list = self.soup.select_one('.panel-story-chapter-list')
            recent_chapter = chapter_list.find('li', class_='a-h')
            chapter_label = recent_chapter.a['title']

            # Get chapter title and number.
            pattern = r'chapter\s*(\d*):*.*'
            match = re.search(pattern, chapter_label, re.IGNORECASE)
            self.title = match.group(0) if match else ''
            self.num = int(match.group(1)) if match else -1
        except (AttributeError, IndexError) as e:
            raise ValueError('Could not retrieve chapter details.')

    def __str__(self):
        """Displays Manga title and Chapter title."""
        return f'{self.manga_title} | {self.title}'
