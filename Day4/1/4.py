usernames = ["alex", "johnny", "bob", "samantha", "anna"]

result = list(filter(lambda username: len(username) >= 6, usernames))

print(result)