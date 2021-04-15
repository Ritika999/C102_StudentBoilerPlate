



def upload_file(img_name):
    access_token = ""
    file =img_name
    file_from = file
    file_to="/C102/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


