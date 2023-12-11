from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import datetime
from django.utils import timezone
from django.core.validators import RegexValidator

class EmployeeManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Email address is required')
        
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        
        if kwargs.setdefault('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, password, **kwargs)
    
class Login_employee(models.Model):
    # Other fields
    is_verified = models.BooleanField(default=False)


class Employee(AbstractBaseUser, PermissionsMixin):
     email = models.EmailField(max_length=255, unique=True)
     first_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255)
     id_number = models.CharField(max_length=13, null=True, default=None)
     cell = models.CharField(max_length=15)
     dept = models.CharField(max_length=255)
     emp_type = models.CharField(max_length=25)
     postal = models.CharField(max_length=255)
     home_address = models.CharField(max_length=500, default=None, null=True)
     work_address = models.CharField(max_length=500, default=None, null=True)
     postal_address = models.CharField(max_length=500, default=None, null=True)
     ip_address = models.CharField(max_length=255)
     mac_address = models.CharField(max_length=255)
     reg_time = models.DateTimeField(blank=True, null=True, default=timezone.now) 
     is_active = models.BooleanField(default=True)
     is_staff = models.BooleanField(default=True)
     is_admin = models.BooleanField(default=False)
     is_verified = models.BooleanField(default=False)
     password = models.CharField(max_length=255)

    
     objects = EmployeeManager()
     USERNAME_FIELD = 'email'
     REQUIRED_FIELDS = []
    
    
     def __str__(self):
         return f'{self.email}'
    
     def has_perm(self, perm, obj=None):
         return True
    
     def has_module_perms(self, app_label):
         return True
    
     @property
     def is_staff(self):
         return self.is_admin

    
    
class clockin(models.Model): 
    # username = models.ForeignKey(mockdata, on_delete=models.CASCADE, null=True)
    user_id = models.IntegerField(default=None)
    IDNumber = models.CharField(max_length=13)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255)
    geolocation = models.CharField(max_length=255)
    clockin_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    clockout_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    takebreak = models.DateTimeField(blank=True, null=True, default=timezone.now)
    endbreak =  models.DateTimeField(blank=True, null=True, default=timezone.now)
    
class employees(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    total_leave_days = models.IntegerField(default=15)
    status_choices = [
        ('A', 'Active'),
        ('I', 'Inactive'),
    ]

    status = models.CharField(max_length=255, choices=status_choices)
    project_name = models.CharField(max_length=255, default=None)
    project_role = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.name
class Record(models.Model):
    employee = models.ForeignKey(employees, on_delete=models.CASCADE) 
    record_type_choices =[
        ('L', 'Leave'),
        ('R','Resignation'),
        ('T', 'Termination'),
    ]
    record_type = models.CharField(max_length=1, choices= record_type_choices )
    date = models.DateField()
    details =  models.TextField()
    status_choices = [
        ('A', 'Active'),
        ('I', 'Inactive'),
    ] 

class Leave(models.Model):
    LEAVE_TYPES = (
        ('sick', 'Sick'),
        ('vacation', 'Vacation'),
        ('personal', 'Personal'),
    )

    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=255, default=None)
    duration = models.PositiveSmallIntegerField(null=True, blank=True)
    total_leave_days = models.IntegerField(default=15)
    days_left = models.IntegerField(default=15)
    status_choices = models.CharField(max_length=255, default="Pending")
    userid = models.IntegerField()
    description = models.CharField(max_length=1000, default=None)


"""
class Leave(models.Model):
    employee = models.ForeignKey(employees, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    LEAVE_TYPES = (
        ('sick', 'Sick'),
        ('vacation', 'Vacation'),
        ('personal', 'Personal'),
    )
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPES)
    total_number = models.IntegerField()
    used_number = models.IntegerField()
    remaining_number = models.IntegerField(null=True, blank=True)
   

    

    def calculate_remaining_number(self):
        if self.total_number and self.used_number:
            remaining = self.total_number - self.used_number
            self.remaining_number = remaining if remaining > 0 else 0
        else:
            self.remaining_number = None
"""

class resignation_model(models.Model):
    empname = models.CharField(max_length=100, null=True)
    filename = models.CharField(max_length=100, null=True)
    # department = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)
    noticedate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    resigndate = models.DateTimeField(blank=True, null=True, default=timezone.now)

#class recentprojects(models.models):
 #   name = models.CharField(max_length=100)
  #  progress = models.JSNONField()


class Termination(models.Model):
    name = models.ForeignKey(employees, on_delete=models.CASCADE)
    filename = models.CharField(max_length=100, null=True)
    department = models.CharField(max_length=100)
    terminationtype = models.CharField(max_length=100)
    terminationdate = models.DateField(auto_now_add=False)
    reason = models.CharField(max_length=100)
    noticedate = models.DateField(auto_now_add=False)
