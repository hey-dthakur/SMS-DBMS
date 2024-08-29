CREATE TABLE department (
  department_id NUMBER(10) PRIMARY KEY,
  department_name VARCHAR2(50) NOT NULL,
  department_head VARCHAR2(50) NOT NULL
);


CREATE TABLE student (
  student_id NUMBER(10) PRIMARY KEY,
  student_name VARCHAR2(50) NOT NULL,
  student_email VARCHAR2(50) NOT NULL,
  student_phone VARCHAR2(20) NOT NULL,
  department_id NUMBER(10) REFERENCES department(department_id)
);


CREATE TABLE faculty (
  faculty_id NUMBER(10) PRIMARY KEY,
  faculty_name VARCHAR2(50) NOT NULL,
  faculty_email VARCHAR2(50) NOT NULL,
  department_id NUMBER(10) REFERENCES department(department_id)
);


CREATE TABLE course (
  course_id NUMBER(10) PRIMARY KEY,
  course_name VARCHAR2(50) NOT NULL,
  course_description VARCHAR2(200),
  faculty_id NUMBER(10) REFERENCES faculty(faculty_id),
  department_id NUMBER(10) REFERENCES department(department_id)
);


CREATE TABLE enrollment (
  enrollment_id NUMBER(10) PRIMARY KEY,
  student_id NUMBER(10) REFERENCES student(student_id),
  course_id NUMBER(10) REFERENCES course(course_id),
  enrollment_date DATE NOT NULL
);

CREATE TABLE attendance (
  attendance_id NUMBER(10) PRIMARY KEY,
  student_id NUMBER(10) REFERENCES student(student_id),
  course_id NUMBER(10) REFERENCES course(course_id),
  attendance_date DATE NOT NULL,
  attendance_status VARCHAR2(10) NOT NULL
);


CREATE TABLE grade (
  grade_id NUMBER(10) PRIMARY KEY,
  student_id NUMBER(10) REFERENCES student(student_id),
  course_id NUMBER(10) REFERENCES course(course_id),
  grade_value NUMBER(3,2) NOT NULL
);

CREATE TABLE fee_type (
  fee_type_id NUMBER(10) PRIMARY KEY,
  fee_type_description VARCHAR2(50) NOT NULL
);

CREATE TABLE fees (
  fee_id NUMBER(10) PRIMARY KEY,
  student_id NUMBER(10) REFERENCES student(student_id),
  fee_type_id NUMBER(10) REFERENCES fee_type(fee_type_id),fee_amount NUMBER(10),fee_date DATE not null );