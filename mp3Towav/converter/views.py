from django.shortcuts import render
from django.core.files.base import ContentFile
from wsgiref.util import FileWrapper
from django.shortcuts import HttpResponse
import pydub

def index(request):
	return render(request, 'converter/home.html')

def upload_file(request):
	if request.method == "POST":
		wavFile = request.FILES['wavFile']
		input = audiotools.open(wavFile)

		#sound = pydub.AudioSegment.from_wav(wavFile)
		wavStr = request.FILES['wavFile'].name
		wavFile = wavStr.split(".wav")
		mp3File = wavFile[0] + ".mp3"

		#newFile = sound.export(mp3File, format="mp3")
		response = HttpResponse(input.convert((mp3File), 
                    audiotools.MP3Audio,
                    compression=audiotools.MP3Audio.COMPRESSION_MODES[10],
                    progress=progress), content_type='application/mp3')
		response['Content-Disposition'] = 'attachment; filename=myfile.mp3'
		return response
	else:
		return render(request, 'converter/home.html')