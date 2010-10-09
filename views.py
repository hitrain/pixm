from mailpix.forms import Email
from django.shortcuts import render_to_response
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import hashlib, datetime
from django.http import HttpResponseRedirect

	
def proove(request):
		
		if 'email' in request.POST:
			form = Email({'email':request.POST['email']})
			if form.is_valid():
				message = request.POST['email']
		
				hashl = hashlib.md5()
				hashl.update(str(datetime.datetime.now()))
				x = len(message)*11
				image = Image.new('RGBA', (x,31))
				draw = ImageDraw.Draw(image)
				draw.text((10,10), message, fill='green')
				b = image.getbbox()
				image = image.crop((5,5,b[2]+5,b[3]+5))
				del draw
				d = hashl.hexdigest()
				image.save('C:/Python26/djcode/mysite/media/img/'+d+'.png', 'PNG')
				return render_to_response('pix.html', {'proove':message, 'img_link':d})
			else:
				
				return render_to_response ('mailpix.html', {'e':form})
		else:
			return render_to_response ('mailpix.html')