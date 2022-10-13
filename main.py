import whisper

model = whisper.load_model("large")
options = whisper.DecodingOptions(language="ja", without_timestamps=True)
result = model.transcribe("sound.m4a")
print(result["text"])