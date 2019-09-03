from django.db import models


FT_CHOICES = (('primary','primary'),('mandatory','mandatory'),('optional','optional'))

DT_CHOICES = (

	('text','TextField'),
	('date','DateField'),('datetime','DateTimeField'),('image','ImageField'),
	('email','EmailField'),('file','FileField'),('number','IntegerField'),
	('textarea','TextAreaField'),
	('time','TimeField'),('url','URLField'),('select','SelectDropDownField')
    )
    
PD_CHOICES = DOC_CHOICES=(('Passport','Passport'),('Driving licence','Driving licence'),
('VoterID','VoterID'),('PAN Card','PAN Card'),('Aadhar Card','Aadhar Card'),
('NREGA job card','NREGA job card'),('rental agreement','rental agreement'),
('utility bill','utility bill'),('PPOs','PPOs'),
('Municipal tax receipt','Municipal tax receipt'),('birth certificate','birth certificate'),
('social security card','social security card'),('ration card','ration card'),
('SalesTax Registration Certificate','SalesTax Registration Certificate'),
('SEBI Registration Certificate','SEBI Registration Certificate'),('Form 18 & ROC Receipt','Form 18 & ROC Receipt'),
('CDC and Mariner Declaration','CDC and Mariner Declaration'),('Notarized GPO','Notarized GPO'),
('MoA/AoA','MoA/AoA'),('Annual return copy with ROC','Annual return copy with ROC'),('form 32','form 32'),
('current bank statements','current bank statements'),("Employer's issued Photo ID","Employer's issued Photo ID"),
('Credit card statements','Credit card statements'),('RV report','RV report'),
('Medical Insurance Policy','Medical Insurance Policy'),('Pan Intimation Letter','Pan Intimation Letter'),
('Factory Registration Certificate','Factory Registration Certificate'),('Shop and Establishment Certificate','Shop and Establishment Certificate'),('school leaving certificate','school leaving certificate'),
('10th/12th/(pg/ug)certificate','10th/12th/(pg/ug)certificate'),('Form 60','Form 60'),('sales and income tax returns','sales and income tax returns'),('GIR No','GIR No'),('Income Tax exemption letter','Income Tax exemption letter'),('Certificate of Incorporation','Certificate of Incorporation'),('Income Tax registration u/s 12','Income Tax registration u/s 12'),('FATCA Declaration','FATCA Declaration'),('Certificate of commencement of busines','Certificate of commencement of busines'),('Memorandum & Articles of Association','Memorandum & Articles of Association'),('Trust deed /Bye-Laws/ Constitutional Document','Trust deed /Bye-Laws/ Constitutional Document'),('National Population Registered letter','National Population Registered letter'),('bank passbook','bank passbook'),('CST/VAT/GST certificate','CST/VAT/GST certificate'),
('Self Declare','Self Declare'))

FT_CONSTRAINT_CHOICES = (('^[A-Za-z ]+$','only alpha'),
                ('([A-z0-9À-ž\s]){3,}','alpha numeric'),('^\d$','number'),
                ("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$","email contraint"),
                ('^\d{10}$','phone number (10 digits)'),('genderSelect','GenderSelect'),
                ('dob_constraint','DOB constraint'),('None','None'))

class Policy(models.Model):
    policy_name = models.CharField(max_length=50)
    policy_description = models.TextField()
    
    def __str__(self):
       return self.policy_name
    

class PolicyField(models.Model):
    policy = models.ForeignKey(Policy,on_delete=models.CASCADE,)
    name = models.CharField(max_length=100)
    meta = models.CharField(choices=FT_CHOICES,max_length=60)
    datatype = models.CharField(choices=DT_CHOICES,max_length=60)
    pattern = models.CharField(choices=FT_CONSTRAINT_CHOICES,max_length=100,help_text='select data validations')
    proof  = models.CharField(choices=PD_CHOICES,max_length=60,blank=True,null=True)
    message = models.CharField(max_length=256)
    def __str__(self):
        return self.name

