from django.db import models

# Create your models here.


class Book(models.Model):
    STATES = [
        ('available', 'Available'),
        ('checkedout', 'Checked Out'),
    ]

    title = models.CharField(max_length=48)
    author = models.CharField(max_length=72)
    year = models.CharField(max_length=4)
    status = models.CharField(choices=STATES, default='available', max_length=48)
    date_added = models.DateTimeField(auto_now_add=True)
    last_borrowed = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return f'Book: {self.title} ({self.status})'


def __repr__(self):
    return f'< Book: {self.title} | Author: {self.author} | Year: {self.year} | ISBN: {self.isbn} | Date_Added: {self.date_added} | Last_Borrowed {self.last_borrowed} | ({self.status}) >'
