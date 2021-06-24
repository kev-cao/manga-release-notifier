import re

class Chapter:
    """Represents the latest chapter of a manga in a soup, or the next chapter if provided a current chapter.
    You can access the title of the manga, the latest chapter title, the chapter number, and the link to the chapter.
    """
    def __init__(self, soup):
        """Uses the soup to get the next chapter."""
        self.soup = soup
        self.__init_manga_title()
        self.__init_chapter_details()

    def __init_manga_title(self):
        """Gets the title of the manga in the soup."""
        try:
            story_info = self.soup.select_one('[class*=-info]')
            self.manga_title = story_info.h1.get_text() 
        except AttributeError as e:
            raise ValueError('Could not retrieve manga title.')

    def __init_chapter_details(self):
        """Gets some starting chapter details."""
        latest_chapter = self.soup.select_one('.chapter-name')
        self.title, self.latest_num, self.link = self.__process_html_chapter(latest_chapter)

    def fetch_chapter_details(self, last_chapter):
        """Gets the details of the next chapter from the soup."""
        # Ngl, this whole part is a bit ugly, but I really only want this to work and don't need more than that.
        try: 
            chapter_list = self.soup.find_all('a', class_='chapter-name')
            last_title, last_num, last_link = self.title, self.latest_num, self.link

            for chapter in chapter_list:
                title, num, link = self.__process_html_chapter(chapter)

                if num <= last_chapter:
                    break
                else:
                    last_title = title
                    last_num = num
                    last_link = link

            self.title = last_title
            self.num = last_num
            self.link = last_link
        except (AttributeError, IndexError) as e:
            print(e)
            raise ValueError('Could not retrieve chapter details.')

    def __process_html_chapter(self, chapter):
        """Extracts the details of a chapter from HTML."""
        chapter_label = chapter['title']
        chapter_link = chapter['href']

        # Get chapter title and number.
        pattern = r'chapter\s*(\d*):*.*'
        match = re.search(pattern, chapter_label, re.IGNORECASE)
        title = match.group(0) if match else ''
        num = int(match.group(1)) if match else -1
        link = chapter_link

        return (title, num, link)

    def __str__(self):
        """Displays Manga title and Chapter title."""
        return f'{self.manga_title} | {self.title} @ {self.link}'
