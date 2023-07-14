def is_subscribed(newsletter, email):
    subscribers = []
    if newsletter is not None and newsletter.get("subscribers") is not None:
            subscribers = newsletter.get("subscribers")
    if email in subscribers:
        return True
    return False