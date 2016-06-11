from django.db import models

# Create your models here.


class place(models.Model):
    placeName        = models.CharField(max_length=255, blank=True)
    room             = models.CharField(max_length=255, blank=True)


class program(models.Model):
    groupName        = models.CharField(max_length=255, blank=True)
    contentName      = models.CharField(max_length=255, blank=True)
    contentData      = models.CharField(max_length=255, blank=True)
    category         = models.IntegerField(default=0)
    place            = models.ForeignKey(place)
    firstFlag        = models.BooleanField(default=False)
    secondFlag       = models.BooleanField(default=False)
    thirdFlag        = models.BooleanField(default=False)
    allFlag          = models.BooleanField(default=False)
    start_at         = models.DateTimeField(null=True, blank=True)
    end_at           = models.DateTimeField(null=True, blank=True)
    created_at       = models.DateTimeField(null=True, auto_now_add=True)
    updated_at       = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __unicode__(self):
        return self.contentName

    def place__placeName(self):
        return self.place.placeName

    class Meta:
        ordering=['created_at']


class photo(models.Model):
    program          = models.ForeignKey(program)
    path             = models.CharField(max_length=255, blank=True)
    publicFlag       = models.BooleanField(default=False)
    created_at       = models.DateTimeField(null=True, auto_now_add=True)


class vote(models.Model):
    program          = models.OneToOneField(program)
    num              = models.IntegerField(default=0)

    def __unicode__(self):
        return self.program.contentName

    def place(self):
        return self.program.place


