#!/usr/bin/env python3

###############################################################################
# Module Imports
###############################################################################

import peewee

###############################################################################
# Global Constants
###############################################################################

DBPATH = "/home/anqxyr/heap/_scp/scp-wiki.2014-12-13.db"

###############################################################################
# Database ORM Classes
###############################################################################

db = peewee.SqliteDatabase(DBPATH)


class BaseModel(peewee.Model):

    class Meta:
        database = db


class Page(BaseModel):
    pageid = peewee.IntegerField(primary_key=True)
    url = peewee.CharField(unique=True)
    html = peewee.TextField()
    thread_id = peewee.IntegerField(null=True)


class Revision(BaseModel):
    pageid = peewee.IntegerField(index=True)
    number = peewee.IntegerField()
    user = peewee.CharField(index=True)
    time = peewee.DateTimeField()
    comment = peewee.CharField()


class Vote(BaseModel):
    pageid = peewee.IntegerField(index=True)
    user = peewee.CharField(index=True)
    vote = peewee.IntegerField()


class ForumPost(BaseModel):
    post_id = peewee.IntegerField(primary_key=True)
    thread_id = peewee.IntegerField(index=True)
    title = peewee.CharField()
    content = peewee.TextField()
    user = peewee.CharField(index=True)
    time = peewee.DateTimeField()
    parent = peewee.CharField(null=True)


class Image(BaseModel):
    url = peewee.CharField(unique=True)
    source = peewee.CharField()
    data = peewee.BlobField()
    # for future use:
    #status = peewee.CharField()


class Author(BaseModel):
    url = peewee.CharField(unique=True)
    author = peewee.CharField()
    override = peewee.BooleanField()


class Tag(BaseModel):
    tag = peewee.CharField(index=True)
    url = peewee.CharField()
