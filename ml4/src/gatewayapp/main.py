#create api gateway app
from ensurepip import version
import httpx
from itertools import cycle
from fastapi import FastAPI
import consul
from gatewayapp.configurations.config import CONSUL_HOST, CONSUL_PORT
from fastapi import HTTPException
from fastapi import Request, Response

#create api gateway app
app = FastAPI(title="API Gateway", description="API Gateway for microservices", version="1.0.0")
#create consul client
consul_client = consul.Consul(host=CONSUL_HOST, 
                              port=CONSUL_PORT)

#create load balancer
LOAD_BALANCERS = {}
#routing table
ROUTING_TABLE = {
    ("POST", "payments"): "payment-service",
    ("GET", "payments"): "payment-service"
}
#create routing engine function
def route_engine(method: str, resource: str):
     route_key = (        
        method.upper().strip(),
        resource.lower().strip()
    )

     if route_key not in ROUTING_TABLE:
        raise HTTPException(
            status_code=404,
            detail=f"No route found for {method} /api/{resource}"
        )

     return ROUTING_TABLE[route_key]

def get_service_instance(service_name: str):
    index, services = consul_client.health.service(
        service=service_name,
        passing=True
    )

    instances = []

    for item in services:
        service = item["Service"]
        address = service["Address"]
        port = service["Port"]

        instances.append(f"http://{address}:{port}")

    if not instances:
        raise HTTPException(
            status_code=503,
            detail=f"No healthy instances found for {service_name}"
        )

    current_instances = LOAD_BALANCERS.get(service_name, {}).get("instances")

    if current_instances != instances:
        LOAD_BALANCERS[service_name] = {
            "instances": instances,
            "cycle": cycle(instances)
        }

    return next(LOAD_BALANCERS[service_name]["cycle"])


async def forward_request(
    service_url: str,
    resource: str,
    product_id: int,
    request: Request
):
    target_url = f"{service_url}/{resource}/{product_id}"

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=target_url,
            params=request.query_params,
            content=await request.body()
        )

    return Response(
        content=response.content,
        status_code=response.status_code,
        media_type=response.headers.get("content-type")
    )


@app.get("/")
def home():
    return {
        "message": "API Gateway running",
        "features": [
            
            "Routing engine abstraction",
            "Round-robin load balancing"
        ],
        "routes": {
            "create_payment": "POST /api/payments/{order_id}",
            "check_payments": "GET /api/payments}"
        }
    }


@app.post("/api/payments/{order_id}")
async def create_payment_gateway(
    order_id: int,
    request: Request
):
    service_name = route_engine("POST", "payments")
    service_url = get_service_instance(service_name)

    return await forward_request(
        service_url=service_url,
        resource="payments",
        product_id=order_id,
        request=request
    )



