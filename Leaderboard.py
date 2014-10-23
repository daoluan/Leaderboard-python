# -*- coding: utf-8 -*- 
#!/usr/bin/python

import redis

class Leaderboard:
    def __init__(self,host,port,key,db):
        self.host = host
        self.port = port
        self.key = key
        self.db = db
        self.r = redis.StrictRedis(host=self.host,port=self.port,db=self.db)

    def isRedisValid(self):
        return self.r is None

    def addMember(self,member,score):
        if self.isRedisValid():
            return None

        return self.r.zadd(self.key,score,member)

    def delMember(self,member):
        if self.isRedisValid():
            return None

        return self.r.zrem(self.key,member)

    def incrScore(self,member,increment):
        """increase score on specified member"""
        if self.isRedisValid():
            return None

        return self.r.zincrby(self.key,member,increment)

    def getRankByMember(self,member):
        """Get ranking by specified member."""
        if self.isRedisValid():
            return None

        return self.r.zrank(self.key,member)

    def getLeaderboard(self,start,stop,reverse,with_score):
        """Return the whole leaderboard."""
        if self.isRedisValid():
            return None

        return self.r.zrange(self.key,start,stop,reverse,with_score)

    def getLeaderboardByPage(self,item_per_page,page_num,reverse=False,with_score=False):
        """Return part of leaderboard configurably."""
        # fix parameters
        if item_per_page <= 0:
            item_per_page = 5
        if page_num <= 0:
            page_num = 1

        # note: it is possible that return value is empty list.
        return self.getLeaderboard((page_num-1)*item_per_page,
                                                        page_num*item_per_page-1,
                                                        reverse,with_score)

    def getWholeLeaderboard(self,reverse=False,with_score=False):
        """Return the whole leaderboard."""
        return self.getLeaderboard(0,-1,reverse,with_score) 