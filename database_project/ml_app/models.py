# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class DataType(models.Model):
	data = models.CharField(max_length=255)

	def __unicode__(self):
		return self.data 
	

class Task(models.Model):
	title = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.title 


class Algorithm(models.Model):
	alg_title = models.CharField(max_length=255)
	task = models.ForeignKey(Task, related_name='algorithms', null=True)

	def __unicode__(self):
		return self.alg_title 


class DataTypeTask(models.Model):	
	data = models.ForeignKey(DataType)
	task = models.ForeignKey(Task) 

	def __unicode__(self):
		return self.data.data