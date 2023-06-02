import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import mediainfo
import logging
import os

logger = logging.getLogger(__name__)

# fileName = '../static/1723118684792018.ogg'
pathRoot = '../static/'

# def mediaInfo(pathFile = '../static/1723118684792018WEB.wav'):
#     info = mediainfo(pathFile)
#     print(info)

def ogg2wav(pathFile = ''):
    try:
        wfn = pathFile.replace('.ogg','.wav')
        audio = AudioSegment.from_ogg(pathFile)
        audio = audio.set_frame_rate(16000)
        audio.export(wfn, format='wav') 
        msgLog = 'Conversion Success'
        logger.info(msgLog)
        return msgLog
    except BaseException as error:
        msgLog = error
        logger.error(msgLog)
        return msgLog

def deleteAudio(id = ''):
    try:
        data = os.listdir(pathRoot)
        for i in data:
            if i.startswith(id):
                os.remove(f'{pathRoot}{i}')
        msgLog = 'Delete Success'
        logger.info(msgLog)
        return msgLog
    except BaseException as error:
        msgLog = error
        logger.error(msgLog)
        return msgLog

def textRecognition(id = ''):
    pathFile = f'{pathRoot}{id}.ogg'
    if os.path.exists(pathFile):
        logger.info(f'File Exist: {os.path.exists(pathFile)}')
        ogg2wav(pathFile)
        r = sr.Recognizer()
        with sr.AudioFile(pathFile.replace('.ogg','.wav')) as source:
            audio = r.record(source)
            try:
                text = r.recognize_google(audio, language = 'es-ES')
                msgLog = 'Recognition Success'
                logger.info(msgLog)
                deleteAudio(id)
                return [text, 1]
            except BaseException as error:
                deleteAudio(id)
                msgLog = 'Recognition Failed'
                logger.error(msgLog)
                return ['', 0]
    else:
        msgLog = 'Recognition Failed'
        logger.error(msgLog)
        deleteAudio(id)
        return msgLog

# print(textRecognition(id = '1723118684792018'))
