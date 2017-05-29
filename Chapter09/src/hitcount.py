import redis

r = redis.StrictRedis(host='0.0.0.0', port=6379, db=0)

def hit(key):
    r.incr(key)

def getHit(key):
    return (r.get(key))
