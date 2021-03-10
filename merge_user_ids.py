from random import randrange, choice
import time

def merge(all_users):
    obj_to_return = {}

    for user in all_users:
        exists = False
        if "helpdesk_id" in user:
            temp_key = f"helpdesk_id-{user['helpdesk_id']}"
            if f"helpdesk_id-{user['helpdesk_id']}" in obj_to_return:
                obj_to_return[temp_key].update(user)
                exists = True

        if "email" in user:
            temp_key = f"email-{user['email']}"
            if f"email-{user['email']}" in obj_to_return:
                obj_to_return[temp_key].update(user)
                exists = True

        if "phone_number" in user:
            temp_key = f"phone_number-{user['phone_number']}"
            if f"phone_number-{user['phone_number']}" in obj_to_return:
                obj_to_return[temp_key].update(user)
                exists = True

        if not exists:
            obj_to_return[temp_key] = user
    return list(obj_to_return.values())


def merge_user_ids(existing_users, new_users):
    all_users = existing_users + new_users
    to_return = []
    while True:
        res = merge(all_users)
        if (res == to_return):
            break
        else:
            to_return = res

    return to_return

def speed_test():
    existing_users = []
    existing_count = 0
    new_count = 0
    new_users = []
    key_choices = ["helpdesk_id", "email", "phone_number"]
    for x in range(randrange(1, 20000)):
        existing_users.append({
            f"{choice(key_choices)}": f"key{randrange(1,2000)}", # this will test out the possibility for key vals being the same even tho the key is different 
            "name": f"name{randrange(1,500)}",
            "city": f"city{randrange(1,500)}",
            "color": f"color{randrange(1,500)}",
            "cheese": f"name{randrange(1,500)}",
            "dog": f"name{randrange(1,500)}"
        })
        existing_count += 1

    for x in range(randrange(1, 2000)):
        new_users.append({
            f"{choice(key_choices)}": f"key{randrange(1,25)}",
            "name": f"name{randrange(1,500)}",
            "city": f"city{randrange(1,500)}",
            "color": f"color{randrange(1,500)}",
        })
        new_count += 1

    start_time = time.time()
    result = len(merge_user_ids(existing_users, new_users))


    print(f"Merged {existing_count} existing records with {new_count} new records, resulting in {result} new records, in {time.time() - start_time} seconds")


def basic_test():

    existing_users = [
        {"helpdesk_id": 1, "name": "will"},
        {"helpdesk_id": 2, "name": "bill"},
    ]
    new_users = [{"helpdesk_id": 1, "city": "nyc"}]

    expected_answer = [
        {"helpdesk_id": 1, "name": "will", "city": "nyc"},
        {"helpdesk_id": 2, "name": "bill"}
    ]

    if merge_user_ids(existing_users, new_users) == expected_answer:
        print("Test 1 pass")
    else:
        print("Test 1 fail")

    existing_users = [
        {"helpdesk_id": 1, "name": "bob"},
        {"email": "e1", "color": "red"}
    ]
    new_users = [
        {"helpdesk_id": 1, "phone_number": "p1", "dog": "max"},
        {"email": "e1", "phone_number": "p1", "cheese": "stinky"}
    ]

    expected_answer = [
        {
            "helpdesk_id": 1,
            "email": "e1",
            "phone_number": "p1",
            "name": "bob",
            "color": "red",
            "dog": "max",
            "cheese": "stinky"
        }
    ]

    if merge_user_ids(existing_users, new_users) == expected_answer:
        print("Test 2 pass")
    else:
        print("Test 2 fail")


# Run tests
speed_test()
basic_test()