from django.shortcuts import render, redirect, get_object_or_404
from kafe_id.models import Meja, Menu, Pesanan, DetailPesanan, User
from django.utils import timezone
from django.urls import reverse

def tampilkan_menu(request, id):
    meja = get_object_or_404(Meja, pk=id)
    menu_items = Menu.objects.all()
    context = {
        'meja': meja,
        'menu_items': menu_items,
    }
    return render(request, 'kafe/menu_list.html', context)

def proses_pesanan(request):
    if request.method == 'POST':
        meja_id = request.POST.get('meja_id')
        meja = get_object_or_404(Meja, pk=meja_id)

        # Simpan user
        user = User.objects.create(meja=meja, waktu=timezone.now())

        # Simpan pesanan utama
        pesanan = Pesanan.objects.create(user=user, meja=meja, status='antri')

        # Simpan detail pesanan
        for key in request.POST:
            if key.startswith('menu_'):
                menu_id = key.split('_')[1]
                jumlah = int(request.POST[key])
                if jumlah > 0:
                    menu = Menu.objects.get(id=menu_id)
                    DetailPesanan.objects.create(
                        pesanan=pesanan,
                        menu=menu,
                        jumlah=jumlah
                    )

        redirect_url = reverse('tampilkan_menu', kwargs={'id': meja.id})
        return render(request, 'kafe/pesanan_sukses.html', {'meja': meja, 'redirect_url': redirect_url})

    else:
        return redirect('tampilkan_menu', id=1)

def Dashboard_admin(request):
    daftar_pesanan = Pesanan.objects.all().order_by('id')
    context = {'daftar_pesanan' : daftar_pesanan}
    return render(request, 'kafe/dashboard.html', context)

def update_status_pesanan(request, pesanan_id, status_baru):
    pesanan = get_object_or_404(Pesanan, id=pesanan_id)
    pesanan.status = status_baru
    pesanan.save()
    return redirect('dashboard_admin')