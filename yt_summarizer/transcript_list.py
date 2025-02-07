import sys

from youtube_transcript_api import YouTubeTranscriptApi


# retrieve the available transcripts
def find_other_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    for transcript in transcript_list:
        print(transcript.language)
        return transcript.fetch()
