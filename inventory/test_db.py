from django.http import JsonResponse
from .db import get_default_connection

def test_db(request):
    conn = get_default_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT TOP 10 * FROM Tenants")  # ya aapke table ka naam
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]
        return JsonResponse({"status": "success", "rows": data})
    else:
        return JsonResponse({"status": "error", "message": "DB not connected"})
