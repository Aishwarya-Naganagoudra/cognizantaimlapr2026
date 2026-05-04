#create transaction controller
from fastapi import APIRouter, HTTPException
router = APIRouter(prefix="/transactions/v1.0", tags=["transactions"])
from bankingapp.dtos.transaction_request import TransactionRequest  
from bankingapp.dtos.transaction_response import TransactionResponse
from bankingapp.services.transaction_service_impl import TransactionServiceImpl
transaction_service = TransactionServiceImpl()
@router.post("/", response_model=TransactionResponse)
async def create_transaction(transaction:TransactionRequest):
    try:
        created_transaction = await transaction_service.create_transaction(transaction)
        return created_transaction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.get("/{transaction_id}", response_model=TransactionResponse)
async def get_transaction(transaction_id:int):
    try:
        transaction = await transaction_service.get_transaction(transaction_id)
        return transaction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
@router.get("/",response_model=list[TransactionResponse])
async def get_all_transactions():
    try:
        transactions = await transaction_service.get_all_transactions()
        #print(transactions)
        return transactions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
@router.put("/", response_model=TransactionResponse)
async def update_transaction(transaction:TransactionRequest):
    try:
        updated_transaction = await transaction_service.update_transaction(transaction)
        return updated_transaction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.delete("/{transaction_id}")
async def delete_transaction(transaction_id:int):
    try:
        success = await transaction_service.delete_transaction(transaction_id)
        if success:
            return {"message": "Transaction deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Transaction not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))