from models.engine.file_storage import FileStorage

# create an instance of file storage
storage = FileStorage()

# call the reload() method to load data from the JSON file
storage.reload()