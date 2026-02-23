from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Employee


def index(request):
    """หน้าแรก — เปลี่ยนเส้นทางไปหน้าฟอร์ม"""
    return redirect('form')


def form(request):
    """
    ฟังก์ชันแสดงและจัดการฟอร์มบันทึกข้อมูลพนักงาน
    - GET  → แสดงฟอร์มเปล่า
    - POST → รับข้อมูล ตรวจสอบ และบันทึกลง Database
    """
    if request.method == 'POST':
        full_name = request.POST.get('fullName', '').strip()
        email = request.POST.get('email', '').strip()
        position = request.POST.get('position', '').strip()
        phone = request.POST.get('phone', '').strip()

        # ตรวจสอบข้อมูลครบถ้วน
        if not all([full_name, email, position, phone]):
            messages.error(request, '⚠️ กรุณากรอกข้อมูลให้ครบทุกช่อง')
            return render(request, 'form.html', {
                'full_name': full_name,
                'email': email,
                'position': position,
                'phone': phone,
            })

        # ตรวจสอบอีเมลซ้ำ
        if Employee.objects.filter(email=email).exists():
            messages.error(request, f'❌ อีเมล {email} ถูกใช้งานแล้ว')
            return render(request, 'form.html', {
                'full_name': full_name,
                'email': email,
                'position': position,
                'phone': phone,
            })

        # บันทึกลงฐานข้อมูล
        Employee.objects.create(
            full_name=full_name,
            email=email,
            position=position,
            phone=phone,
        )
        messages.success(request, f'✅ บันทึกข้อมูลของ {full_name} เรียบร้อยแล้ว!')
        return redirect('form')

    return render(request, 'form.html')


def contact(request):
    """ฟังก์ชันแสดงหน้าติดต่อ"""
    return render(request, 'contact.html')


def employee_list(request):
    """แสดงรายชื่อพนักงานทั้งหมด"""
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})
