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

const todoItems = [
  {
    id: 1,
    title: "Nature walk in the park",
    description: "Visit the park with my friends",
    completed: true
  },

  {
    id: 2,
    title: "Visit",
    description: "Got to my aunt's place",
    completed: true
  },

  {
    id: 3,
    title: "Write",
    description: "Do an article about anthropology",
    completed: true
  },
];

class Login extends Component {
    constructor(props) {
      super(props);
      this.state = {todoItems};
    };

    render() {
        return (
            <LoginWrapper>
                <LogoWrapper>
                    <img src="http://thecreativecat.net/wp-content/uploads/PAWS-logo.jpg" alt="PAWS" height='200px'/>
                </LogoWrapper>
                    <FormWrapper>
                        <FieldInput fieldname="Username" />
                        <FieldInput fieldname="Password" />
                        <LoginButton>LOGIN</LoginButton>
                    </FormWrapper>
                
                                
            </LoginWrapper>
    //     <main className="content">
    //     <LoginButton>Button</LoginButton>
    //     <div className="row">
    //       <div className="col-md-6 col-sm-10 mx-auto p-0">
    //         <div className="card p-3">
    //           <ul className="list-group list-group-flush">
    //           {this.state.todoItems.map(item => (
    //           <div>
    //             <h1>{item.title}</h1>
    //             <span>{item.description}</span>
    //           </div>
    //           ))}
    //           </ul>
    //         </div>
    //       </div>
    //     </div>
    //   </main>
      )
    }
  }
  
export default Login;