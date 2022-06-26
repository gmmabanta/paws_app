import React, { useState } from "react"
import LoginButton from "../common/LoginButton";
import styled from "styled-components";
import FieldInput from "../common/FieldInput";

const LoginWrapper = styled.div`
    background-color: #BDDDBB;
    max-width: 450px;
    margin: auto;
    justify-content: center;
    align-items: center;
    border-radius: 10px;
    margin-top: 100px;
    padding-left: 20px;
    padding-right: 20px;
    padding-top: 50px;
    padding-bottom: 50px;
`;

const LogoWrapper = styled.div`
    width: 200px;
    height: 200px;
    border-radius: 50%;
    overflow: hidden;
    margin: auto;
`;

const FormWrapper = styled.form`
    margin-top: 30px;
    display: grid;
    justify-content: center;
    align-items: center;
`;

function Login () {
  const [username, setUsername] = useState('');
  const [password1, setPassword1] = useState('');
  const [password2, setPassword2] = useState('');

  const submitHandler = (e) => {
    e.preventDefault();
    console.log('submitted');
    console.log('username', username);
    console.log('password', password1);
    // handle login POST request
  }

  return (
    <LoginWrapper>
      <LogoWrapper>
        <img src="http://thecreativecat.net/wp-content/uploads/PAWS-logo.jpg" alt="PAWS" height='200px'/>
      </LogoWrapper>
      <FormWrapper onSubmit={submitHandler}>
        <FieldInput 
          id="username" 
          fieldname="Username" 
          type="text" 
          value={username} 
          onChangeHandler={setUsername}
        />
        <FieldInput 
          fieldname="Password" 
          type="password" 
          value={password1} 
          onChangeHandler={setPassword1}
        />
        <LoginButton type="submit">LOGIN</LoginButton>
      </FormWrapper>        
    </LoginWrapper>
  );
} 

export default Login;