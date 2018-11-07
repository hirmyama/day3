import boto3

s3 = boto3.resource('s3')


def create_bucket():
    bucket_name = input('バケット名: ')
    s3.Bucket(name=bucket_name).create(CreateBucketConfiguration={'LocationConstraint': 'ap-northeast-1'})


def delete_bucket():
    print('まだ実装されていません')


def list_bucket():
    for bucket in s3.buckets.all():
        print(bucket.name)


def put_object():
    print('まだ実装されていません')


def get_object():
    print('まだ実装されていません')


def exit_app():
    print('終了します')
    exit(0)


COMMANDS = {
    # 'コマンド', ('説明文', コマンドに対応する関数)
    'create bucket': ('バケットを作成', create_bucket),
    'delete bucket': ('バケットを削除', delete_bucket),
    'list buckets': ('バケットを一覧表示', list_bucket),
    'put object': ('オブジェクト（テキスト）を作成', put_object),
    'get object': ('オブジェクト（テキスト）を削除', get_object),
    'exit': ('アプリケーションを終了', exit_app),
    # オブジェクト一覧、ファイルアップロード/ダウンロード, 署名付きURL生成などを追加してください
}


def display_commands():
    for key, value in COMMANDS.items():
        print('{:<15} ... {}'.format(key, value[0]))


def main_loop():
    while True:
        display_commands()
        print('---')
        command = input('コマンド: ')
        description, func = COMMANDS[command]
        print(description)
        print('---')
        try:
            func()
        except Exception as e:
            print(e)
        print('---')


if __name__ == '__main__':
    main_loop()
