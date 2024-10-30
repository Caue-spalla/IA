import pyaudio
import wave
import numpy as np
from scipy.fftpack import fft
import tkinter as tk
from tkinter import messagebox

CHUNK = 4096
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 96000
RECORD_SECONDS = 2

def gravar(nomeAudio):
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)


    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        data = np.array(np.frombuffer(data, dtype=np.int16)) * 2
        data = data.astype(np.int16).tobytes()
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()


    wf = wave.open(f"{nomeAudio}.wav", 'wb') 
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def fftAnalise(arquivoAudio):

    wf = wave.open(arquivoAudio, 'rb')
    data = wf.readframes(wf.getnframes())
    data = np.frombuffer(data, dtype=np.int16)


    fft_data = fft(data)


    psd = np.abs(fft_data) ** 2


    return psd

def compararAudio(psd1, psd2):

    similarity = np.corrcoef(psd1, psd2)[0, 1]


    return similarity

def gravarAudioBase():
    gravar("audioBase")
    global audioBase
    audioBase = fftAnalise('audioBase.wav')
    messagebox.showinfo("Sucesso", "Gravação de padrão concluída!")

def compararAudioMostrarResultado():
    gravar("Audio")
    Audio_psd = fftAnalise('Audio.wav')
    similarity = compararAudio(audioBase, Audio_psd)
    similarity_percentage = similarity * 100
    acerto_valor_label = tk.Label(janela, text=f"{similarity_percentage:.1f}%", font=("Arial", 16))
    acerto_valor_label.grid(row=4, column=1, padx=10, pady=10)

    if similarity > 0.5:
        messagebox.showinfo("Resultado", "Reconhecimento bem-sucedido!")
    else:
        messagebox.showinfo("Resultado", "Reconhecimento falhou!")

janela = tk.Tk()
janela.title("TTF Reconhecimento de voz")
titulo = tk.Label(janela, text="Reconhecimento de voz", font=("Arial", 16))
nome_label = tk.Label(janela, text="Aluno: Cauê Spalla Rovaron", font=("Arial", 12))
data_label = tk.Label(janela, text="Data: 22/08/2024", font=("Arial", 12))
gravar_button = tk.Button(janela, text="Gravar padrão", command=gravarAudioBase, width=15)
escutar_button = tk.Button(janela, text="Escutar amostra", command=compararAudioMostrarResultado, width=15)
acerto_label = tk.Label(janela, text="Acerto:", font=("Arial", 12))

titulo.grid(row=0, column=0, columnspan=2, pady=10)
nome_label.grid(row=1, column=0, columnspan=2, pady=5)
data_label.grid(row=2, column=0, columnspan=2, pady=5)
gravar_button.grid(row=3, column=0, pady=10)
escutar_button.grid(row=4, column=0, pady=10)
acerto_label.grid(row=3, column=1, padx=10, pady=10)



janela.mainloop()
