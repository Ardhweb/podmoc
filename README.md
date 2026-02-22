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
<img width="1023" height="767" alt="Screenshot_7" src="https://github.com/user-attachments/assets/52ef4b7a-5d6b-4f7b-a5d0-396828c3a80f" />
<img width="1023" height="767" alt="Screenshot_6" src="https://github.com/user-attachments/assets/c11981fa-6d04-4d37-af38-3d1d53c61850" />
<img width="1023" height="767" alt="Screenshot_5" src="https://github.com/user-attachments/assets/f234a375-3646-4dd0-848f-e5b636530ffc" />
<img width="1023" height="767" alt="Screenshot_4" src="https://github.com/user-attachments/assets/f7774ff4-97da-42b5-871f-023411f79c68" />
<img width="1023" height="767" alt="Screenshot_3" src="https://github.com/user-attachments/assets/6194707c-51fe-45ae-a162-42aa82024e89" />
<img width="1023" height="681" alt="Screenshot_2" src="https://github.com/user-attachments/assets/93b8c032-4bc7-41bc-a89f-ed4686a93fe3" />
<img width="1023" height="767" alt="Screenshot_17" src="https://github.com/user-attachments/assets/a8213890-3af2-4199-90ea-4dd9ae27cb02" />
<img width="753" height="607" alt="Screenshot_16" src="https://github.com/user-attachments/assets/f5fb87c2-0ac0-440b-881a-c2777381dfc8" />
<img width="1023" height="767" alt="Screenshot_15" src="https://github.com/user-attachments/assets/586dff76-0bf4-4cca-873e-4da514558e7a" />
<img width="1023" height="767" alt="Screenshot_14" src="https://github.com/user-attachments/assets/66321ca3-ccf7-45b3-9041-d76a20b8eb35" />
<img width="1023" height="767" alt="Screenshot_13" src="https://github.com/user-attachments/assets/bc17953a-530e-4c74-b07a-d607b8220c09" />
<img width="1023" height="767" alt="Screenshot_12" src="https://github.com/user-attachments/assets/35cde3c4-7d33-4980-abd3-864ee655656b" />
<img width="1023" height="767" alt="Screenshot_11" src="https://github.com/user-attachments/assets/fac91582-9c0d-4b7c-bbff-716057387d7a" />
<img width="1023" height="767" alt="Screenshot_10" src="https://github.com/user-attachments/assets/a0577e06-c03f-4822-91e3-0019839d4873" />
<img width="1023" height="767" alt="Screenshot_9" src="https://github.com/user-attachments/assets/e0e45e6d-78e1-42dc-9faf-dbd4916b7a21" />
<img width="1023" height="767" alt="Screenshot_8" src="https://github.com/user-attachments/assets/93273e06-9bc6-488c-a8a3-c6f918871e4b" />

<img width="1023" height="767" alt="Screenshot_17" src="https://github.com/user-attachments/assets/5bea78f3-a925-4b45-ab69-17361ef2f341" />

## Admin Panel Creditonal:
username: admin
password: admin
