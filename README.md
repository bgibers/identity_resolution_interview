# identity_resolution_interview
```
Write a function called merge_user_ids that merges two arrays of user
objects to provide a final array of user objects (identity resolution).

We should merge two objects if they share any of the same "primary"
keys. The three possible primary keys are:
    helpdesk_id
    email
    phone_number

For all other fields, a match on any other key does not indicate that
the users should be merged. For example, users from the same city but
with no other matches should not be merged.

When merging, any conflicts can be resolved arbitrarily. For example, if
two user objects are to be merged and one has key "city" with value
"nyc" and one has key "city" with value "brooklyn" you may select either
as the key in the final object.

ARGS:
    existing_users - array of existing user objects, i.e. the data of
        users already in the system
    new_users - array of new user objects from the most recent pull
        from the helpdesk, which should be merged into the existing
        users OR merged with other new user objects (if any) to form a
        new user object in the output
RETURNS:
    an array of final user objects

Example 1 (simple):
ARGS:
    existing_users = [
        {"helpdesk_id": 1, "name": "will"},
        {"helpdesk_id": 2, "name": "bill"}
    ]
    new_users = [{"helpdesk_id": 1, "city": "nyc"}]
RETURNS:
    [
        {"helpdesk_id": 1, "name": "will", "city": "nyc"},
        {"helpdesk_id": 2, "name": "bill"}
    ]

Example 2 (more involved):
ARGS:
    existing_users = [
        {"helpdesk_id": 1, "name": "bob"},
        {"email": "e1", "color": "red"}
    ]
    new_users = [
        {"helpdesk_id": 1, "phone_number": "p1", "dog": "max"},
        {"email": "e1", "phone_number": "p1", "cheese": "stinky"}
    ]
RETURNS:
    [
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
```
