---
name: process-transcript
description: Analyze a YouTube transcript file and generate chapter breakdown with keypoints
argument-hint: "<transcript-file>"
allowed-tools: Read, Write, Glob
---

# Process YouTube Transcript

Analyze a transcript file and create a chapter breakdown with keypoints.

## Instructions

1. **Read the transcript file**: `$ARGUMENTS`
   - If no argument provided, use Glob to find the most recent file in `transcripts/`

2. **Analyze the content** to identify logical chapters based on:
   - Topic changes
   - Natural breaks in the conversation
   - Shifts in subject matter

3. **For each chapter**, extract 3-5 key points that capture the main ideas

4. **For each chapter**, also capture:
   - 2-4 lessons (concise takeaways)
   - 1-3 stories (anecdotes or narrative moments)
   - 2-4 examples (concrete demonstrations or scenarios)

5. **Generate a markdown file** with this structure:

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

6. **Save the output** to `keypoints/` directory
   - Filename format: `{original_basename}_keypoints.md`
   - Example: `dQw4w9WgXcQ_20240101_120000.txt` → `dQw4w9WgXcQ_20240101_120000_keypoints.md`

7. **Report** the output file path to the user
