"""Twitter."""
import re


class Tweet:
    """Tweet class."""

    def __init__(self, user: str, content: str, time: float, retweets: int):
        """Make consrtuctor."""
        self.user = user
        self.content = content
        self.time = time
        self.retweets = retweets


def find_fastest_growing(tweets: list) -> Tweet:
    """Find the fastest growing tweet."""
    dictionary = {}
    for tweet in tweets:
        res = int(tweet.retweets / tweet.time)
        dictionary[tweet] = res
    result = max(dictionary.items(), key=lambda x: x[1])[0]
# max(dictionary, key=dictionary.get) тоже самое
    return result


def sort_by_popularity(tweets: list) -> list:
    """Sort tweets by popularity."""
    retweets_time = {}
    res = []
    for tweet in tweets:
        retweets_time[tweet] = [tweet.retweets, -tweet.time]
    tweets_by_pop = sorted(retweets_time.items(), key=lambda listt: listt[1], reverse=True)
    for twit in tweets_by_pop:
        res.append(twit[0])
    return res


def filter_by_hashtag(tweets: list, hashtag: str) -> list:
    """Filter tweets by hashtag."""
    result = []
    for tweet in tweets:
        if hashtag in tweet.content:
            result.append(tweet)
    return result


def sort_hashtags_by_popularity(tweets: list) -> list:
    """Sort hashtags by popularity."""
    hashtags_pop = {}
    res = []
    for tw in tweets:
        result = re.findall(r'#\w+', tw.content)  # выдает списком найденные
        for has in result:
            if has in hashtags_pop:
                hashtags_pop[has] = hashtags_pop[has] + tw.retweets
            elif has not in hashtags_pop:
                hashtags_pop[has] = tw.retweets
    sort_hash = sorted(hashtags_pop.items(), key=lambda x: (-x[1], x[0]))
    for has in sort_hash:
        res.append(has[0])
    return res


if __name__ == '__main__':
    tweet1 = Tweet("@realDonaldTrump", "Despite the negative press covfefe #bigsmart", 1249, 54303)
    tweet2 = Tweet("@elonmusk", "Technically, alcohol is a solution #bigsmart", 366.4, 166500)
    tweet3 = Tweet("@CIA", "We can neither confirm nor deny that this is our first tweet. #heart", 2192, 284200)
    tweets = [tweet1, tweet2, tweet3]

    print(find_fastest_growing(tweets).user)  # -> "@elonmusk"

    filtered_by_popularity = sort_by_popularity(tweets)
    print(filtered_by_popularity[0].user)  # -> "@CIA"
    print(filtered_by_popularity[1].user)  # -> "@elonmusk"
    print(filtered_by_popularity[2].user)  # -> "@realDonaldTrump"

    filtered_by_hashtag = filter_by_hashtag(tweets, "#bigsmart")
    print(filtered_by_hashtag[0].user)  # -> "@realDonaldTrump"
    print(filtered_by_hashtag[1].user)  # -> "@elonMusk"

    sorted_hashtags = sort_hashtags_by_popularity(tweets)
    print(sorted_hashtags[0])  # -> "#heart"
