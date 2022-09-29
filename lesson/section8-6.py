import glob
import zipfile

# zipfile

with zipfile.ZipFile('test.zip', 'w') as z:
    # z.write('test_dir')
    # z.write('test_dir/test.txt')
    for f in glob.glob('lesson/test_dir/**', recursive=True):
        print(f)
        z.write(f)

with zipfile.ZipFile('test.zip', 'r') as z:
    # z.extractall('zzz')
    with z.open('test_dir/test.txt') as f:
        print(f.read())