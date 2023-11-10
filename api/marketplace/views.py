from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer

# Create your views here.
@api_view(["GET"])
def get_all_transactions(request: HttpRequest):
    transactions = Transaction.objects.all()
    serializer = TransactionSerializer(transactions, many=True)

    return Response(serializer.data)

@api_view(["GET", "POST"])
def create_transaction(request: HttpRequest):
    data = request.data
    serializer = TransactionSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"Success": "The transaction was created successfully"}, status=201
        )
    else:
        return Response(serializer.errors, status=400)

@api_view(["GET"])
def get_transaction(request: HttpRequest, transaction_id: int):
    try:
        transaction = Transaction.objects.get(id=transaction_id)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)
    except Transaction.DoesNotExist:
        return Response({"Error": "The transaction does not exist"}, status=404)
    
@api_view(["DELETE"])
def delete_transaction(request: HttpRequest, transaction_id: int):
    try:
        transaction = Transaction.objects.get(id=transaction_id)
        transaction.delete()
        return Response(
            {"Success": "The transaction was deleted successfully"}, status=200
        )
    except Transaction.DoesNotExist:
        return Response({"Error": "The transaction does not exist"}, status=404)
    
@api_view(["GET", "PUT"])
def update_transaction(request: HttpRequest):
    transaction_id = request.data.get("transaction_id")
    try:
        transaction = Transaction.objects.get(id=transaction_id)
    except Transaction.DoesNotExist:
        return Response({"Error": "The transaction does not exist"}, status=404)
    
    if request.method == 'GET':
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"Success": "The transaction was updated successfully"}, status=200
            )
        else:
            return Response(serializer.errors, status=400)