"""
class ProgressBar(models.Model):
    name =  models.ForeignKey(employees, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)

    progress = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=False)
    """
class Project(models.Model):
    projectname = models.CharField(max_length=255, default=None)
    leader = models.CharField(max_length=255, default=None)
    startdate = models.DateField(auto_now_add=False)
    enddate = models.DateField(auto_now_add=False)
    status = models.CharField(max_length=100)
    github = models.CharField(max_length=255, default=None)

    """
    progress = models.CharField(
        max_length=6,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
            # Regex pattern that matches a percentage with 0-2 decimal places
            validators.RegexValidator(r'^\d{1,2}(\.\d{1,2})?%$',
                                      'Enter a percentage with up to 2 decimal places (e.g. 25.50%)')
        ]
    )
    """

class UserProfile(models.Model):
    user_id = models.IntegerField(default=None)
    profile_picture = models.ImageField(upload_to='App/static/media', null=True, blank=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    birth_date = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=15)
    address = models.CharField(max_length=150, default='')
    state = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=250, default='')
    zip_code = models.CharField(max_length=90, default='')
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+27764835831'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=20, default='')
    department = models.CharField(max_length=50, default='')
    designation = models.CharField(max_length=80, default='')
    report = models.CharField(max_length=95, default='')

class PersInfo(models.Model):
    id_num = models.CharField(max_length=15, default='')
    pass_num = models.CharField(max_length=20, default='')
    pass_expdate = models.DateField(auto_now_add=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+27764835831'. Up to 15 digits allowed."
    )
    phone_num = models.CharField(validators=[phone_regex], max_length=20, default='')
    nationality = models.CharField(max_length=50)
    religion = models.CharField(max_length=95)
    marital_st = models.CharField(max_length=60)
    emp_spouse = models.CharField(max_length=70)
    num_child = models.CharField(max_length=80)

class EmergCon(models.Model):
    emerg_name = models.CharField(max_length=57, default='')
    emerg_rel = models.CharField(max_length=100, default='')
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+27764835831'. Up to 15 digits allowed."
    )
    phone_1 = models.CharField(validators = [phone_regex], max_length=20, default='')
    phone_2 = models.CharField(validators = [phone_regex], max_length=20, default='')

    em_name = models.CharField(max_length=57, default='')
    em_rel = models.CharField(max_length=100, default='')
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+27764835831'. Up to 15 digits allowed."
    )
    em_phone_1 = models.CharField(validators = [phone_regex], max_length=20, default='')
    em_phone_2 = models.CharField(validators = [phone_regex], max_length=20, default='')

class FamilyInfo(models.Model):
    fam_member_name = models.CharField(max_length=60, default='')
    fam_rel = models.CharField(max_length=67, default='')
    date_of_birth = models.DateField(auto_now_add=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+27764835831'. Up to 15 digits allowed."
    )
    fam_member_phone = models.CharField(validators= [phone_regex], max_length=15, default='')

class EducationInfo(models.Model):
    inst = models.CharField(max_length=80, default='')
    subject = models.CharField(max_length=70, default='')
    start_date = models.DateField(auto_now_add=True)
    compl_date = models.DateField(auto_now_add=True)
    qual_name = models.CharField(max_length=90, default='')
    grade = models.CharField(max_length=78, default='')

    sec_inst = models.CharField(max_length=80, default='')
    sec_subject = models.CharField(max_length=70, default='')
    sec_start_date = models.DateField(auto_now_add=True)
    sec_compl_date = models.DateField(auto_now_add=True)
    sec_qual_name = models.CharField(max_length=90, default='')
    sec_grade = models.CharField(max_length=78, default='')

class ExperienceInfo(models.Model):
    company_name = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=90, default='')
    job_position = models.CharField(max_length=90, default='')
    period_f = models.DateField(auto_now_add=True)
    period_t = models.DateField(auto_now_add=True)

    sec_company_name = models.CharField(max_length=100, default='')
    sec_location = models.CharField(max_length=90, default='')
    sec_job_position = models.CharField(max_length=90, default='')
    sec_period_f = models.DateField(auto_now_add=True)
    sec_period_t = models.DateField(auto_now_add=True)


class Documents(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/', default=None)
    course_name = models.CharField(max_length=255, null=True)
    institution = models.CharField(max_length=255, null=True)
    assign_month = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.file.name
    
class EmailVerificationToken(models.Model):
    token_id = models.AutoField(primary_key=True, default=None)
    email = models.EmailField(default=None)
    token = models.CharField(max_length=255, default=None)
    created_at = models.DateTimeField(auto_now_add=True)