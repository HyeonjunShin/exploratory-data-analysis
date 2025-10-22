import pandas as pd
import librosa
import matplotlib.pyplot as plt
import numpy as npRR


def laod_sample_data():
    wave, sr = librosa.load(librosa.ex('nutcracker')) # sr: sampling rate
    return wave, sr
    

def main():
    wave, sr = laod_sample_data()
    plt.figure(figsize=(12, 4))

    # print(range(0,wave.size) / sr)
    print(wave)
    print(wave.size)
    print(wave.size/sr)
    print(wave)
    print(sr)
    # plt.plot(range(0,wave.size), wave)
    librosa.display.waveshow(wave, sr=sr)
    plt.title('Waveform (Raw Audio Data)')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.grid(True) # 그리드(격자) 표시
    plt.show()


if __name__ == "__main__":
    main()