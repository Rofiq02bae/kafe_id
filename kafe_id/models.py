from django.db import models

class Meja(models.Model):
    nama = models.CharField(max_length=50)

    def __str__(self):
        return self.nama

class User(models.Model):
    meja = models.ForeignKey(Meja, on_delete=models.SET_NULL, null=True)
    waktu = models.DateTimeField(auto_now_add=True)

class Menu(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama

class Pesanan(models.Model):
    STATUS_CHOICES = [
        ('antri', 'Antri'),
        ('proses', 'Proses'),
        ('selesai', 'Selesai'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meja = models.ForeignKey(Meja, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='antri')
    waktu = models.DateTimeField(auto_now_add=True)
    
class DetailPesanan(models.Model):
    pesanan = models.ForeignKey(Pesanan, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    jumlah = models.PositiveIntegerField()
