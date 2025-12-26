import faster_whisper

import tempfile
import os


whisper_model = faster_whisper.WhisperModel("small", device="cpu", compute_type="int8")
def new_voice(message, bot):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # Сохраняем во временный файл
    with tempfile.NamedTemporaryFile(suffix=".ogg", delete=False) as tmp:
        tmp.write(downloaded_file)
        tmp_path = tmp.name

    # Распознаём через Whisper
    segments, _ = whisper_model.transcribe(tmp_path, language="ru")
    user_text = "".join(seg.text for seg in segments).strip()

    os.unlink(tmp_path)  # Удаляем временный файл

    if not user_text:
        bot.reply_to(message, "Не удалось распознать речь. Попробуйте ещё раз.")
        return
    return user_text