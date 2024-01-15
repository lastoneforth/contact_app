from django.test import TestCase
import pytest
from app.models import Contacts
from app.views import index
from django.urls import reverse, resolve
from django.test import RequestFactory
# Create your tests here.


@pytest.mark.django_db
def test_contact_create():
    # Create dummy data
    contact = Contacts.objects.create(full_name="Muhammed Ali", phone_number="75859538350", )
    # Assert the dummy data saved as expected
    assert contact.full_name == "Muhammed Ali"
    assert contact.phone_number == "75859538350"


@pytest.mark.django_db
def test_index():
    request = RequestFactory().get('')
    response = index(request)
    assert response.status_code == 200


