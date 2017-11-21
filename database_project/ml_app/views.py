# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views import generic
from .models import DataType, Task, Algorithm, DataTypeTask

# Create your views here.

class HomeView(generic.ListView):
	template_name='home.html'
	model = DataType
	context_object_name = 'data_types'
	
	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)

		context.update({
			'tasks': Task.objects.all(),
			'algorithms' : Algorithm.objects.all()

			})
		return context

	def get_query_set(self):
		return DataType.objects.all()


class DataTypeView(generic.ListView):
	model = DataType
	template_name = 'view_data_types.html'


class UpdateDataType(generic.UpdateView):
	model = DataType
	template_name = 'upadate_datatypes.html'
	fields = ['data']


class TaskView(generic.ListView):
	model = Task
	template_name = 'view_tasks.html' 


class UpdateTask(generic.UpdateView):
	model = Task
	template_name = 'update_tasks.html'
	fields = ['title']


class AlgView(generic.ListView):
	model = Algorithm
	template_name = 'view_algorithms.html'


class UpdateAlg(generic.UpdateView):
	model = Algorithm
	template_name = 'update_algorithms.html'
	fields = ['alg_title']


class DataTypeTaskView(generic.DetailView):
	model = DataTypeTask
	template_name = 'view_datatype_tasks.html'


class SearchView(generic.FormView):
	template_name = 'home.html'
	model = DataType

	

	def post(self, request, *args, **kwargs):
		form = request.POST 
		if DataType.objects.filter(data=form['select_term']).exists():
			searched = DataType.objects.get(data=form['select_term'])
			return redirect('results', pk=searched.id)


class ResultsView(generic.DetailView):
	template_name = 'search_results_page.html'
	model = DataType

	def get_context_data(self, **kwargs):
		context = super(ResultsView, self).get_context_data(**kwargs)

		results = DataTypeTask.objects.filter(data=self.get_object())

		algorithms_list = []
		for result in results:
			task = result.task
			algorithms = Algorithm.objects.filter(task=task)
			algorithms_list.append(algorithms)

		context['algorithms'] = algorithms_list
		return context
	










