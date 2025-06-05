import requests
from bs4 import BeautifulSoup

def fetch_hacker_news():
    url = "https://news.ycombinator.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        titles = soup.select('.titleline > a')
        if not titles:
            print("No titles found. The structure may have changed.")
            return

        print("\n🔥 Top Hacker News Headlines:\n")
        for i, title in enumerate(titles[:15], start=1):  # Limit to top 15
            print(f"{i}. {title.text}\n   Link: {title['href']}\n")
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

def main():
    print("=== Interactive Web Scraper ===")
    print("1. Fetch Hacker News Headlines")
    print("2. Exit")
    
    while True:
        choice = input("\nChoose an option (1-2): ")
        if choice == '1':
            fetch_hacker_news()
        elif choice == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
