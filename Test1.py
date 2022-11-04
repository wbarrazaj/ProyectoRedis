import redis

r = redis.Redis(
    host='localhost',
    port=6379, 
    password='')

print (r)

r.set('foo', 'Wilson Barraza')
value = r.get('foo')
print(value)
print("Hola")

"""
./System/Volumes/Data/opt/homebrew/etc/redis.conf
./System/Volumes/Data/opt/homebrew/Cellar/redis/7.0.5/.bottle/etc/redis.conf
"""

