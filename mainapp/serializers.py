from rest_framework import serializers
from mainapp.models import *


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("name", "description", "price")

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("user", "phone", "salary", "role")

class RTVResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RTVResource
        fields = ("SKU", "owner", "creationDate", "duaration", "campaign")

class NonTVResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonTVResource
        fields = ("SKU", "owner", "type", "formfactor", "campaign")


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ("name", "morningTimePrice", "afternoonTimePrice", "eveningTimePrice", "nightTimePrice", "primeTimePrice")


class AdvertisingPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisingPlace
        fields = ("name", "type", "town", "avrPrice")

class BroadcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broadcast
        fields = ("period", "times", "startDate", "endDate", "price", "channel", "tvResource")

class PublishedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Published
        fields = ("month", "year", "amount", "price", "nonTVResourse", "advertisingPlace")


class CampaignSerializer(serializers.ModelSerializer):
    # service = serializers.SlugRelatedField(many=True, slug_field='id',read_only=True)
    class Meta:
        model = Campaign
        fields = ("id", "description", "subject", "paymentDetails", "signDate", "startDate", "endDate", "moneySpent", "plannedBudget", "state", "lastUpdateDate", "client", "employee", "service")

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ("report", "date", "campaign", "employee")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( "username", "password", "email", "first_name", "last_name")
        extra_kwargs = {'password': {'write_only': True}, }


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model= Client
        fields = ("edrpou", "contactPersone", "phone", "address", "activity", "user")

    def create(self, validated_data):

        user_data = validated_data.pop('user')
        user = User(username=user_data["username"], email=user_data["email"], first_name=user_data["first_name"], last_name=user_data["last_name"] )
        user.set_password(user_data["password"])
        user.save()
        client = Client.objects.create(user=user, **validated_data)
        return client