```

To run this application do the following;
  - Make sure you have installed python3.8 or higher
  - Install pip3

  - After installing the above, run the following command.
```
```
 pip install -r requirements.txt 
 python manage.py makemigrations 
 python manage.py migrate
 python manage.py runserver
 ```

- The above is a 4 commands line which you can split into individuals if you want so.,



### The following are functional requirements that were achieved in this phase
  - A home Page to welcome new users and also redirect them to other pages.
  - All data tables were implimented
  - Account registration and Login for both Teacher and Student.
  - Teacher can be able to create a classroom, A course etc/.
  - A teacher can be able to view his profile and  dashboard for the course he is tutoring.
  - A teacher is able to add, Delete, Update and Modify assginemts.
  - A teacher is able to view all students who has joined his Class.

  - Student Module is halfway done and a student can only register and signin. No further functionalities after here.



  ### 6.3 Testing

  Software testing is an essential phase in the development life cycle of an application. Testing ensures that the developed system meets its functional and non-functional requirements. Two important terms in software testing are Verification and Validation.

  Verification is the process of evaluating work-products like requirement specs, design specs and test cases etc. of different development phases to make sure that they meet the requirements for that phase. It ensures that the system is built in the right way.

  Validation is the process of evaluating the software at the end of the development phase to make sure that it meets the business requirements. It is used to make sure that the product fulfills its intended use and that the end product is built right.

  #### Test Data

  System testing was achieved using Dummy data as test data since a lot of data is required. Fake(dummy) data was created. System testing is done in the following technique

  1. **Functionality Testing**

  Below are some of the checks that are performed:

  - Verification that there is no dead page or invalid redirects- system passes this
  - Check all the validations on each field- No form submission is done without filling all the necessary fields.
  - Verification of the workflow of the system- the data workflow of the system is correct and consistent.
  - Verify the data integrity- the data integrity of properties/land assumed to be valid as the owner has to upload valid details.

  2. **Usability Testing**

  To verify how the application is easy to use with.

  - Test the navigation and controls. -The system has easy navigation from login, dashboard, profile, faq and home view.
  - Content checking- Every user is able to check the available content he/she is authorized to view

  3. **Interface Testing**

  Performed to verify the interface and the dataflow from one system to other. The blockchain land registry system interfaces can be between the API's used. System interface testing passed well.

  4. **Compatibility testing**

  Compatibility testing is performed based on the context of the application.

  - Browser compatibility- The system is compatible to 98% of browsers, google chrome, opera mini, Mozilla Firefox, Internet Explorer, Torch browser, UC browser .
  - Responsiveness- The web system is compatible to various devices like notebook, mobile, tv and laptops.

      1. **Performance testing**

  Performed to verify the server response time and throughput under various load conditions.

  - **Load testing -** It is the simplest form of testing conducted to understand the behavior of the system under a specific load. Load testing will result in measuring important business critical transactions and load on the database, application server, etc. are also monitored.

  Load testing of the Elearniung  system was done on loading of home page. 6 dummy data  were created for each model. 
 


  6. **Security testing -** Performed to verify if the application is secured on web as data theft and unauthorized access are more common issues and below are some of the techniques to verify the security level of the system.

  - Broken Authorization and Session Management- the system passes this test as a user cannot access the 'Elearning resources/assignments which might be confidential'. Middleware implemented for each route
  - Insecure Direct Object References- Teacher/Students  can only update or view his or her required itesm . No common user can update any resources.
  - Sensitive Data Exposure- all sensitive data of users e.g password and username are only known to the owner. Password are salted before storage.
  - Unvalidated Redirects and Forwards- all redirects and forwards in the system follows after a middleware function which validates if the requesting user is authorized for the route.

  Unit testing is a strategy in software testing where individual components in a software are tested for correctness.

  #### Test Plan.

  The test plan shown below includes test cases test result and test data.

  | S.No | Test Case | Pre-Condition | Post-Condition | Results |
  | --- | --- | --- | --- | --- |
  | 1 | User registration | User will be on registration page. User will fill the form by providing unique username, email, contact and other details depending on whether He is a techer or a student. | On submitting the form, user data will be stored in the database and can now login with the username key. | Pass |
  | 2 | Login | User must be able to see a form prompting him to provide his unique username key for the user and submit it. Otherwise create new account where user will be on test(1). | On submitting the form, if credentials are correct, user will be redirected to dashboard of the app. Otherwise, a message of wrong credentials returned | Pass |
| 3 | Dashboard Navigation Click | None | My Courses, Assignments,Available Classrooms or Profile links are displayed for Student while Teacher's dashboard has the controls for **Add Assignment, Resources, Add a classroom or stream, Perfom CRUD operation on assignments and resources, logout etc** | Pass |
| 4 | View profile | Teacher/Student will be able to view his/her profile. User can now change the account details. | User changed details are updated and new details returned on the page. | Pass |
| 5 | Redirect To Individual Required Dashboard | Teacher/Student will be able to be rediirected to their dashboard after login or registration i.e When a student logins, he should be redirected to his dashboard but not that of a teacher. | Teacher are redicted to dashboard that allows them to perform teacher's duty while student are on empty page no implimented. | Pass for Teachers , Unimplimented for students |
| 6 | Models Implimented  | Each Model Specifies is implimented and accepts all its required data and format. | Every Model or data table was able to insert data and raise Exeptions for incorrect data| Pass |
| 7 | Double Registration | No email or username should be registered twice | The application raises an error when username/email already in the database is re-registered again. | Pass |
| 8 | Authenticity and Authorization of resources | No teacher that should be able to view a resources uploaded by another for a particular course | Teachers are able to access the resources or assignments which are created for his course and section. | Pass |
