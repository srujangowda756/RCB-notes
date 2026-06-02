from zipfile import ZipFile, ZIP_DEFLATED, ZIP_STORED
with ZipFile('smaple.zip','w',ZIP_DEFLATED) as zip:
    zip.write('sample.txt')

