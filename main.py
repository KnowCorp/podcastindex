import json
import src

config = src.get_config_from_env()
index = src.init(config)


def save_to_file(filename: str, data: dict) -> None:
    data_json = json.dumps(data, indent=4)

    with open(f"out/{filename}.json", "w") as file:
        file.write(data_json)


def search(search: str) -> None:
    result = index.search(search, clean=True)

    save_to_file(f"search_{search}", result)


def podcasts(feed_id: int = None, feed_url: str = None, itunes_id: int = None) -> None:
    if feed_id:
        name = feed_id
        result = index.podcastByFeedId(feed_id)

    elif feed_url:
        name = feed_url.replace("/", "_").replace(":", "_")
        result = index.podcastByFeedUrl(feed_url)

    elif itunes_id:
        name = itunes_id
        result = index.podcastByItunesId(itunes_id)

    else:
        raise ValueError("Must provide either feed_id, feed_url, or itunes_id")

    save_to_file(f"podcasts_{name}", result)


def episodes(
    id: int = None,
    feed_id: int = None,
    feed_url: str = None,
    itunes_id: int = None,
    since: int = None,
) -> None:
    """
    since: Unix timestamp
        since = -525600     # 1 year
        since = -2628000    # 1 month
        since = -7884000    # 3 months
        since = -15768000   # 6 months
        since = 1577836800  # Jan 1st 2020
    """

    if id:
        name = id
        result = index.episodeById(id)

    elif feed_id:
        name = feed_id
        result = index.episodesByFeedId(feed_id, since=since)

    elif feed_url:
        name = feed_url.replace("/", "_").replace(":", "_")
        result = index.episodesByFeedUrl(feed_url)

    elif itunes_id:
        name = itunes_id
        result = index.episodesByItunesId(itunes_id)

    else:
        raise ValueError("Must provide either feed_id, feed_url, or itunes_id")

    save_to_file(f"episodes_{name}", result)


def recent(max: int = 5, excluding: str = None, before_episode_id: int = None) -> None:
    result = index.recentEpisodes(
        max=max,
        excluding=excluding,
        before_episode_id=before_episode_id,
    )

    name = f"max_{max}" if not excluding else f"max_{max}_excluding_{excluding}"

    save_to_file(f"recent_{name}", result)


if __name__ == "__main__":
    search(search="This American Life")
    # podcasts(feed_id=522613)
    # podcasts(feed_url="http://feed.thisamericanlife.org/talpodcast")
    # podcasts(itunes_id=201671138)
    # episodes(id=1270106072)
    # episodes(feed_id=522613)
    # episodes(feed_id=522613, since=-525600)
    # episodes(feed_url="http://feed.thisamericanlife.org/talpodcast")
    # episodes(itunes_id=201671138)
    # recent(max=5, excluding="trump", before_episode_id=1270106072)
