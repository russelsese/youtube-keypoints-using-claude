# YouTube Transcript Breakdown

A Claude Code project that downloads YouTube transcripts and generates structured chapter breakdowns with keypoints, lessons, stories, and examples — powered by Claude AI.

## Features

- Download transcripts from any YouTube video with captions
- Automatically identify chapters based on topic shifts
- Extract keypoints, lessons, stories, and examples per chapter
- Output clean, structured markdown files

## Requirements

- Python 3.7+
- [Claude Code](https://claude.ai/code) CLI

## Setup

```bash
pip install -r requirements.txt
```

## Usage

### Option A: Full workflow in one command

```bash
/transcript https://www.youtube.com/watch?v=VIDEO_ID
```

This downloads the transcript and generates the keypoints file in a single step.

### Option B: Two-step workflow

```bash
# Step 1 — Download the transcript
/download-transcript https://www.youtube.com/watch?v=VIDEO_ID

# Step 2 — Analyze and generate keypoints
/process-transcript transcripts/VIDEO_ID_YYYYMMDD_HHMMSS.txt
```

## Output

| Type | Location | Format |
|------|----------|--------|
| Transcripts | `transcripts/` | `{video_id}_{YYYYMMDD_HHMMSS}.txt` |
| Keypoints | `keypoints/` | `{video_id}_{YYYYMMDD_HHMMSS}_keypoints.md` |

### Keypoints file structure

Each generated markdown file contains:

```
## Chapter 1: [Topic Name]
Timestamp: [start] - [end]

- Keypoint 1
- Keypoint 2
- Keypoint 3

**Lessons**
- ...

**Stories**
- ...

**Examples**
- ...

---

## Summary
[2-3 sentence summary of the full video]
```

## Project Structure

```
youtube-transcript-breakdown/
├── download_transcript.py      # Fetches transcript via youtube-transcript-api
├── requirements.txt
├── transcripts/                # Downloaded .txt transcript files
├── keypoints/                  # Generated .md keypoints files
└── .claude/skills/
    ├── download-transcript/    # /download-transcript skill
    ├── process-transcript/     # /process-transcript skill
    └── transcript/             # /transcript (combined) skill
```
