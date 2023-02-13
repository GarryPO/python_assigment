import glob
import os
import pytest
from files_handler_class import Files_handler


@pytest.fixture
def files_hadndler():
    pathA = "dirs/a"
    pathB = "dirs/b"
    pathC = "dirs/c"
    files_handler = Files_handler(pathB, pathA, pathC)
    return files_handler


@pytest.fixture(autouse=True, scope='function')
def destentation_cleanup():
    yield
    files = glob.glob('dirs/c/*')
    for f in files:
        os.remove(f)
    try:
        os.remove('test.txt')
    except FileNotFoundError as e:
        pass    

def test_compare_sets(files_hadndler):

    assert files_hadndler.compare_sets(
        [8, 2, 3], [1, 4, 8]) == 1, 'Compare score is incorrect'
    
    assert files_hadndler.compare_sets(
        [1, 2, 3], [1, 1]) == 2, 'Compare score is incorrect'
    
    assert files_hadndler.compare_sets(
        [-1, 2, 3], [1, 4, 8]) == 0, 'Compare score is incorrect'
    
    assert files_hadndler.compare_sets(
        ['a', 2, 3], [1, 4, 8]) == 0, 'Compare score is incorrect'
    
    assert files_hadndler.compare_sets(
        [1, 2, 3], [1, 2, 8]) == 2, 'Compare score is incorrect'
    
    assert files_hadndler.compare_sets(
        [14, 62324, 42, 4, 2, -87], [1, 4, 2, 234, 23, 3, 8, -87]) == 3, 'Compare score is incorrect'


def test_copy_file_to_c(files_hadndler):
    f= open('test.txt','w') 
    f.write('Test string to be found')
    f.close()
    files_hadndler.copy_file_to_C(f.name, files_hadndler.pathC)
    test_file_path = f'{files_hadndler.pathC}/{f.name}'
    assert os.path.exists(test_file_path) is True, 'File wasn\'t copied'
    assert os.path.isfile(test_file_path) is True, 'Copied is not a file'


def test_update_scores_file(files_hadndler):

    files_hadndler.update_scores_file(
        'test_file_name', 10, files_hadndler.pathC)
    with open('dirs/c/scores.txt') as scores:
        score = scores.read()
        assert ('test_file_name' in score) is True, 'Path wasn\'t written'
        assert ('10' in score) is True, 'Score wasn\'t written'


def test_check_if_path_exist(files_hadndler):

    assert files_hadndler.check_if_path_exist(
        ['ff', None, 123]) is False, 'Unexisting path reported as existing!'

    assert files_hadndler.check_if_path_exist(
        ['ff', 'ddd', 123]) is False, 'Unexisting path reported as existing!'

    assert files_hadndler.check_if_path_exist(
        files_hadndler.path_list) is True, 'Existing path reported as unexisting!'

   
def test_is_int(files_hadndler):
    assert files_hadndler.is_int(0) is True, 'Should be True for int!'
    assert files_hadndler.is_int(-45) is True, 'Should be True for int!'
    assert files_hadndler.is_int(187878) is True, 'Should be True for int!'
    assert files_hadndler.is_int(
        0.2412) is False, 'Should be False for double!'
    assert files_hadndler.is_int("a") is False, 'Should be False for non int!'


def test_input_exeption_paths():
    with pytest.raises(AssertionError) as e_inf:
        f_h = Files_handler('test','ste','dddd')
        f_h.main(3)
        print(e_inf.value)
    assert str(e_inf.value) == "One of the paths doesn't exist - check the input", 'Expected exeption is not present'

def test_input_exeption_score(files_hadndler):
    min_amount = 'string'

    with pytest.raises(AssertionError) as e_inf:
        files_hadndler.main(min_amount)   
    assert str(e_inf.value) ==  f"Value passed - {min_amount} - is not an integer - check the  input", 'Expected exeption is not present'


def test_files_handler():
    pathA = "dirs/a"
    pathB = "dirs/b"
    pathC = "dirs/c"
    min_amount = 1
    #asserting 1 since I used .gitkeep to be able to commit c folder to git
    assert len(os.listdir(pathC)) == 1,'Folder is not empty'
    files_handler = Files_handler(pathB, pathA, pathC)
    files_handler.main(min_amount)  

    assert len(os.listdir(pathC)) == 3,'Files to be copied are missing'
          