// src/components/Login.js
import React from 'react';
import { Formik, Field, Form } from 'formik';
import axios from 'axios';

const Login = () => {
  return (
    <div>
      <h1>Login</h1>
      <Formik
        initialValues={{ username: '', password: '' }}
        onSubmit={async (values) => {
          try {
            const response = await axios.post('/api/login', values);
            console.log(response.data);
            // Redirect to dashboard or other page
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
            <Field name="password" type="password" placeholder="Password" />
          </div>
          <button type="submit">Login</button>
        </Form>
      </Formik>
    </div>
  );
};

export default Login;
