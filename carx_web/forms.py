from django import forms
from django.contrib.auth import authenticate
from carx_drf.models import Vehicle, Maker, Makermodel


class loginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control form-login' , 'placeholder':'Username','autocomplete': 'off'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control form-login ', 'placeholder':' Password','autocomplete': 'off'}))

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class VehicleForm(forms.ModelForm):
    FUEL_TYPE = (
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('CNG', 'CNG'),
        ('LPG', 'LPG'),
    )

    TRANSMITION = (
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),

    )
    VEHICLE_TYPE = (
        ('4 Wheeler', '4 Wheeler'),
        ('2 Wheeler', '2 Wheeler'),
        ('Commercial', 'Commercial'),
    )

    SUSPENSION_TYPE = (
        ('Front', 'Front'),
        ('Rear', 'Rear'),
    )
    BREAKS_TYPE = (
        ('Front', 'Front'),
        ('Rear', 'Rear'),
    )
    STEERING_TYPE = (
        ('Power', 'Power'),
        ('Regular', 'Regular'),
    )

    vehicle_type = forms.CharField(required=True, widget=forms.Select(choices=VEHICLE_TYPE, attrs={'class': 'form-control'}))
    make = forms.ModelChoiceField(queryset=Maker.objects.all(), required=True, widget=forms.Select(attrs={'class':'form-control' , 'placeholder':'Car Maker', 'autocomplete': 'off'}))
    model = forms.ModelChoiceField(queryset=Makermodel.objects.all(), required=True, widget=forms.Select(attrs={'class':'form-control' , 'placeholder':'Car Model', 'disabled': True}))
    segment = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Segment', 'autocomplete': 'off'}))
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vehicle name', 'autocomplete': 'off'}))
    verient = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Veriemt', 'autocomplete': 'off'}))
    fuletype = forms.CharField(required=True, widget=forms.Select(choices=FUEL_TYPE, attrs={'class':'form-control' , 'placeholder':'Car Model', 'autocomplete': 'off'}))
    engine = forms.CharField(required=True, widget=forms.TextInput(attrs={'autocomplete': 'on', 'class': 'form-control decimal', 'placeholder':'Engine'}))
    power = forms.CharField(required=True, widget=forms.TextInput(attrs={'autocomplete': 'on', 'class': 'form-control number', 'placeholder':'Power'}))
    capacity = forms.CharField(required=True, widget=forms.TextInput(attrs={'autocomplete': 'on', 'class': 'form-control decimal', 'placeholder':'Capacity'}))
    output = forms.CharField(required=True, widget=forms.TextInput(attrs={'autocomplete': 'on', 'class': 'form-control number', 'placeholder':'Max output'}))
    torque = forms.CharField(required=True, widget=forms.TextInput(attrs={'autocomplete': 'on', 'class': 'form-control', 'placeholder':'Torque'}))
    transmission_type = forms.CharField(required=True, widget=forms.Select(choices=TRANSMITION, attrs={'autocomplete': 'on', 'class': 'form-control'}))
    transmission = forms.CharField(required=True, widget=forms.TextInput(attrs={'autocomplete': 'on', 'class': 'form-control', 'placeholder':'Transmision'}))
    weight = forms.FloatField(required=True, widget=forms.TextInput(attrs={'autocomplete': 'off', 'class': 'form-control decimal', 'placeholder':'Weight in Kg'}))
    height = forms.FloatField(required=True, widget=forms.TextInput(attrs={'autocomplete': 'off', 'class': 'form-control decimal', 'placeholder': 'Height'}))
    suspensiontype = forms.CharField(required=True, widget=forms.Select(choices=SUSPENSION_TYPE, attrs={'class': 'form-control'}))
    startdate = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    enddate = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    fueltank = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fuel Tank capacity'}))
    ground_clearance = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control number', 'placeholder':'Ground Clearance'}))
    breaks = forms.CharField(widget=forms.Select(choices=BREAKS_TYPE, attrs={'class': 'form-control', 'placeholder':'Breaks'}))
    steering = forms.CharField(widget=forms.Select(choices=STEERING_TYPE, attrs={'class': 'form-control'}))
    length = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control decimal', 'placeholder':'Lenght'}))
    width = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control decimal', 'placeholder':'Width'}))
    type_and_wheel = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Type and wheel'}))
    turning_radius = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control number', 'placeholder':'Turning radius'}))
    mileage = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control decimal', 'placeholder': 'Mileage per Km'}))
    scaling = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Scaling'}))

    class Meta:
        model = Vehicle
        fields = ['make', 'name', 'model', 'segment', 'verient', 'height', 'mileage', 'ground_clearance', 'breaks', 'scaling', 'length', 'width', 'type_and_wheel', 'turning_radius', 'fuletype', 'weight', 'fueltank', 'transmission', 'startdate', 'suspensiontype','image', 'enddate', 'transmission_type', 'torque', 'output', 'capacity', 'power', 'engine', 'vehicle_type']
