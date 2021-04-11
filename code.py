import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)
def main():
    access_token = 'PZeC8RnMctsAAAAAAAAAAfWVixjCuQVg6LSodGpB5DSoVX7BV4Y1b4pzIo6r0dta'
    transferData = TransferData(access_token)
    file_from = input("Enter The File Pass To Transfer")
    file_to = input("Enter The Full Pass To Upload To Drop Off")
    transferData.upload_file(file_from, file_to)
    print("File Has Been Moved")

main()