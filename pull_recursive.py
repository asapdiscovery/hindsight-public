from datetime import datetime
from github import Github, Auth
import os



def main():
    todays_date = datetime.date(datetime.now()).isoformat()

    token = os.getenv('HINDSIGHT_PAT_TOKEN')
    if not token:
        raise ValueError("No token found")

    # todays date

    # using an access token
    auth = Auth.Token(token)
    g = Github(auth=auth)

    repo = g.get_repo("asapdiscovery/hindsight")

    contents = repo.get_contents("hindsight/outputs/plots")
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            print(file_content)
            print(file_content.path)


    print("Done")

if __name__ == "__main__":
    main()

