# Lesson videos

Rendered with Pillow and ffmpeg. `python3 lv.py F2.3 out/f2-3.mp4` renders one lesson from `scripts_f.py` (scenes, durations, captions) and writes the `.mp4` and its `.vtt` captions. F1.1 has its own script, `lesson_f11.py`.

`shots/` holds screens captured from the staging demo (dark theme). Copy the rendered `.mp4` and `.vtt` into `site/static/videos/`; the site picks them up by lesson code.
