#create transaction service implementation from transaction service abstract class
import json

from fastapi.encoders import jsonable_encoder

from bankingapp.dtos.transaction_request import TransactionRequest
from bankingapp.dtos.transaction_response import TransactionResponse
from bankingapp.repositories.transaction_repo_impl import TransactionRepoImpl
from bankingapp.services.transaction_service import TransactionService
from fastapi import Depends
from bankingapp.configurations.redis_client import RedisClient
class TransactionServiceImpl(TransactionService):
    def __init__(self):
        self.transaction_repo = TransactionRepoImpl()
        #create redis client instance and assign to self.redis_client
        self.redis_client = RedisClient().client

    
    async def create_transaction(self, transaction:TransactionRequest)->TransactionResponse:
        return await self.transaction_repo.create_transaction(transaction)
    
    async def get_transaction(self, transaction_id:int)->TransactionResponse:
        
         return await self.transaction_repo.get_transaction_by_id(transaction_id)

              
    
    async def get_all_transactions(self)->list[TransactionResponse]:         
        cache_key = "transactions:all"
        # 1. Check Redis
        cached_data = await self.redis_client.get(cache_key)
        if cached_data is not None:
            print("CACHE HIT") 
            return json.loads(cached_data)
        if cached_data is None:
           print("CACHE MISS")
         # 2. Fetch DB
           transactions = await self.transaction_repo.get_all_transactions()

         # 3. Convert Pydantic objects to JSON-safe data
           transactions_data = jsonable_encoder(transactions)

         # 4. Save to Redis
           await self.redis_client.set(
                cache_key,
                json.dumps(transactions_data),
                ex=60
            )
           return transactions_data
         
    
    async def update_transaction(self, transaction:TransactionRequest)->TransactionResponse:
        return await self.transaction_repo.update_transaction(transaction)
    
    async def delete_transaction(self, transaction_id:int)->bool:
        return await self.transaction_repo.delete_transaction(transaction_id)