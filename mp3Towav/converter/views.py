from django.shortcuts import render
from django.core.files.base import ContentFile
from wsgiref.util import FileWrapper
from django.shortcuts import HttpResponse
from django.template import loader

import pydub

from pydub import AudioSegment

def index(request):
	return render(request, 'converter/home.html')

def upload_file(request):
	if request.method == "POST":
		#get the wav file that was uploaded by the user

		if len(request.FILES) != 0:
			wavFile = request.FILES['wavFile']

			#create a space for the mp3 file in the FILES list in the Django server
			request.FILES['mp3File'] = wavFile

			#get the name of the wav file, get rid of the .wav part and append .mp3
			wavStr = request.FILES['wavFile'].name

			listCheck = wavStr.split(".")

			if listCheck[1] != "wav":
				return render(request, 'converter/home.html', {'check': 'Please Choose a .WAV File'})
			else:
				wavList = wavStr.split(".wav")
				mp3File = wavList[0] + ".mp3"

				#convert the wav file to mp3 and store it in the mp3 file space we made on the FILES list
				AudioSegment.from_wav(wavFile).export(request.FILES['mp3File'], format="mp3")

				#create a httpresponse to return the mp3 file to the user aka the file is downloaded onto the users computer
				response = HttpResponse(content=request.FILES['mp3File'], content_type='application/mp3')
				response['Content-Disposition'] = 'attachment; filename="%s"'%mp3File
				return response
		else:
			return render(request, 'converter/home.html', {'check': 'Please Choose a .WAV File'})
	else:
		return render(request, 'converter/home.html')