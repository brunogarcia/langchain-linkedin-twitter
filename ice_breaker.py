from third_parties import linkedin, twitter
from agents import linkedin_agent, twitter_agent


def ice_break(name: str):
    linkedin_profile_url = linkedin_agent.lookup(name=name)
    linkedin_data = linkedin.scrape_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url
    )

    twitter_username = twitter_agent.lookup(name=name)
    twitter_data = twitter.scrape_user_tweets(username=twitter_username, num_tweets=5)

    print(f"Here is the LinkedIn data: {linkedin_data}")
    print(f"Here is the Twitter data: {twitter_data}")

    return linkedin_data, twitter_data


if __name__ == "__main__":
    ice_break(name="Bruno Garcia Echegaray")
