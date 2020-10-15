import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate


frecuenciaSegmento = SinSignal(freq=600, amp=1, offset=0)
frecuenciaLetras = SinSignal(freq=1450, amp=1, offset=0)
frecuenciaL = SinSignal(freq=1300, amp=1, offset=0)
frecuenciaO = SinSignal(freq=1600, amp=1, offset=0)
frecuenciaG = SinSignal(freq=800, amp=1, offset=0)
frecuenciaR = SinSignal(freq=1900, amp=1, offset=0)
frecuenciaA = SinSignal(freq=200, amp=1, offset=0)
frecuenciaD = SinSignal(freq=500, amp=1, offset=0)

#para el Segmento
wave_Segmento = frecuenciaSegmento.make_wave(duration=0.4, start=0, framerate=44100)

#para la cantidad de letras
wave_Letras = frecuenciaLetras.make_wave(duration=0.4, start=0.4, framerate=44100)

#L
wave_L = frecuenciaL.make_wave(duration=0.4, start=0.8, framerate=44100)

#O
wave_O = frecuenciaO.make_wave(duration=0.4, start=1.2, framerate=44100)

#G
wave_G = frecuenciaG.make_wave(duration=0.4, start=1.6, framerate=44100)

#R
wave_R = frecuenciaR.make_wave(duration=0.4, start=2, framerate=44100)

#A
wave_A = frecuenciaA.make_wave(duration=0.4, start=2.4, framerate=44100)

#D
wave_D = frecuenciaD.make_wave(duration=0.4, start=2.8, framerate=44100)

#O2
wave_O2 = frecuenciaO.make_wave(duration=0.4, start=3.2, framerate=44100)


wave_audio = wave_Segmento + wave_Letras + wave_L + wave_O + wave_G + wave_R + wave_A + wave_D + wave_O2

wave_audio.write("audio.wav")