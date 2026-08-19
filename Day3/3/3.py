library = {
    "B101": {
        "title": "Python Basics",
        "author": "John Smith",
        "copies": 5
    },
    "B102": {
        "title": "Data Structures",
        "author": "Alice Brown",
        "copies": 3
    },
    "B103": {
        "title": "Machine Learning",
        "author": "David Lee",
        "copies": 4
    }
}


book_id = "B101"

if library[book_id]["copies"] > 0:
    library[book_id]["copies"] -= 1
    print("Book issued successfully.")
else:
    print("Book is not available.")

print(library)