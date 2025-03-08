import redis 
 
# Connect to the Redis server 
redis_host = 'myrediscache-ewccmb.serverless.apse1.cache.amazonaws.com' 
redis_port = 6379 
redis_password = None  # Add password if your Redis server requires authentication 
 
# Create a Redis client 
client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True) 
 
print(client) 
 
client.ping() 
print("successfully") 
# if client: 
#     print("connecetd") 
# else: 
#     print("erroer")# # Define the queue name 
#queue_name = 'my_queue' 
 
# Data to push into the queue 
data = '1' 
 
# Push data into the queue 
#client.lpush(queue_name, data) 
 
#print(f"Data '{data}' pushed to the queue '{queue_name}' successfully")
