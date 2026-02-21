# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

YouTube Transcript Breakdown - Downloads YouTube transcripts and uses Claude Code skills to generate chapter breakdowns with keypoints.

## Workflow

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Download a transcript
/download-transcript https://youtube.com/watch?v=VIDEO_ID

# 3. Process the transcript
/process-transcript transcripts/VIDEO_ID_20240101_120000.txt
```

## Skills

- `/download-transcript <url>` - Download transcript from YouTube URL
- `/process-transcript <file>` - Analyze transcript and generate keypoints markdown

## Architecture

- `download_transcript.py` - Python script to fetch transcript via youtube-transcript-api
- `.claude/skills/` - Claude Code skills for the two-stage workflow
- `transcripts/` - Downloaded transcript .txt files (timestamped)
- `keypoints/` - Generated markdown files with chapters and keypoints

## File Naming

- Transcripts: `transcripts/{video_id}_{YYYYMMDD_HHMMSS}.txt`
- Keypoints: `keypoints/{video_id}_{YYYYMMDD_HHMMSS}_keypoints.md`
