from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import School

class SchoolSerializer(ModelSerializer):
    emblem = SerializerMethodField()  # Explicitly handle the emblem field
    image1 = SerializerMethodField()  # Explicitly handle the image1 field

    class Meta:
        model = School
        fields = [
            'username', 'schoolname', 'telephone', 'schoolemail', 'schooladdress',
            'postal_address', 'website', 'slogan', 'emblem', 'type_of_school', 
            'umalusi', 'provinc', 'district', 'circuit', 'curriculum', 'grade_levels', 
            'local_municipality', 'urban_rural', 'ward_id', 'Eei_district', 
            'emis_number', 'examination_number', 'examination_centre', 
            'persal_paypoint_number', 'persal_component_number', 'name_of_principal', 
            'number_of_teachers', 'section_21', 'school_fees', 'quintile_Level', 
            'image1', 'history', 'mission'
        ]

    def get_emblem(self, obj):
        request = self.context.get('request')  # Get request from serializer context
        if obj.emblem:  # Ensure the emblem field is not None
            return request.build_absolute_uri(obj.emblem.url)
        return None  # Return None if the emblem is missing

    def get_image1(self, obj):
        request = self.context.get('request')  # Get request from serializer context
        if obj.image1:  # Ensure the image1 field is not None
            return request.build_absolute_uri(obj.image1.url)
        return None  # Return None if the image1 is missing
