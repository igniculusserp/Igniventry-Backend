from inventory.models.user_model import User
from inventory.repositories.user_repository import insert_user as repo_insert_user

def create_user_service(data):
    # Validation yahan kar sakte hain (optional)
    user = User(
        UserName=data.get("UserName"),
        FirstName=data.get("FirstName"),
        LastName=data.get("LastName"),
        Password=data.get("Password"),
        Email=data.get("Email"),
        ContactNo=data.get("ContactNo"),
        Country=data.get("Country"),
        Role=data.get("Role"),
        GroupName=data.get("GroupName"),
        ManagerName=data.get("ManagerName"),
        IsActive=data.get("IsActive"),
        CreatedDate=data.get("CreatedDate"),
        DeletedDate=data.get("DeletedDate"),
    )
    return repo_insert_user(user)