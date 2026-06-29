#!/usr/bin/python3
"""Module for fetching and saving posts from JSONPlaceholder."""
import requests
import csv


def fetch_and_print_posts():
    """Fetch all posts and print their titles."""
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch all posts and save them to posts.csv."""
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    if response.status_code == 200:
        posts = response.json()

        data = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in posts
        ]

        with open(
            "posts.csv",
            mode="w",
            newline="",
            encoding="utf-8"
        ) as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["id", "title", "body"]
            )

            writer.writeheader()
            writer.writerows(data)
