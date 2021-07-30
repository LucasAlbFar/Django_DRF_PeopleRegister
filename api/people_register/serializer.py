from people_register.validator import *
from people_register.functions import *


class PersonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonType
        fields = '__all__'

    def create(self, validated_data):
        validated_data['person_type'] = upper_case(validated_data['person_type'])
        check_duplicate_person_type(validated_data)

        return PersonType.objects.create(**validated_data)


class PersonMediaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonMediaType
        fields = '__all__'
        read_only_fields = ('media_type',)


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        read_only_fields = ('id', 'last_update',)

    def validate(self, data):
        if not nome_valido(data['name']):
            raise serializers.ValidationError({'name': 'Name must contain alpha characters only'})

        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': 'Invalid CPF'})

        return data

    def create(self, validated_data):
        validated_data['id'] = id_generator()
        validated_data['name'] = upper_case(validated_data['name'])
        trigger_audit(validated_data)

        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if not cpf_valido(validated_data['cpf']):
            raise serializers.ValidationError({'cpf': 'Invalid CPF'})

        update_person_data(instance, validated_data)
        update_audit(instance, validated_data)

        Person.objects.update(**validated_data)
        return validated_data


class PersonMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonMedia
        fields = '__all__'
        read_only_fields = ('object_media',)


class PersonAuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonAudit
        fields = '__all__'


class ListPeopleSerializer(serializers.ModelSerializer):
    person_type = serializers.ReadOnlyField(source='person_type.person_type')

    class Meta:
        model = Person
        fields = '__all__'
