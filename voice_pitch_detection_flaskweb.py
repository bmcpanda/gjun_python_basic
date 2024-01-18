from flask import Flask, request, jsonify, render_template
from pitch_detection import fundamental_frequency_pitch_track
import os

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def voice_pitch_detection_upload():
    return render_template('page_1.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'audioFile' not in request.files:
        return jsonify({'message': '沒有選擇檔案'}), 400

    audio_file = request.files['audioFile']

    if not audio_file.filename.endswith('.wav') and not audio_file.filename.endswith('.mp3'):
        return jsonify({'message': '檔案不是WAV或MP3'}), 400

    # 將檔案保存到 uploads 資料夾中
    audio_file.save('uploads/' + audio_file.filename)
    fundamental_frequency_pitch_track('uploads/', audio_file.filename)

    return jsonify({'message': '檔案上傳成功'}), 200


@app.route('/check_upload_status/<jpg_name>', methods=['GET'])
def check_upload_status(jpg_name):
    print(os.path.exists(jpg_name))
    # 在這裡檢查檔案處理的狀態，並返回相應的 JSON 對象
    # 例如，如果檔案處理成功，可以返回 {'status': 'success'}
    # 如果檔案還在處理中，可以返回 {'status': 'processing'}
    # 如果檔案處理失敗，可以返回 {'status': 'failure'}

    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True)
