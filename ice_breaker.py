from agents import linkedin_agent
from third_parties import linkedin


def ice_break(name: str):
    linkedin_profile_url = linkedin_agent.lookup(name=name)
    linkedin_data = linkedin.scrape_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url
    )

    print(f"Here is the LinkedIn data: {linkedin_data}")
    return linkedin_data


if __name__ == "__main__":
    ice_break(name="Bruno Garcia Echegaray")
