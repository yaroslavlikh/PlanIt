import faster_whisper

whisper_model = faster_whisper.WhisperModel("small", device="cpu", compute_type="int8")
import tempfile
import os

def new_voice(message, bot):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with tempfile.NamedTemporaryFile(suffix=".ogg", delete=False) as tmp:
        tmp.write(downloaded_file)
        tmp_path = tmp.name

    segments, _ = whisper_model.transcribe(tmp_path, language="ru")
    user_text = "".join(seg.text for seg in segments).strip()
    print(user_text)
    os.unlink(tmp_path)

    if not user_text:
        bot.reply_to(message, "Не удалось распознать речь. Попробуйте ещё раз.")
        return
    return user_text