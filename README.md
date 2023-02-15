# Python home assigment

## Class to be tested - Files_handler 

### Files_handler goal is to compare CSV's provided to it and to find if they contain the same elements and if they do to check
### If number of similarities found corresponds to score number provided as argument for a main function of the class to copie file that was being compared to the destination location provided during class init

## Tests are iplemented using pytest framework 

### To run tests - 

### 1. Clone repository

### 2 . cd to project root

### 3. Run 'pip install -r requirements.txt'

### 4. Run pytest comand 


# Part II - API anylises 

##  General  testing approach 
### No matter whats the neture of endpoint there are couple of cases to be tested with any:
### 1. Check inplementation correctness - Naming conventions are followed, there are no mistakes in resource and itype definitions and that they follow defined object model
### 2. API operations tests - this kind of tests should cover if correctness of responses codes returned for resource or operation requested, payload verifications, response headers checks 
### 3.This kind of tests can logicaly be splitted in two categories - positive and negative, first once to cover all happy scenarios when everything should happen according to our expectations and negative ones when API operation requsted cannot be performed due  to missing/incorrect input, like missing payload fields or specific headers  
### 4. Another part of API testing would be user permissions and sequrity tests - checking that user are not able to access resourses that doesn't confirm his permissions, trying to request an API operation with missing authorisation etc.
### 5. If an anpoind under test confirms OpenAPI standarts may parts of testing can be achieved by tools like https://schemathesis.readthedocs.io/en/stable/ - it can help to find all the places where API undertest break unexpectidly and return 500

## Create_Camera() testing 
### It would be easier to acomplish this assimnet if url to swagger.json would be provided. Also there is not enough info about rebroadcasting address - it is not  clear from the screenshots provided if it is going to be generated and assigned automatiocally or user should provide it as an input.
### For testing of this endppint I would implement all kind of tests described above plus a couple of specific -
### 1. Happy camera initiation for each camera type - once correct input provided requested camera should be created abd should be accessible via assigned adress
### 2. Nagative initiation tests for each camera type - if input is incorrect or mandatory fields are missing  no cammera should be created, correct error message should be returned. 
### 3. Additionaly it is important to check correctness of camera settings and AI settings in the response object - if they confirm what whas originaly requested 

## Test example:

 ```
 import swagger_client
 import json
 from swagger_client import ApiExeption
 

def test_happy_camera_creation():
    swagger_client.configuration.access_token = 'some_token'
    api = swagger_client.CameraApi()
    good_payload = {"some":"jsone"}
    try:
        resp = api.create_camera(good_payload)
        body = json.loads(resp.body)
        assert body.get('mode') == good_payload.get('mode'), "Camera created with inorrect mode!"
        assert body.get('capture_address') == good_payload.get('capture_address'), "Cameras capture address is inorrect mode!"
        assert resp.status_code == 200, "Camera wasn't created!"
        
    expect ApiExeption as e:
        print(f"Exeption accured during camera creation - {str(e)}")    
  
  ```



