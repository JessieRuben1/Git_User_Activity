import sys
import requests

# fetch user activity from the Github API
def fetch_user_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    
    try:
        # send the HTTP GET request
        response = requests.get(url)
        
        # check for successful response
        if response.status_code == 200:
            activities = response.json()
            
            # Display user activities
            for activity in activities[:10]: # fetch recent 10 activites
                repo_name = activity.get("repo", {}).get("name", "Unknnown repo")
                action_type = activity.get("type", "Unknown action")
                
                # generate readable messages for specific actions
                if action_type == "PushEvent":
                    commit_count = len(activity.get("payload", {}).get("commits", []))
                    print(f"Pushed {commit_count} commits to {repo_name}")
                elif action_type == "IssueEvent":
                    action = activity.get("payload", {}).get("action", "Unknown")
                    print(f"{action.capitalize()} an issue in {repo_name}")
                elif action_type == "WatchEvent":
                    print(f"Starred {repo_name}")
                else:
                    print(f"{action_type.replace('Event', '')} in {repo_name}")
        elif response.status_code == 404:
            print(f"Error: GitHub user '{username}' not found.")
        else:
            print(f"Error: Failed to fetch data (status code {response.status_code}).")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not connect to GitHub API. Details: {e}")
        
# main cli entry point 
def main():
    if len(sys.argv) < 2:
        print("Usage: github_activity.py <username>")
        return
    
    username = sys.argv[1]
    fetch_user_activity(username)

if __name__ == "__main__":
    main()