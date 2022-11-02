import redis

r = redis.Redis(
    host='Ares',
    port=6379, 
    password='Emilita01')

print (r)


r.set('foo', 'bar')
value = r.get('foo')
print(value)