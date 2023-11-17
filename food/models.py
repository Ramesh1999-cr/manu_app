from django.db import models

# Create your models here.
class Item(models.Model):
    item_name=models.CharField(max_length=200)
    item_dsc=models.CharField(max_length=500)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=600,default="https://www.google.com/search?q=pizza+pic&rlz=1C1CHBF_enIN1041IN1042&sxsrf=AB5stBiKdXwdVAUlNf-UGHGzJ5nS2UmnCA:1690453289196&tbm=isch&source=iu&ictx=1&vet=1&fir=vwyNmrlxb87lKM%252C5xpz_Vm2ema2NM%252C%252Fm%252F0663v%253BOt0IjAyD4C7f_M%252CL_YY9OWBaDG7sM%252C_%253BefJ23c2_JH_n7M%252CbBq_NwtYzsoXvM%252C_%253BSoPN2gMsF42S-M%252CbJrwjubfhkn9gM%252C_%253BaiM4Q7-DR5ureM%252CSeOWqVcLRTzMfM%252C_%253BIEfM_7QrpfT8ZM%252CWYOf39ozq1-2MM%252C_&usg=AI4_-kSWCKjgsj8AMKRYwuYXn0U8aeCa0g&sa=X&ved=2ahUKEwiIhb-e1a6AAxWLbmwGHZuqC-UQ_B16BAhIEAE#imgrc=vwyNmrlxb87lKM")




