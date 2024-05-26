""" Updates the GitHub release with the content from CHANGELOG.md """
import argparse
import functools
from pathlib import Path

import requests

from releaser import request_with_retries, make_auth_headers


def find_release_by_tag(repo_full_name: str, headers: dict[str, str], release_tag: str) -> str:
    release_resp = request_with_retries(
        functools.partial(
            requests.get,
            url=f"https://api.github.com/repos/{repo_full_name}/releases/tags/{release_tag}",
            headers=headers,
        )
    )
    try:
        release_resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            raise RuntimeError(f'Could not find a release by tag "{release_tag}"') from e
    latest_release_id = release_resp.json()["id"]
    return latest_release_id


def update_release_body(repo_full_name: str, headers: dict[str, str], release_id: str, new_body: str) -> None:
    release_resp = request_with_retries(
        functools.partial(
            requests.patch,
            url=f"https://api.github.com/repos/{repo_full_name}/releases/{release_id}",
            headers=headers,
            json=dict(
                body=new_body,
            ),
        )
    )
    release_resp.raise_for_status()
    print(release_resp.json()["html_url"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="DataLens Release Update")
    parser.add_argument("--changelog-path", type=Path, default=Path("../../../../CHANGELOG.md"))
    parser.add_argument("--root-repo-name", default="datalens-tech/datalens")

    args = parser.parse_args()

    changelog_body = ""
    with open(args.changelog_path, "r") as f:
        release_title = f.readline().strip()
        _, release_tag, _release_date = release_title.split(" ")
        new_line = f.readline()
        while not new_line.startswith("## v"):
            changelog_body += new_line
            new_line = f.readline()

    gh_auth_headers = make_auth_headers()
    release_to_update = find_release_by_tag(args.root_repo_name, gh_auth_headers, release_tag)
    update_release_body(args.root_repo_name, gh_auth_headers, release_to_update, changelog_body)
