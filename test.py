# -*- coding: utf-8 -*- 
#!/usr/bin/python

import redis
from main import Leaderboard

def print_list(thing):
    for item in thing:
        print "--->",item
    print ""

def print_with_score(thing):
    for item in thing:
        print "--->",item[0],item[1]
    print ""

if __name__ == "__main__":
    """test"""
    topic = {
        "深入剖析 redis 数据结构 intset":10,
        "深入剖析 redis 事务机制":20,
        "深入剖析 redis 数据结构 skiplist":30,
        "深入剖析 redis 数据结构 redisObject":40,
        "深入剖析 redis 数据结构 dict":50,
        "redis 数据结构综述":60,
        "红黑树并没有我们想象的那么难(上)":70,
        "红黑树并没有我们想象的那么难(下)":100}

    lb = Leaderboard("127.0.0.1",6379,"hot-spot",0)
    for item,score in topic.iteritems():
        lb.addMember(item,score)

    print_with_score(lb.getWholeLeaderboard(True,True))

    print_list(lb.getLeaderboardByPage(3,2))

    print "红黑树并没有我们想象的那么难(下)'s ranking: ", \
            lb.getRankByMember("红黑树并没有我们想象的那么难(下)"),"\n"

    print "Test Leaderboard.addMember: ",lb.addMember("post-to-delete",1000),"\n"

    print_list(lb.getWholeLeaderboard())
    print "Test Leaderboard.delMember: ",lb.delMember("post-to-delete"),"\n"
    print_list(lb.getWholeLeaderboard())

    print "Test Leaderboard.incrScore: ",lb.incrScore("红黑树并没有我们想象的那么难(下)",100),"\n"
    print_list(lb.getWholeLeaderboard())