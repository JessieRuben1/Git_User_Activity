# GitHub User Activity CLI

## Introduction
`github_activity.py` is a simple command-line interface (CLI) application that fetches the recent activity of a GitHub user and displays it in the terminal. This project utilizes the GitHub API to provide insights into a user's recent events, such as pushes, issues, stars, and more.

---

## Features
- Fetch recent activity of any GitHub user.
- Display information in a human-readable format.
- Graceful handling of errors such as invalid usernames or API failures.

---

## Prerequisites
- Python 3.x installed on your system.
- Internet connection to access the GitHub API.

---

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/JessieRuben1/Git_User_Activity.git
   cd Git_User_Activity
   ```

2. **Check Dependencies:**
   This project uses the `requests` module, which is included in Python's standard library. Ensure it is installed:
   ```bash
   pip install requests
   ```

---

## Usage

Run the script using Python, providing the desired GitHub username as an argument.

### Fetch User Activity
```bash
python github_activity.py <GitHub_username>
```

Example:
```bash
python github_activity.py kamranahmedse
```

### Sample Output:
```
Pushed 3 commits to kamranahmedse/developer-roadmap
Opened an issue in kamranahmedse/developer-roadmap
Starred kamranahmedse/developer-roadmap
```

---

## Error Handling
- If the username is invalid or the user does not exist:
  ```bash
  Error: GitHub user '<username>' not found.
  ```
- If there are connectivity issues or the API fails:
  ```bash
  Error: Could not connect to GitHub API. Details: <error details>
  ```

---

## Roadmap
- Add the ability to filter events by type (e.g., Push, Issue).
- Include structured output (e.g., tables or JSON format).
- Implement caching to reduce API calls for repeated requests.

---

## Contribution
Contributions are welcome! Feel free to fork this repository, create a new branch, and submit a pull request for any feature enhancements or bug fixes.

---

## License
This project is licensed under the MIT License.

---

## Author
Developed by Jessie Ruben. 😊
```