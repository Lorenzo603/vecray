subscribers = {}


def register(event_type: str, fn):
    key = id(fn)
    if event_type not in subscribers:
        subscribers[event_type] = {key: fn}
    else:
        subscribers[event_type][key] = fn


def unregister(event_type: str, fn):
    if event_type not in subscribers:
        return
    key = id(fn)
    subscribers[event_type].pop(key)


def fire_event(event_type: str, data):
    if event_type not in subscribers:
        return
    events = subscribers[event_type]
    for fn in events.values():
        fn(data)


if __name__ == "__main__":
    def handle_some_event(data):
        print(data)


    def handle_some_event2(data):
        print(data)

    print(subscribers)
    register("aaa", handle_some_event)
    register("aaa", handle_some_event2)
    register("bbb", handle_some_event)

    fire_event("aaa", "data")

    print(subscribers)

    unregister("aaa", handle_some_event)

    print(subscribers)
