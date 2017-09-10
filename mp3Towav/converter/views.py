from django.shortcuts import render
from django.core.files.base import ContentFile
from wsgiref.util import FileWrapper
from django.shortcuts import HttpResponse

import pydub

from pydub import AudioSegment

def index(request):
	return render(request, 'converter/home.html')

def upload_file(request):
	if request.method == "POST":
		#get the wav file that was uploaded by the user
		wavFile = request.FILES['wavFile']

		#create a space for the mp3 file in the FILES list in the Django server
		request.FILES['mp3File'] = wavFile

		#get the name of the wav file, get rid of the .wav part and append .mp3
		wavStr = request.FILES['wavFile'].name
		wavList = wavStr.split(".wav")
		mp3File = wavList[0] + ".mp3"

		#convert the wav file to mp3 and store it in the mp3 file space we made on the FILES list
		AudioSegment.from_wav(wavFile).export(request.FILES['mp3File'], format="mp3")

		#create a httpresponse to return the mp3 file to the user aka the file is downloaded onto the users computer
		response = HttpResponse(content=request.FILES['mp3File'], content_type='application/mp3')
		response['Content-Type'] = 'application/mp3'

		#make sure the file name will be the previous file name now ending in .mp3
		response['Content-Disposition'] = 'attachment; filename="%s"'%mp3File
		return response
	else:
		return render(request, 'converter/home.html')
