from ..db import get_default_connection

def insert_user(user):
    conn = get_default_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO Users 
            (UserName, FirstName, LastName, Password, Email, ContactNo, Country, Role, GroupName, ManagerName, IsActive, CreatedDate, DeletedDate)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user.UserName,
                user.FirstName,
                user.LastName,
                user.Password,
                user.Email,
                user.ContactNo,
                user.Country,
                user.Role,
                user.GroupName,
                user.ManagerName,
                user.IsActive,
                user.CreatedDate,
                user.DeletedDate,
            )
        )
        conn.commit()
        return True
    return False