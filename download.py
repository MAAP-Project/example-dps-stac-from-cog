import fsspec
import fire

def download(download_from: str, download_to: str):
    assert download_from.startswith('s3://')
    fs = fsspec.filesystem('s3')
    try:
        fs.download(download_from, download_to)
    except Exception as ex:
        print(f'Error downloading {download_from} to {download_to}')
        raise

if __name__ == '__main__':
    fire.Fire(download)