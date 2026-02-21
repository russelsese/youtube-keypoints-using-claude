#!/usr/bin/env python3
"""
Download YouTube video transcripts to timestamped text files.

Usage:
    python download_transcript.py <youtube_url>

Examples:
    python download_transcript.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
    python download_transcript.py https://youtu.be/dQw4w9WgXcQ
"""

import sys
import re
import os
from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi


ytt_api = YouTubeTranscriptApi()


def extract_video_id(url: str) -> str:
    """Extract video ID from various YouTube URL formats."""
    patterns = [
        r'(?:v=|/v/|youtu\.be/)([a-zA-Z0-9_-]{11})',
        r'^([a-zA-Z0-9_-]{11})$',  # Just the video ID
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    raise ValueError(f"Could not extract video ID from: {url}")


def format_timestamp(seconds: float) -> str:
    """Convert seconds to MM:SS format."""
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{minutes:02d}:{secs:02d}"


def download_transcript(url: str) -> str:
    """
    Download transcript from YouTube URL and save to file.

    Returns the path to the saved transcript file.
    """
    video_id = extract_video_id(url)

    # Fetch transcript
    transcript_list = ytt_api.fetch(video_id)

    # Format transcript with timestamps
    lines = []
    for entry in transcript_list:
        timestamp = format_timestamp(entry.start)
        text = entry.text.replace('\n', ' ')
        lines.append(f"[{timestamp}] {text}")

    formatted_transcript = '\n'.join(lines)

    # Create output directory if it doesn't exist
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'transcripts')
    os.makedirs(output_dir, exist_ok=True)

    # Generate filename with timestamp
    timestamp_str = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{video_id}_{timestamp_str}.txt"
    filepath = os.path.join(output_dir, filename)

    # Save transcript
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(formatted_transcript)

    return filepath


def main():
    if len(sys.argv) < 2:
        print("Usage: python download_transcript.py <youtube_url>")
        print("Example: python download_transcript.py https://www.youtube.com/watch?v=VIDEO_ID")
        sys.exit(1)

    url = sys.argv[1]

    try:
        filepath = download_transcript(url)
        print(f"Transcript saved to: {filepath}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error downloading transcript: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
