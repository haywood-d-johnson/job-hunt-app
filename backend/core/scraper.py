import requests, random, time
from bs4 import BeautifulSoup

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Android 11; Mobile; rv:68.0) Gecko/68.0 Firefox/89.0",
    # Add more User-Agents here...
]

def get_random_user_agent():
    """Returns a random User-Agent string."""
    return random.choice(USER_AGENTS)

def scrape_indeed(keyword, location=""):
    """Scrapes job listings from Indeed."""
    url = f"https://www.indeed.com/jobs?q={keyword}&l={location}"
    headers = {
        "User-Agent": get_random_user_agent()
    }

    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.content, "html.parser")
        listings = []

        for job_card in soup.find_all("div", class_="job_seen_beacon"):
            title_element = job_card.find("h2", class_="jobTitle")
            company_element = job_card.find("span", class_="companyName")
            location_element = job_card.find("div", class_="companyLocation")
            link_element = job_card.find("a", class_="jcs-JobTitle")

            if title_element and company_element and location_element and link_element:
                title = title_element.text.strip()
                company = company_element.text.strip()
                location = location_element.text.strip()
                href = "https://www.indeed.com" + link_element["href"]


                listings.append({
                    "title": title,
                    "company": company,
                    "location": location,
                    "link": link
                })

        time.sleep(random.uniform(1, 3))

        return listings

    except requests.exceptions.RequestException as e:
        print(f"Error during scraping: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
