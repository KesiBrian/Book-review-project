// src/components/Register.js
import React from 'react';
import { Formik, Field, Form } from 'formik';
import axios from 'axios';

const Register = () => {
  return (
    <div>
      <h1>Register</h1>
      <Formik
        initialValues={{ username: '', email: '', password: '' }}
        onSubmit={async (values) => {
          try {
            const response = await axios.post('/api/register', values);
            console.log(response.data);
            // Redirect to login page
          } catch (error) {
            console.error(error);
          }
        }}
      >
        <Form>
          <div>
            <Field name="username" placeholder="Username" />
          </div>
          <div>
            <Field name="email" type="email" placeholder="Email" />
          </div>
          <div>
            <Field name="password" type="password" placeholder="Password" />
          </div>
          <button type="submit">Register</button>
        </Form>
      </Formik>
    </div>
  );
};

export default Register;
