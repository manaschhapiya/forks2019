"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""

import json

facdetail = """

{
    
	"teacher": {
		"First Name": "Dr. smita",
		"Last Name": "Agarwal",
		"Photo": "https: //www.google.com/search?q=images&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjYr-DLopriAhUUOisKHc9QAVUQ_AUIDigB&biw=647&bih=590#",
		"Department": "CSE",
		"Research Areas": "cn , cgm",
		"Contact Details": 9782712309
	},


	"teacher1": {
		"First Name": "Dr. Manas",
		"Last Name": "Chhapiya",
		"Photo": " https:  //www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwjEqb7sopriAhXZR30KHVvGBmsQjRx6BAgBEAU&url=%2Furl%3Fsa%3Di%26source%3Dimages%26cd%3D%26ved%3D%26url%3Dhttps%253A%252F%252Fpixabay.com%252Fimages%252Fsearch%252Fflowers%252F%26psig%3DAOvVaw0J4GRxMr_oFU9mWFj0CTzk%26ust%3D1557897508263256&psig=AOvVaw0J4GRxMr_oFU9mWFj0CTzk&ust=1557897508263256",
		"Department": "CSE",
		"Research Areas": "cn , cgm",
		"Contact Details": 9787812309
	}

}

"""


stddetail =  """

{
    
	"student": {
		"First Name": "Manas",
		"Last Name": "Chhapiya",
		"Photo": "https: //www.google.com/search?q=images&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjYr-DLopriAhUUOisKHc9QAVUQ_AUIDigB&biw=647&bih=590#",
		"Department": "CSE",
		"Roll no.": "1egjcs104",
		"Contact Details": [9782712309,09874321234]
	}

}
"""