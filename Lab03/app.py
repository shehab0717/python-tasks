

import auth


def app():
    authinticated, userId = auth.start()
    print(f"User id: {userId}")


app()