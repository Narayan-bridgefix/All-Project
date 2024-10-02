from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name','org_id']
    
class Test(serializers.Serializer):
    number = serializers.IntegerField(required=True)
    bool = serializers.BooleanField(default=True)
    strin  = serializers.CharField(trim_whitespace=True,max_length=20,min_length=2,error_messages={'error':"asdf"})
    email  = serializers.EmailField(max_length=20, min_length=5, allow_blank=False)
    regex = serializers.RegexField("regex", max_length=None, min_length=None, allow_blank=False)
    slug=serializers.SlugField(max_length=50, min_length=None, allow_blank=False)
    url = serializers.URLField(max_length=200, min_length=None, allow_blank=False)
    uuid = serializers.UUIDField(format='hex_verbose')
    filepath = serializers.FilePathField(path='/', match=None, recursive=False, allow_files=True, allow_folders=False)
    ip = serializers.IPAddressField(protocol='both')
    int = serializers.IntegerField(max_value=100, min_value=10)
    float = serializers.FloatField(max_value=100, min_value=10)
    decimal = serializers.DecimalField(max_digits=3, decimal_places=2, coerce_to_string=True, max_value=1000, min_value=1)
    datetime = serializers.DateTimeField(format='iso-8601', input_formats=None, default_timezone=None)
    date = serializers.DateField(format=None, input_formats=None)
    time = serializers.TimeField(format=None, input_formats=None)
    duration = serializers.DurationField(max_value=None, min_value=None)
    choice = serializers.ChoiceField(choices=[("hello","test")])
    multic = serializers.MultipleChoiceField(choices=[("hello","test"),("1","val1")],required=True)
    fileup = serializers.FileField(max_length=None, allow_empty_file=False, use_url=False)
    scores = serializers.ListField(
   child=serializers.IntegerField(min_value=0, max_value=100)
)
    json=serializers.JSONField(binary=False)
    modified = serializers.HiddenField(default=10)