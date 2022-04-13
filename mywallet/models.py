from django.db import models


class WalletUser(models.Model):
    username = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100, null=False)

    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.username
    
    def toDataSet(self):
        return {
            'username': self.username,
            'name': self.name, 
            'first_name': self.first_name,
            'amount': self.amount
        }

class Transfer(models.Model):
    sender = models.ForeignKey(WalletUser, on_delete=models.CASCADE, related_name='sender')
    receiver= models.ForeignKey(WalletUser, on_delete=models.CASCADE, related_name='receiver')
    amount = models.DecimalField(decimal_places=2, max_digits=10)

# Create your models here.
