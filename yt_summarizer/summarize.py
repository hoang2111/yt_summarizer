from youtube_transcript_api import YouTubeTranscriptApi
import re
import ollama
from audio_extracter import case_of_no_transcript
import sys
from transcript_list import find_other_transcript


def summarizer(yt_link, video_title=""):
    extract = re.search(r"(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+)", yt_link)

    transcript = ""

    if extract:
        try:
            print("Valid YouTube link!")
            video_id = extract.group(1)
            # raw_transcript = YouTubeTranscriptApi.get_transcript(video_id)
            raw_transcript = find_other_transcript(video_id)
            for text in raw_transcript:
                transcript += f"{text['text']}\n"

        except Exception:
            print("Invalid YouTube link!")
            transcript = case_of_no_transcript(yt_link)
            print(transcript)
    else:
        return "Not a YouTube Link"

    # llama3.2 for summarization
    response = ollama.chat(
        model='llama3.2',
        messages=[{'role': 'user', 'content': f'Title: {video_title} \nSummarize this in the language of the text: \n{transcript}'}]
    )

    return response['message']['content']
