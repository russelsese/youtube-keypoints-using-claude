---
name: transcript
description: Download YouTube transcript and generate chapter breakdown with keypoints
argument-hint: "<youtube-url>"
allowed-tools: Bash, Read, Write, Glob
---

# YouTube Transcript Workflow

Download a transcript from YouTube and generate a chapter breakdown with keypoints in a single workflow.

## Instructions

### Stage 1/4: Downloading transcript

1. Output: **Stage 1/4: Downloading transcript...**

2. Run the download script:
   ```bash
   python download_transcript.py $ARGUMENTS
   ```

3. Capture the transcript filepath from the output

4. Output: ✓ Transcript downloaded

### Stage 2/4: Reading transcript

1. Output: **Stage 2/4: Reading transcript...**

2. Read the downloaded transcript file using the filepath from Stage 1

3. Output: ✓ Transcript loaded ([X] characters)

### Stage 3/4: Analyzing content and generating chapters

1. Output: **Stage 3/4: Analyzing content and generating chapters...**

2. Analyze the content to identify logical chapters based on:
   - Topic changes
   - Natural breaks in the conversation
   - Shifts in subject matter

3. For each chapter, extract 3-5 key points that capture the main ideas

4. For each chapter, also capture:
   - 2-4 lessons (concise takeaways)
   - 1-3 stories (anecdotes or narrative moments)
   - 2-4 examples (concrete demonstrations or scenarios)

5. Output: ✓ Identified [N] chapters

### Stage 4/4: Saving keypoints file

1. Output: **Stage 4/4: Saving keypoints file...**

2. Generate a markdown file with this structure:

```markdown
# Video Transcript Analysis

**Source transcript:** [filename]
**Processed:** [current date/time]

---

## Chapter 1: [Topic Name]
**Timestamp:** [start] - [end]

- Keypoint 1
- Keypoint 2
- Keypoint 3

**Lessons**
- Lesson 1
- Lesson 2

**Stories**
- Story 1

**Examples**
- Example 1
- Example 2

---

## Chapter 2: [Topic Name]
**Timestamp:** [start] - [end]

- Keypoint 1
- Keypoint 2
- Keypoint 3

**Lessons**
- Lesson 1
- Lesson 2

**Stories**
- Story 1

**Examples**
- Example 1
- Example 2

---

## Summary

[2-3 sentence summary of the entire video content]
```

3. Save the output to `keypoints/` directory
   - Filename format: `{original_basename}_keypoints.md`
   - Example: `dQw4w9WgXcQ_20240101_120000.txt` → `dQw4w9WgXcQ_20240101_120000_keypoints.md`

4. Output: ✓ Keypoints saved

### Final Summary

After all stages complete, output a summary:

```
---
✓ Complete!

Transcript: transcripts/[filename].txt
Keypoints:  keypoints/[filename]_keypoints.md
```
