import pickle
import scripts


class UserProfile:
    def __init__(self, username='USER', profile_pic=None, theme=None):
        self.username = username
        self.profile_pic = profile_pic
        self.theme = theme
        self.highscore = 0
        self.last_score = 0


def check_user_exist():
    try:
        with open(scripts.openfile('data/user.tetrisprofile'), 'rb') as f:
            pass
    except FileNotFoundError:
        with open(scripts.openfile('data/user.tetrisprofile'), 'wb') as f:
            pickle.dump(UserProfile(), f)
