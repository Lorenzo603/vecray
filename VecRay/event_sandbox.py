
subscribers = {}

def subscribe(event_type: str, fn):
    key = id(fn)
    print(key)
    if not event_type in subscribers:
        subscribers[event_type] = {key: fn}
    else:
        subscribers[event_type][key] = fn

def unsubscribe(event_type: str, fn):
    if not event_type in subscribers:
        return
    print("unsub")
    key = id(fn)
    subscribers[event_type].pop(key)


def post_event(event_type: str, data):
    if not event_type in subscribers:
        return
    for fn in subscribers[event_type].values():
        fn(data)


def handle_some_event(data):
    print(data)
def handle_some_event2(data):
    print(data)

print(subscribers)
subscribe("aaa", handle_some_event)
subscribe("aaa", handle_some_event2)
subscribe("bbb", handle_some_event)
post_event("aaa", "data")

print(subscribers)

unsubscribe("aaa", handle_some_event)

print(subscribers)