## Setting Up the Project

### Step 1: Clone the Project

To get started, first clone the project repository:

```bash id="3kgl4b"
git clone <your-repository-url>
cd <project-directory>
```

### Step 2: Create and Activate a Virtual Environment

Create a virtual environment for the project:

```bash id="qzwkao"
python -m venv venv
```

Activate the virtual environment:

* On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

* On Windows:

  ```bash
  venv\Scripts\activate
  ```

### Step 3: Install Dependencies

Once the virtual environment is activated, install the required dependencies:

```bash id="lmbsch"
pip install -r requirements.txt
```

```bash id="f9089b"
podman run <your-podman-image>
```

### Step 5: Run the Django Development Server

To start the Django development server, run the following command:

```bash id="p8floa"
python manage.py runserver
```

The app should now be accessible at `http://127.0.0.1:8000/`.

---

## Creating a Course

To create a course, you first need to create a teacher. Here’s how you can do that:

### Step 1: Create a Teacher

To sign up as a teacher, visit the following URL:

```id="fs2x55"
/users/teacher/signup
```

Or, alternatively, you can click on the “Sign up as Teacher” button.

### Step 2: Create a Superuser

Next, create a superuser to access the Django admin panel. In your command line, run:

```bash id="baya4f"
django-admin createsuperuser
```

Follow the prompts to set up the admin user.

### Step 3: Access the Admin Panel

Once the superuser is created, you can log in to the admin panel at:

```id="4omxgk"
http://127.0.0.1:8000/admin/
```

Use the superuser credentials to log in.

### Step 4: Create a Course

* In the Django admin panel, go to the **Courses** section.
* Click on the **Add** button to create a new course.
* For the **Author** field, select the teacher you created earlier.

You can now add course details, and it will be associated with the teacher you signed up.

### Step 5: Add Lessons (Inline)

Once the course is created, you can add lessons to it. These lessons will appear inline under the course in the admin panel.

---

## Creating a Student Account and Enrolling in a Course

Now, let's create a student account and have the student enroll in a course.

### Step 1: Create a Student Account

To sign up as a student, go to:

```id="1pfgq5"
/users/student/signup
```

Complete the registration process.

### Step 2: Log in as a Student

After creating a student account, log in using the student credentials.

### Step 3: Explore Courses

Once logged in, visit the home page and click on the **Explore Courses** button to view available courses.

### Step 4: Enroll in a Course

To enroll in a course, click on the course you're interested in, then click the **Enroll** button.

The student will now be enrolled in the course.

