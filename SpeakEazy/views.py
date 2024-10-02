from django.shortcuts import render
from django.http import HttpResponse
from .models import VideoFile
import tensorflow as tf
from .sign_language_prediction import process_video
import os
from django.http import JsonResponse
from .my_test import method

def SpeakEazy(request):
    return render(request,'home.html')


def voice_to_text(request):
    context = {'include_link': True} 
    return render(request,'VoiceToText.html',context)

def text_to_voice(request):
    context = {'include_link': True} 
    return render(request,'Text to voice.html',context)

def gesture_to_text(request):
    context = {'include_link': False}
    if request.method == 'POST':
        video_file = request.FILES['video']
        video_file_instance = VideoFile(video_file=video_file)
        video_file_instance.save()

        # Call your custom function to process the video and get the prediction
        prediction = process_video(video_file_instance.video_file.path)

        # Return the prediction as a JSON response
        return JsonResponse({'prediction': prediction})
    context = {'include_link': False}
    return render(request,'Gesture to Text.html',context)

def gesture_to_voice(request):
    context = {'include_link': True} 
    return render(request,'GestureToVoice.html',context)

def notepad(request):
    context = {'include_link': True}
    return render(request,'notepad.html',context)



def upload_video(request):
    context = {'include_link': False}

    if request.method == 'POST':
        video_file = request.FILES['video']
        video_file_instance = VideoFile(video_file=video_file)
        video_file_instance.save()

        # Call your custom function to process the video and get the prediction
        prediction = process_video(video_file_instance.video_file.path)
        if os.path.exists(video_file_instance.video_file.path):
            os.remove(video_file_instance.video_file.path)
        # Return the prediction as a JSON response
        return JsonResponse({'prediction': prediction})

    return render(request, 'upload_video.html', context)


def live(request):
    if request.method == 'POST':
        method()  # Call the method
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'}, status=400)