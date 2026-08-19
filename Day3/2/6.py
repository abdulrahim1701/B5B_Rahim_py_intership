admin_permissions = {
    "create",
    "edit",
    "delete",
    "manage_users"
}

editor_permissions = {
    "create",
    "edit"
}

required_permission = "delete"

if required_permission in editor_permissions:
    print("\nEditor can perform the action.")
else:
    print("\nEditor cannot perform the action; admin permission is required.")
