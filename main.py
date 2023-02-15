import requests


class Main(object):
    def __init__(self):
        self.url = "https://api.github.com/repos/freeCodeCamp/freeCodeCamp/contributors"
        self.headers = {
            "Authorization": "Bearer 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"
        }

    @property
    def get(self):
        try:
            response = requests.get(self.url, headers=self.headers)

            response.raise_for_status()
            response_body = response.json()

            user_list = []

            for body in response_body:
                user = requests.get(
                    f'https://api.github.com/users/{body["login"]}',
                    headers={
                        "Authorization": "Bearer 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"
                    },
                )

                data = {
                    "username": body["login"],
                    "contributions": body["contributions"],
                    "location": user.json()["location"],
                }
                user_list.append(data)

            new_user_list = sorted(
                user_list, key=lambda d: d["contributions"], reverse=True
            )[:25]

            for user in new_user_list:
                print(user)

        except requests.exceptions.ConnectionError as e:
            raise SystemExit(e)

        except requests.exceptions.Timeout as e:
            raise SystemExit(e)

        except requests.exceptions.HTTPError as e:
            raise SystemExit(e)

        except requests.exceptions.RequestException as e:
            raise SystemExit(e)


if __name__ == "__main__":
    Main().get
