from django.db import models

# Create your models here.

class School(models.Model):
    ''' 
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        # Ensure only school users can be linked
        limit_choices_to={'profile__user_type': 'school'},
        related_name='school_profile',
        null=True,
        blank=True
    )'''
    # Make sute that username is the User.username field from the User Model
    username = models.CharField(max_length=250, blank=False)
    schoolname = models.CharField(max_length=100, blank=True)
    telephone = models.CharField(max_length=200, blank=True, null=True)
    schoolemail = models.EmailField(blank=True, null=True)
    schooladdress = models.TextField(max_length=100, default="", blank=False)
    postal_address = models.CharField(max_length=100, blank=True)
    website = models.TextField(max_length=100, blank=True, null=True)
    slogan = models.CharField(max_length=200, blank=True)
    emblem = models.ImageField(
        upload_to='uploads/schoolprofile/', default=None, blank=True, null=True)

    SCHOOL_SECTOR = [
        ('Primary', 'Primary School'),
        ('Secondary', 'Secondary School'),
        ('Combined', 'Combined School'),
        ('Vocational', 'Vocational School'),
        ('Other', 'Other School'),
    ]
    type_of_school = models.CharField(
        max_length=200, blank=True, choices=SCHOOL_SECTOR)

    UMALUSI = [
        ('DBE', 'The Department of Basic Education (DBE)'),
        ('IEB', 'The Independent Examination Board (IEB)'),
        ('SACAI', 'The South African Comprehensive Assessment Institute (SACAI)')
    ]
    umalusi = models.CharField(max_length=200, blank=True, choices=UMALUSI)

    PROVINCE = [
        ('Limpopo', 'Limpopo'),
        ('Free State', 'Free State'),
        ('Gauteng', 'Gauteng'),
        ('North West', 'North West'),
        ('KwaZulu-Natal', 'KwaZulu-Natal'),
        ('Mpumalanga', 'Mpumalanga'),
        ('Eastern Cape', 'Eastern Cape'),
        ('Northern Cape', 'Northern Cape'),
        ('Western Cape', 'Western Cape'),
    ]
    provinc = models.CharField(max_length=50, choices=PROVINCE, null=True)

    DISTRICT = [
        ('Alfred Nzo District', 'Alfred Nzo District'),
        # Add remaining district choices here
    ]
    district = models.CharField(max_length=200, default="", choices=DISTRICT)

    CIRCUIT = [
        ('Soutpansberg East', 'Soutpansberg East Circuit'),
        # Add remaining circuit choices here
    ]
    circuit = models.CharField(max_length=200, default="", choices=CIRCUIT)

    CURRICULUM = [
        ('CAPS', 'CAPS curriculum'),
        ('Cambridge', 'Cambridge curriculum')
    ]
    curriculum = models.CharField(
        max_length=100, blank=True, choices=CURRICULUM)

    grade_levels = models.CharField(max_length=100, blank=True)
    local_municipality = models.CharField(max_length=100, blank=True)
    urban_rural = models.CharField(max_length=100, blank=True)
    ward_id = models.CharField(max_length=100, blank=True)
    Eei_district = models.CharField(max_length=100, blank=True)

    emis_number = models.CharField(max_length=100, blank=True)
    examination_number = models.CharField(max_length=100, blank=True)
    examination_centre = models.CharField(max_length=100, blank=True)
    persal_paypoint_number = models.CharField(max_length=100, blank=True)
    persal_component_number = models.CharField(max_length=100, blank=True)

    name_of_principal = models.CharField(max_length=100, blank=True)
    number_of_teachers = models.CharField(max_length=100, blank=True)

    SECTION = [
        ('Section 21 (Self Reliant)', 'Self Reliant: Yes'),
        ('Section 21 (Self Reliant)', 'Self Reliant: No'),
    ]
    section_21 = models.CharField(max_length=100, choices=SECTION, blank=True)
    school_fees = models.CharField(max_length=100, blank=True)

    QUANTILE = [
        ('Quintile 1', 'Q1'),
        ('Quintile 2', 'Q2'),
        ('Quintile 3', 'Q3'),
        ('Quintile 4', 'Q4'),
        ('Quintile 5', 'Q5'),
    ]
    quintile_Level = models.CharField(max_length=100, choices=QUANTILE, blank=True)

    image1 = models.ImageField(
        upload_to='uploads/schoolprofile/', default=None, blank=True, null=True)

    history = models.CharField(max_length=200, blank=True)
    mission = models.CharField(max_length=200, blank=True) 

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'school profile'