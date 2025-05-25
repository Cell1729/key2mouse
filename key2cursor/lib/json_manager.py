import json

def load_json(file_path):
    """
    JSONファイルを読み込み、Pythonの辞書型に変換する関数
    :param file_path: 読み込むJSONファイルのパス
    :return: JSONデータを含む辞書型オブジェクト
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data