import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """
    Scrape Linkedin profile with Nubela's ProxyCurl API
    """
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f"Bearer {os.getenv('PROXY_CURL_API')}"}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

    exclude_keys = [
        "people_also_viewed",
        "recommendations",
        "languages",
        "certifications",
    ]

    data = response.json()
    data = {
        key: value
        for key, value in data.items()
        if key not in exclude_keys and value not in ([], "", "", None)
    }

    if data.get("groups") is not None:
        for group_dict in data.get("groups", []):
            group_dict.pop("profile_pic_url", None)

    if data.get("experiences") is not None:
        for experience_dict in data.get("experiences", []):
            experience_dict.pop("logo_url", None)
            experience_dict.pop("company_linkedin_profile_url", None)

    return data
