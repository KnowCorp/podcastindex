from helpers.parser import read_response

import feedparser
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def read(
    url: str = "https://feeds.buzzsprout.com/2040953.rss",
):
    feed = feedparser.parse(url)

    if feed.status == 200:
        logger.info(f"Feed: {feed.feed.title}")
        logger.info(f"Entries: {len(feed.entries)}")

        parsed_map = read_response(map=feed.entries[0])
        available_keys = parsed_map.keys()

        logger.info(parsed_map)
        logger.info("")
        logger.info(available_keys)


if __name__ == "__main__":
    read(url="https://itunes.apple.com/us/rss/toppodcasts/limit=100/explicit=true/xml")


# Buzz URL dict_keys(['itunes_title', 'title', 'title_detail', 'summary', 'summary_detail', 'content', 'authors', 'author', 'links', 'id', 'guidislink', 'published', 'published_parsed', 'podcast_transcript', 'itunes_duration', 'itunes_episodetype', 'itunes_explicit'])
# iTunes dict_keys(['id', 'guidislink', 'link', 'title', 'title_detail', 'summary', 'summary_detail', 'im_name', 'links', 'im_contenttype', 'tags', 'im_artist', 'im_price', 'im_image', 'rights', 'rights_detail', 'im_releasedate', 'content'])
