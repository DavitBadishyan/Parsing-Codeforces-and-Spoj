import requests
import json
from bs4 import BeautifulSoup as BS

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def load_usernames(path='usernames.txt'):
    with open(path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def get_all_problems_by_rating(rating):
    url = "https://codeforces.com/api/problemset.problems"
    r = requests.get(url, headers=headers)
    data = r.json()
    if data.get("status") != "OK":
        raise RuntimeError("Failed to fetch problemset")
    problems = data["result"]["problems"]
    return {
        (p["contestId"], p["index"], p["name"])
        for p in problems if p.get("rating") == rating
    }

def get_user_solved(user):
    solved = set()
    url = f"https://codeforces.com/api/user.status?handle={user}"
    r = requests.get(url, headers=headers)
    soup = BS(r.content, 'html.parser')
    data = json.loads(str(soup))
    for item in data.get("result", []):
        try:
            verdict = item.get('verdict', '')
            # if verdict == 'OK':  #not only accepted ones if user tried this problem don't include it on contest
            p = item["problem"]
            solved.add((p["contestId"], p["index"]))
        except Exception:
            # Skip problematic entries
            pass
    return solved

def find_unsolved(usernames, rating):
    all_problems = get_all_problems_by_rating(rating)
    all_solved_names = set()
    for user in usernames:
        print(f"Fetching solved problems for user: {user}")
        solved = get_user_solved(user)
        all_solved_names.update(solved)
    unsolved = []
    for contestId, index, name in all_problems:
        if (contestId, index) not in all_solved_names:
            unsolved.append((contestId, index, name))
    return sorted(unsolved)

if __name__ == "__main__":
    usernames = load_usernames()
    rating = int(input("Enter desired problem rating (e.g., 800): "))
    unsolved = find_unsolved(usernames, rating)
    for contestId, index, name in unsolved:
        print(f"https://codeforces.com/problemset/problem/{contestId}/{index} : {name}")
