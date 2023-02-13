from files_handler_class import Files_handler


pathA = "dirs/a"
pathB = "dirs/b"
pathC = "dirs/c"
min_amount = 1

files_handler = Files_handler(pathB, pathA, pathC)
files_handler.main(min_amount)