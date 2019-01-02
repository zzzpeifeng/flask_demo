from redis import StrictRedis
from rediscluster import *


sr = StrictRedis(decode_responses=True)
sr.hset("a4","name","lihaibo")
sr.set("name","zpf")
print(sr.hget("a4","name"))
print(sr.keys("*"))
