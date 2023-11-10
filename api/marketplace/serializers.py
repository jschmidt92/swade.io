from rest_framework.serializers import CharField, IntegerField, ModelSerializer
from .models import Transaction


class TransactionSerializer(ModelSerializer):
    item_id = IntegerField(required=False, allow_null=True)
    notes = CharField(required=False, allow_null=True)

    class Meta:
        model = Transaction
        fields = ['id', 'character', 'amount', 'transaction_type', 'item_type', 'item_id', 'notes', 'transaction_time']
