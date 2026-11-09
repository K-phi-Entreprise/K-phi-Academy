# Lesson videos

Rendered with Pillow and ffmpeg. `python3 lv.py F2.3 out/f2-3.mp4` renders one lesson from `scripts_f.py` (scenes, durations, captions) and writes the `.mp4` and its `.vtt` captions. F1.1 has its own script, `lesson_f11.py`.

`shots/` holds screens captured from the staging demo (dark theme). Copy the rendered `.mp4` and `.vtt` into `site/static/videos/`; the site picks them up by lesson code.

## Narration

`narrate.py` reads each caption aloud with Kokoro-82M (Apache 2.0) through `kokoro-onnx`, voice `af_heart` by default (`KPHI_VOICE` to change). Model files: `onnx/model.onnx` and `voices/*.bin` from the Hugging Face repo onnx-community/Kokoro-82M-v1.0-ONNX, packed into `voices.npz` in `KPHI_TTS_DIR` (default /tmp/tts). Scenes stretch to fit what is said; `NARRATE=0` renders without a voice.
