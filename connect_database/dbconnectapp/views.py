from django.shortcuts import render
from django.db import connection
# Create your views here.
def student_list(request):

    cursor = connection.cursor()
    sql = "SELECT * FROM details"
    cursor.execute(sql)
    r = cursor.fetchone()
    print(r)
    return render(request,'output.html',{'data': r})



