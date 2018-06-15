from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserProfile(models.Model):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'

    GENDERS_CHOICES = (
        (GENDER_MALE, GENDER_MALE),
        (GENDER_FEMALE, GENDER_FEMALE)
    )

    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    referral_code = models.CharField(max_length=255, blank=True, null=True, unique=True)
    locale = models.CharField(max_length=10, blank=True, null=True, default='en')
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=255, choices=GENDERS_CHOICES, blank=True, null=True)
    picture = models.ImageField(upload_to='users/pictures/%Y/%m/%d', blank=True, null=True)
    country = models.ForeignKey('countries.Country', null=True, blank=True, on_delete=models.SET_NULL)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    api_key = models.CharField(max_length=255, blank=True, null=True)

    # social networks
    facebook_id = models.CharField(max_length=255, blank=True, null=True, unique=True)
    twitter_id = models.CharField(max_length=255, blank=True, null=True, unique=True)
    twitter_access_key = models.CharField(max_length=255, blank=True, null=True, unique=True)
    twitter_access_secret = models.CharField(max_length=255, blank=True, null=True, unique=True)
    google_access_key = models.CharField(max_length=255, blank=True, null=True, unique=True)

    # geoposition
    user_ip = models.CharField(max_length=255, blank=True, null=True)
    # coordinates = geo_models.PointField(blank=True, null=True)
    # position = GeopositionField(blank=True, null=True)
    timezone = models.CharField(blank=True, null=True, max_length=255)

    premium = models.BooleanField(default=False)

    # def save(self, *args, **kwargs):
    #     if not self.referral_code and self.user:
    #         self.referral_code = self.user.id + int(''.join(random.choice(string.digits) for _ in range(5)))
    #     if self.position and not self.coordinates:
    #         self.coordinates = 'POINT(%s %s)' % (self.position.longitude, self.position.latitude)
    #     if not self.api_key:
    #         random_part = ''.join(
    #             random.choice(string.ascii_lowercase + string.digits) for _ in range(settings.HASH_UNIQUE_NUMBER))
    #         self.api_key = hashlib.sha256(
    #             str(self.id) + datetime.datetime.utcnow().strftime('%Y%d%m%H%M%S%f')).hexdigest() + random_part
    #     return super(UserProfile, self).save(*args, **kwargs)

    class Meta:
        db_table = 'user_profiles'

    def __str__(self):
        return "%s, id: %s" % (self.user_id, self.id)