from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response

#def current_datetime(request):
	#now = datetime.datetime.now()
	#html = "<html><body>It is now %s.</body></html>" % now
	#return HttpResponse(html)
	
#def hours_ahead(request, offset):
	#offset = int(offset)
	#dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	#html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	#return HttpResponse(html)


def current_datetime(request):
	current_date = datetime.datetime.now()
	return render_to_response("current_datetime.html",locals())
	
def hours_ahead(request, offset):
	hour_offset = int(offset)
	next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
	return render_to_response("hours_ahead.html", locals())
	