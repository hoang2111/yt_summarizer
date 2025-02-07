import yt_dlp
import whisper


def case_of_no_transcript(video_url):
    # download audio in case of no sub
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': 'audio.%(ext)s'  # Save as 'audio.wav'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    # speech_to_text
    model = whisper.load_model("base")
    result = model.transcribe("audio.wav")
    return result["text"]
