---
name: download-transcript
description: Download a YouTube video transcript
argument-hint: "<youtube-url>"
allowed-tools: Bash, Read
---

# Download YouTube Transcript

Download a transcript from a YouTube video URL.

## Instructions

1. Run the download script:
   ```bash
   python download_transcript.py $ARGUMENTS
   ```

2. Report the transcript file path to the user

3. Suggest running `/process-transcript <filepath>` to analyze the transcript and generate chapter keypoints
