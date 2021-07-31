"""
It can sometimes be handy to do something with an exception (handle it), but then not silence it.

For example, if an exception is raised in a function and you catch it:
"""
class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement
        self.score = 0

    def __repr__(self):
        return f'<User {self.name}>'

def get_user_score(user):
    try:
        user.score = perform_calculation(user.engagement_metrics)
    except KeyError:
        print('Incorrect values provided to our calculation function.')
 #      raise
    else:  
        if user.score > 500:
            send_engagement_notification(user)

       
def perform_calculation(metrics):
        return metrics['clicks'] * 5 + metrics['hits'] * 2 #key error raised here with the 'clicks' for the dictionary below

def send_engagement_notification(user):
        print(f'Notification sent to {user}.')




my_user = User('Rolf', {'clicks': 61, 'hits': 100})
get_user_score(my_user)

