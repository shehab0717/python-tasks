

import auth


def app():
    authinticated, user = auth.start()
    print(f"{user}")


app()