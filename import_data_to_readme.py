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

todays_date = datetime.date(datetime.now()).isoformat()
content = {
"./plots/docking.png": f"hindsight/outputs/plots/docking/cross_moleculeset/{todays_date}_all_vs_cdd.png",
"./plots/fecs.png": f"hindsight/outputs/plots/fecs/all_fecs_all_targets_all_msets/{todays_date}.png",
"./plots/ml-gat.png": f"hindsight/outputs/plots/ml-gat/cross_moleculeset/{todays_date}_all_vs_cdd.png",
"./plots/ml-schnet.png": f"hindsight/outputs/plots/ml-schnet/cross_moleculeset/{todays_date}_all_vs_cdd.png",
}

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

    for local, remote in content.items():
        write_from_repo_to_local(repo, remote, local)

    print("Done")


if __name__ == "__main__":
    main()
