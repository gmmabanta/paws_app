import React, { Component } from "react"
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

const FormWrapper = styled.div`
    margin-top: 30px;
    display: grid;
    justify-content: center;
    align-items: center;
`;

class Login extends Component {
    constructor(props) {
      super(props);
      this.state = {
        username: '',
        password: ''
      };
    };

    render() {
        return (
            <LoginWrapper>
                <LogoWrapper>
                    <img src="http://thecreativecat.net/wp-content/uploads/PAWS-logo.jpg" alt="PAWS" height='200px'/>
                </LogoWrapper>
                    <FormWrapper>
                        <FieldInput id="username" fieldname="Username" type="text" />
                        <FieldInput fieldname="Password" type="password" />
                        <LoginButton type="submit" >LOGIN</LoginButton>
                    </FormWrapper>        
            </LoginWrapper>
        )
    }
  }
  
export default Login;