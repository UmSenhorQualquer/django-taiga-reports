import os, time
from taiga import TaigaAPI
from django.shortcuts import render_to_response
from django.conf import settings

from taiga_reports.report import Report
from taiga_reports.user_report import UserReport



# Create your views here.
def index(request):
	folder = settings.TAIGA_DATA_FOLDER
	directories = [os.path.join(folder,o) for o in os.listdir(folder) if os.path.isdir(os.path.join(folder,o))]

	
	report = Report(settings.TAIGA_DATA_FOLDER)

	status_points_filename = os.path.join(settings.MEDIA_ROOT,'status_points_{0}.png'.format(int(time.time()))  ) 
	status_count_filename = os.path.join(settings.MEDIA_ROOT,'status_count_{0}.png'.format(int(time.time())) ) 
	tags_points_filename = os.path.join(settings.MEDIA_ROOT,'tags_points_{0}.png'.format(int(time.time())) ) 
	tags_count_filename = os.path.join(settings.MEDIA_ROOT,'tags_count_{0}.png'.format(int(time.time())) ) 
	
	report.save_status_points_graph( status_points_filename )
	report.save_status_counts_graph( status_count_filename )
	report.save_tags_points_graph( tags_points_filename )
	report.save_tags_counts_graph( tags_count_filename )

	closed_status_points_filename 	= os.path.join(settings.MEDIA_ROOT,'status_points_{0}.png'.format(int(time.time()))  ) 
	closed_status_count_filename 	= os.path.join(settings.MEDIA_ROOT,'status_count_{0}.png'.format(int(time.time())) ) 
	closed_tags_points_filename 	= os.path.join(settings.MEDIA_ROOT,'tags_points_{0}.png'.format(int(time.time())) ) 
	closed_tags_count_filename  	= os.path.join(settings.MEDIA_ROOT,'tags_count_{0}.png'.format(int(time.time())) ) 
	
	report.save_status_points_graph( closed_status_points_filename,  closed=True )
	report.save_status_counts_graph( closed_status_count_filename,   closed=True )
	report.save_tags_points_graph( 	 closed_tags_points_filename, 	 closed=True )
	report.save_tags_counts_graph( 	 closed_tags_count_filename, 	 closed=True )

	
	api = TaigaAPI()
	api.auth(username=settings.USER, password=settings.PASS)

	workload_imgs 	= []
	last_moment 	= report.last_moment

	for user_id in settings.TEAM:
		user = api.users.get(user_id)

		user_report 		= UserReport(user_id, last_moment)
		workload_filename 	= os.path.join(settings.MEDIA_ROOT,'workload_{1}_{0}.png'.format(int(time.time()), user_id) ) 
	
		user_report.save_workload_4_next_days_graph(workload_filename, settings.TAGS_PRIORITIES)


		username = (user.full_name if user.full_name!='' else user.username)
		workload_imgs.append( (username, workload_filename) )

	data = {
		'status_points_filename': 	status_points_filename,
		'status_count_filename': 	status_count_filename, 
		'tags_points_filename':		tags_points_filename,
		'tags_count_filename':		tags_count_filename,
		'closed_status_points_filename': 	closed_status_points_filename,
		'closed_status_count_filename': 	closed_status_count_filename, 
		'closed_tags_points_filename':		closed_tags_points_filename,
		'closed_tags_count_filename':		closed_tags_count_filename,
		'workload_images':		workload_imgs,
		'not_assigned_stories': last_moment.not_assigned_stories()
	}

	template_directory = os.path.dirname(os.path.realpath(__file__))
	template_file = os.path.join(template_directory, 'templates', 'index.html')
	return render_to_response(template_file, data)