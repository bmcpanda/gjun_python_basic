import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

file_path = ('../game/')
file_name = ('1_sanpo_(Vocals).mp3')

y, sr = librosa.load(file_path + file_name)

f0, voiced_flag, voiced_probs = librosa.pyin(
    y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))
times = librosa.times_like(f0)


D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
fig, ax = plt.subplots()
img = librosa.display.specshow(D, x_axis='time', y_axis='fft_note', ax=ax)
ax.set(title='pYIN fundamental frequency estimation')
fig.colorbar(img, ax=ax, format="%+2.f dB")
ax.plot(times, f0, label='f0', color='cyan', linewidth=3)
ax.legend(loc='upper right')
plt.show()

# # 繪製波形圖
# plt.figure()
# librosa.display.waveshow(y, sr=sr)
# plt.title('waveform')
# plt.show()

amplitude_threshold = 0.0  # 根据需要调整阈值
# 将振幅小于阈值的部分置为零
y = np.where(np.abs(y) < amplitude_threshold, 0, y)

# 人聲頻率
min_freq = 128
max_freq = 1024

# 提取音调信息
voice_pitches, magnitudes = librosa.core.piptrack(
    y=y,
    sr=sr,
    fmin=min_freq, fmax=max_freq
)

# 聲音強度資訊
plt.figure(figsize=(10, 4))
s_db = librosa.amplitude_to_db(magnitudes, ref=np.max)
librosa.display.specshow(s_db, y_axis='fft_note', x_axis='time')
plt.colorbar()
plt.ylim([min_freq-30, max_freq+50])  # 用這行來強制限制頻率範圍
plt.title('Pitch track')
# plt.show()


# pitch資訊
plt.figure(figsize=(10, 4))
s_db = librosa.amplitude_to_db(voice_pitches, ref=np.max)
librosa.display.specshow(s_db, y_axis='fft_note', x_axis='time')
plt.ylim([min_freq-50, max_freq+50])  # 用這行來強制限制頻率範圍
plt.colorbar()
plt.title('Voice pitch track')
# plt.show()

# test = librosa.hz_to_midi(voice_pitches)
# print(voice_pitches, test, test.shape)
# # 計算短時距傅立葉變換
# S = np.abs(librosa.stft(y))

# voice_pitches, magnitudes = librosa.core.piptrack(
#     y=y,
#     sr=sampling_frequency,
#     fmin=fmin, fmax=fmax
# )

# # 繪製短時距傅立葉變換圖
# fig, ax = plt.subplots()
# img = librosa.display.specshow(
#     librosa.amplitude_to_db(S, ref=np.max),
#     y_axis='log', x_axis='time', ax=ax, fmax=2048)
# ax.set_title('Power spectrogram')
# fig.colorbar(img, ax=ax, format="%+2.0f dB")
# plt.show()
