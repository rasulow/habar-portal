from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(choices=(
            ('category', 'category'),
            ('language', 'language'),
        ),
        default='category',
        max_length=8
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return self.title
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        

    
class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/')
    view_count = models.IntegerField(default=0, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'news'
        verbose_name = 'news'
        verbose_name_plural = 'news'
        
        
    
class Icons(models.Model):
    img = models.FileField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.img}'.split('images/')[1]
    
    class Meta:
        db_table = 'icon'
        verbose_name = 'icon'
        verbose_name_plural = 'icons'
        
class Weather(models.Model):
    degree = models.CharField(max_length=10)
    icon = models.ForeignKey(Icons, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.degree
    
    class Meta:
        db_table = 'weather'
        verbose_name = 'weather'
        verbose_name_plural = 'weathers'
        
