from datetime import datetime
from github import Github, Auth
import os


def write_from_repo_to_local(repo, remote_path, local_path):
    found = False
    try:
        contents = repo.get_contents(remote_path)
        found = True
    except Exception as e:
        print(f"Error: {e}")

        
    if found:
        print(f"Found: {remote_path}") 
        with open(local_path, "wb") as file:
            file.write(contents.decoded_content)
        print(f"File written: {local_path}")
    else:
        print(f"File not found: {remote_path}")



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
            path = file_content.path
            print(path)
             # strip first three dirs from path
            local_path = "/".join(path.split("/")[3:])
            local_path = "plots/detail/" + local_path
            write_from_repo_to_local(repo, path, local_path)


    print("Done")

if __name__ == "__main__":
    main()

