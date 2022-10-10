"""Utils to display to be returned to the user on the console."""
import os
import string

import termcolor


def get_template_dir_path():
    """Return the path of the template's directory.
    テンプレートディレクトリのパスを返す

    戻り値
    Returns:
        文字列型: テンプレートディレクトリのパス
        str: The template dir path.
    """
    # 初期値を None にする
    template_dir_path = None
    # 例外処理
    try:
        # settingsモジュールがあれば読み込む
        import settings
        # settingsにTEMPLATE_PATHがあれば、それを template_dir_path に代入する
        if settings.TEMPLATE_PATH:
            template_dir_path = settings.TEMPLATE_PATH
    except ImportError:
        # モジュールがなければ pass
        pass

    # setting モジュールが存在せず、template_dir_path が None
    if not template_dir_path:
        """
        os.path.abspath(__file__) でこのファイルの絶対パスを取得
        os.path.dirname(os.path.abspath(__file__)) でこのファイルが入っているディレクトリ名を取得
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))) で
        os.path.dirname(os.path.abspath(__file__)) の上の階層のディレクトリ名を取得
        roboter のディレクトリを取得する
        """
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # base_dir(roboter) のまでのパスと 'templates' を結合する
        # ~\roboter\templates
        template_dir_path = os.path.join(base_dir, 'templates')

    return template_dir_path

# Exception のクラスを継承する
class NoTemplateError(Exception):
    """No Template Error"""

def find_template(temp_file):
    """Find for template file in the given location.
    引数に渡されたテンプレートファイルを探す

    戻り値
    Returns:
        テンプレートファイルのパス
         str: The template file path

    独自例外
     Raises:
         テンプレートが存在しなければ NoTemplateError を返す
         NoTemplateError: If the file does not exists.
    """
    # get_template_dir_path の戻り値
    template_dir_path = get_template_dir_path()
    # パスの結合(template_dir_path と 引数で渡された temp_file)
    temp_file_path = os.path.join(template_dir_path, temp_file)
    # temp_file_path のパスが存在しなければ NoTemplateError を処理する
    if not os.path.exists(temp_file_path):
        # temp_file を format で代入する
        raise NoTemplateError('Could not find {}'.format(temp_file))
    # 戻り値に temp_file_path
    return temp_file_path

def get_template(template_file_path, color=None):
    """Return the path of the template.
    テンプレートのパスを返す

    引数
    Args:
        template_file_path にはテンプレートファイルのパスを渡す
        template_file_path (str): The template file path
        color にはターミナルに表示する色を渡す
        color: (str): Color formatting for output in terminal
            詳細
            see in more details: https://pypi.python.org/pypi/termcolor

    戻り値
    Return:
        テンプレートに含まれる文字を含むテンプレートを返す
        string.Template: Return templates with characters in templates.
    """
    # template に find_template関数に引数に渡された template_file_path を渡す
    template = find_template(template_file_path)
    # 'r'モードにし、template を読み取る
    # エンコードに 'utf-8' を指定する
    with open(template, 'r', encoding='utf-8') as template_file:
        # template_file を読み込む
        contents = template_file.read()
        # os.linesep で該当の OS におけるの改行コードを取得する
        # contents の右側から取り除いた文字を返す
        contents = contents.rstrip(os.linesep)
        # "=" で囲んだ中にテンプレートを入れる
        # os.linesep は該当の OS における改行コード
        contents = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(
            contents=contents, splitter='=' * 60, sep=os.linesep
        )
        # 出力する文字列を引数で渡された色に変換する
        contents = termcolor.colored(contents, color)
        # 標準ライブラリの string の Template関数によって文字列に $ を含んだテンプレートを使用可能にする
        return string.Template(contents)
